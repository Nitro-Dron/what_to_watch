# what_to_watch/opinions_app/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, URLField
from wtforms.validators import DataRequired, Length, Optional
from flask_wtf.file import FileAllowed, MultipleFileField


class OpinionForm(FlaskForm):
    title = StringField(
        'Введите название фильма',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(1, 128)]
    )
    text = TextAreaField(
        'Напишите мнение',
        validators=[DataRequired(message='Обязательное поле')]
    )
    source = URLField(
        'Добавьте ссылку на подробный обзор фильма',
        validators=[Length(1, 256), Optional()]
    )
    # Добавьте новое поле в форму.
    images = MultipleFileField()
    submit = SubmitField('Добавить')
    images = MultipleFileField(
        validators=[
            FileAllowed(
                # Список разрешенных расширений для файлов.
                ['jpg', 'jpeg', 'png', 'gif', 'bmp'],
                # Сообщение, в случае если расширение не совпадает.
                message=(
                    'Выберите файлы с расширением '
                    '.jpg, .jpeg, .png, .gif или .bmp'
                )
            )
        ]
    )
