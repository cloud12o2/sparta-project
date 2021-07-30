from flask import Blueprint, render_template
from pymongo import MongoClient

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
ranking_db = client.ranking

box_office = ranking_db['box_office']
watcha = ranking_db['watcha']
netflix = ranking_db['netflix']

ranking_page = Blueprint('ranking', __name__, url_prefix='/ranking')

@ranking_page.route('/')
def ranking():
    title = '영화 순위'

    return render_template(
        'ranking.html',
        title = title,
        box_office=list(box_office.find()),
        watcha=list(watcha.find()),
        netflix=list(netflix.find())
        )