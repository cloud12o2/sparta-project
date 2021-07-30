from flask import Blueprint, render_template
from pymongo import MongoClient


# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost',27017)

upcoming = client.upcoming


# 개봉예정영화 DB에서 가져오기
def yes24_newly_db_find():
    yes24_newly = upcoming['yes24_newly']
    yes24_newly_data = yes24_newly.find({})

    return yes24_newly_data

def daum_watcha_newly_db_find():
    daum_watcha_newly = upcoming['daum_watcha_newly']
    daum_watcha_newly_data = daum_watcha_newly.find({})

    return daum_watcha_newly_data

def netflix_newly_db_find():
    netflix_newly = upcoming['netflix_newly']
    netflix_newly_data = netflix_newly.find({})

    return netflix_newly_data



upcoming_page = Blueprint('upcoming', __name__, url_prefix='/')

@upcoming_page.route('/upcoming')
def upcoming():
    title = ' 개봉예정영화'

    return render_template(
        'upcoming.html',
        title = title,
        yes24_newly = yes24_newly_db_find(),
        daum_watcha_newly = daum_watcha_newly_db_find(),
        netflix_newly = netflix_newly_db_find()
        )