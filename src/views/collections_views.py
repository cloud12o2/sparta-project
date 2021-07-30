from flask import Blueprint, render_template
from pymongo import MongoClient

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.collections


# collections(영화제 수상작들) DB에서 가져오기
def academy_men_db_find():
    academy_men = db['academy_men']
    academy_men_data = []

    for rank in list(academy_men.find({})):
        academy_men_data.append(rank)

    return academy_men_data

def jeonju_db_find():
    jeonju = db['jeonju']
    jeonju_data = []

    for rank in jeonju.find():
        jeonju_data.append(rank)

    return jeonju_data

def venice_film_db_find():
    venice_film = db['venice_film']
    venice_film_data = []

    for rank in list(venice_film.find({})):
        venice_film_data.append(rank)

    return venice_film_data


def academy_film_db_find():
    academy_film = db['academy_film']
    academy_film_data = []

    for rank in list(academy_film.find({})):
        academy_film_data.append(rank)

    return academy_film_data


def academy_women_db_find():
    academy_women = db['academy_women']
    academy_women_data = []

    for rank in list(academy_women.find({})):
        academy_women_data.append(rank)

    return academy_women_data

collection_page = Blueprint('collection', __name__, url_prefix='/ranking')

@collection_page.route('/academy-men')
def academy_men():
    title = '아카데미 남우주연상'
    main_content_title = '아카데미 남우주연상'
   
    return render_template(
        'collections.html',
        title=title,
        main_content_title=main_content_title,
        collection=academy_men_db_find()
        )


@collection_page.route('/jeonju')
def jeonju():
    title = '전주국제영화제 수상작'
    main_content_title = '전주국제영화제 수상작'

    return render_template(
        'collections.html',
        title=title,
        main_content_title=main_content_title,
        collection=jeonju_db_find()
        )

@collection_page.route('/venice-film')
def venice_film():
    title = '베니스영화제 황금사자상 수상작'
    main_content_title = '베니스영화제 황금사자상 수상작'

    return render_template(
        'collections.html',
        title=title,
        main_content_title=main_content_title,
        collection=venice_film_db_find()
        )

@collection_page.route('/academy-film')
def academy_film():
    title = '아카데미 촬영상 수상작'
    main_content_title = '아카데미 촬영상 수상작'

    return render_template(
        'collections.html',
        title=title,
        main_content_title=main_content_title,
        collection=academy_film_db_find()
        )

@collection_page.route('/academy-women')
def academy_women():
    title = '아카데미 여우조연상 수상작'
    main_content_title = '아카데미 여우조연상 수상작'

    return render_template(
        'collections.html',
        title = title,
        main_content_title=main_content_title,
        collection=academy_women_db_find()
        )