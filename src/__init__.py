from flask import Flask

def create_app():
    from .views import index_views
    from .views import board_views
    from .views import ranking_views
    from .views import collections_views
    from .views import upcoming_views
    from .apiRouter import search_api

    app = Flask(__name__)


    from flaskext.markdown import Markdown

    # 마크다운 기능 등록
    Markdown(app, extensions=['nl2br', 'fenced_code'])

    # 웹페이지 블루프린트
    app.register_blueprint(index_views.index_page)
    app.register_blueprint(board_views.board_list_page)
    app.register_blueprint(upcoming_views.upcoming_page)
    app.register_blueprint(ranking_views.ranking_page)
    app.register_blueprint(collections_views.collection_page)

    # API 라우터
    app.register_blueprint(search_api.search_page)

    app.secret_key = 'some_secret'

    if __name__ == '__main__':
        app.run('0.0.0.0', port=5000, debug=True)

    return app
