# what_to_watch/opinions_app/views.py

from random import randrange
from flask import abort, flash, redirect, render_template, url_for
from . import app, db
from .models import Opinion
from .forms import OpinionForm
# Добавьте импорт функции для загрузки данных
from .dropbox import upload_files_to_dropbox


def random_opinion():
    quantity = Opinion.query.count()
    if quantity:
        offset_value = randrange(quantity)
        opinion = Opinion.query.offset(offset_value).first()
        return opinion


@app.route('/')
def index_view():
    opinion = random_opinion()
    # Если random_opinion() вернула None, значит, в БД нет записей.
    if opinion is None:
        abort(500)
    return render_template('opinion.html', opinion=opinion)


@app.route('/add', methods=['GET', 'POST'])
def add_opinion_view():
    form = OpinionForm()
    if form.validate_on_submit():
        text = form.text.data
        if Opinion.query.filter_by(text=text).first() is not None:
            flash('Такое мнение уже было оставлено ранее!')
            return render_template('add_opinion.html', form=form)
        urls = upload_files_to_dropbox(form.images.data)
        opinion = Opinion(
            title=form.title.data,
            text=text,
            source=form.source.data,
            images=urls
        )
        db.session.add(opinion)
        db.session.commit()
        return redirect(url_for('opinion_view', id=opinion.id))
    return render_template('add_opinion.html', form=form)


@app.route('/opinion/<int:id>')
def opinion_view(id):
    opinion = Opinion.query.get_or_404(id)
    return render_template('opinion.html', opinion=opinion)
