from flask import Blueprint, render_template
from pymongo import MongoClient

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost',27017)
upcoming_db = client.upcoming

daum_watcha = upcoming_db['daum_watcha']
netflix = upcoming_db['netflix']
yes24 = upcoming_db['yes24']

upcoming_page = Blueprint('upcoming', __name__, url_prefix='/')

@upcoming_page.route('/upcoming')
def upcoming():
    title = ' 개봉예정영화'

    return render_template(
        'upcoming.html',
        title=title,
        yes24=list(yes24.find({})),
        daum_watcha=list(daum_watcha.find({})),
        netflix=list(netflix.find({})),
        )