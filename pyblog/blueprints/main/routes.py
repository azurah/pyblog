from flask import render_template, url_for, flash, redirect, request, Blueprint
from pyblog.ext import auth
from pyblog.ext.database import db
from pyblog.models import User
from pyblog.blueprints.user.forms import RegistrationForm, LoginForm

main = Blueprint('main', __name__)


@main.route("/", methods=['GET'])
def index():
    registration_form = RegistrationForm()
    login_form = LoginForm()
    return render_template('index.html', title='Home',
                           registration_form=registration_form,
                           login_form=login_form)