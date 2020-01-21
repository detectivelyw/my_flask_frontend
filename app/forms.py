from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')

class PostForm(FlaskForm):
    kernel_version = SelectField(
        'Please Choose a LinuxKit Kernel Version',
        choices=[('4.4', '4.4'), ('4.9', '4.9'), ('4.14', '4.14'), ('4.15', '4.15')]
    )
    container = SelectField(
        'Please Choose a Docker Container to Run',
        choices=[('all', 'all'), ('nginx', 'nginx'), ('alpine', 'alpine'), ('busybox', 'busybox'), ('redis', 'redis'), ('mongo', 'mongo'), ('httpd', 'httpd'), ('ubuntu', 'ubuntu'), ('postgress', 'postgress'), ('node', 'node'), ('mysql', 'mysql'), ('memcached', 'memcached'), ('registry', 'registry'), ('traefik', 'traefik'), ('hello-world', 'hello-world'), ('golang', 'golang'), ('docker', 'docker'), ('mariadb', 'mariadb'), ('consul', 'consul'), ('php', 'php'), ('python', 'python')])
    submit = SubmitField('Submit')
