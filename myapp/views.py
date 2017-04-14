# This is where the routes are defined. It may be # split into a package of its own
# (yourapp/views/) with related views grouped together into modules.
# Python decorators are functions that are used to transform other functions. When a
# decorated function is called, the decorator is called instead. The decorator can then take
# action, modify the arguments, halt execution or call the original function.

from flask import render_template
from flask_login import login_required, current_user


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dashboard')
@login_required
def account():
    return render_template("account.html")
