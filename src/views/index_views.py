from flask import Blueprint, render_template

index_page = Blueprint('index', __name__, url_prefix='/')


@index_page.route('/')
def index():
    title = 'Which Movie'
    return render_template(
        'index.html',
        title = title,
        )