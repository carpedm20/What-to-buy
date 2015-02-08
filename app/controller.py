from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

from app import db
from app.mod_auth.models import *

buy_print = Blueprint('auth', __name__, url_prefix='/carpedm20/buy')

# Set the route and accepted methods
@buy_print.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("index.html")

