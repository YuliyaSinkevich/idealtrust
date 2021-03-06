from flask_wtf import FlaskForm
from flask_babel import lazy_gettext

from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email


class SignupForm(FlaskForm):
    email = StringField(lazy_gettext(u'Email:'),
                        validators=[InputRequired(), Email(message=lazy_gettext(u'Invalid email')), Length(max=30)])
    password = PasswordField(lazy_gettext(u'Password:'), validators=[InputRequired(), Length(min=6, max=80)])
    submit = SubmitField(lazy_gettext(u'Sign Up'))


class SigninForm(FlaskForm):
    email = StringField(lazy_gettext(u'Email:'),
                        validators=[InputRequired(), Email(message=lazy_gettext(u'Invalid email')), Length(max=30)])
    password = PasswordField(lazy_gettext(u'Password:'), validators=[InputRequired(), Length(min=6, max=80)])
    submit = SubmitField(lazy_gettext(u'Sign In'))


class ContactForm(FlaskForm):
    email = StringField(lazy_gettext(u'Email:'),
                        validators=[InputRequired(), Email(message=lazy_gettext(u'Invalid email')), Length(max=30)])
    subject = StringField(lazy_gettext(u'Subject:'), validators=[InputRequired(), Length(min=1, max=80)])
    message = StringField(lazy_gettext(u'Message:'), validators=[InputRequired(), Length(min=1, max=500)])
    submit = SubmitField(lazy_gettext(u'Send'))
