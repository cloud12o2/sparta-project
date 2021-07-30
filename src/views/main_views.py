from flask import Blueprint, render_template

main_page = Blueprint('main', __name__, url_prefix='/')


# 아래와 같은 방식으로 웹페이지를 추가 할 수 있습니다.
# '/' 는 메인 혹은 index 페이지입니다.

@main_page.route('/')
def main():
    title = 'index page'
    return render_template(
        'index.html',
        title = title,
        )