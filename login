from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email



lass LoginForm(Form):
email = StringField('Email', validators=[Required(), Length(1, 64),
Email()])
password = PasswordField('Password', validators=[Required()])
remember_me = BooleanField('Keep me logged in')
submit = SubmitField('Log In')


<ul class="nav navbar-nav navbar-right">
{% if current_user.is_authenticated() %}
<li><a href="{{ url_for('auth.logout') }}">Sign Out</a></li>
{% else %}
<li><a href="{{ url_for('auth.login') }}">Sign In</a></li>
{% endif %}
</ul>

login form


from flask.ext.login import logout_user, login_required
@auth.route('/logout')
@login_required
def logout():
  logout_user()
  flash('You have been logged out.')
  return redirect(url_for('main.index'))





from
from
from
from
from
flask import render_template, redirect, request, url_for, flash
flask.ext.login import login_user
. import auth
..models import User
.forms import LoginForm
@auth.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user is not None and user.verify_password(form.password.data):
      login_user(user, form.remember_me.data)
      return redirect(request.args.get('next') or url_for('main.index'))
    flash('Invalid username or password.')
  return render_template('auth/login.html', form=form)