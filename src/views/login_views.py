from flask import Blueprint, render_template


login_page = Blueprint('login', __name__, url_prefix='/login')

@login_page.route('/')
def login():
    title = '로그인'

    return render_template(
        'login.html',
        title = title,
        )