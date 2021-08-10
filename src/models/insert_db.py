from pymongo import MongoClient
from .crawling import ranking
from .crawling import collections
from .crawling import upcoming

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost',27017)

ranking_db = client.ranking
collections_db = client.collections
upcoming_db = client.upcoming


# DB에 영화 순위 insert
def ranking_db_insert():
    ranking_db.box_office.delete_many({})
    ranking_db.watcha.delete_many({})
    ranking_db.netflix.delete_many({})

    for movie in ranking.box_office():
        ranking_db.box_office.insert_one(movie)

    for movie in ranking.watcha():
        ranking_db.watcha.insert_one(movie)

    for movie in ranking.netflix():
        ranking_db.netflix.insert_one(movie)




# collections(영화제 수상작들) DB에 insert
def collections_db_insert():
    collections_db.academy_men.delete_many({})
    collections_db.jeonju.delete_many({})
    # collections_db.venice_film.delete_many({})
    collections_db.academy_film.delete_many({})
    collections_db.academy_women.delete_many({})

    #아카데미 남우주연상 수상작
    for movie in collections.academy_men():
        collections_db.academy_men.insert_one(movie)

    #전주국제영화제 수상작
    for movie in collections.jeonju():
        collections_db.jeonju.insert_one(movie)

    #베니스영화제 황금사자상 수상작
    # for movie in collections.venice_film():
    #     collections_db.insert_one(movie)

    #아카데미 촬영상 수상작
    for movie in collections.academy_film():
        collections_db.academy_film.insert_one(movie)

    #아카데미 여우조연상 수상작
    for movie in collections.academy_women():
        collections_db.academy_women.insert_one(movie)




# 개봉예정영화 DB에 insert
def upcoming_db_insert():
    upcoming_db.daum_watcha.delete_many({})
    upcoming_db.netflix.delete_many({})
    upcoming_db.yes24.delete_many({})


    for movie in upcoming.netflix():
        upcoming_db.netflix.insert_one(movie)

    for movie in upcoming.daum_watcha():
        upcoming_db.daum_watcha.insert_one(movie)

    for movie in upcoming.yes24():
        upcoming_db.yes24.insert_one(movie)