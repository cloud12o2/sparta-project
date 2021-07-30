# from pymongo import MongoClient
#
# client = MongoClient('mongodb://test:test@localhost', 27017)
# # client = MongoClient('localhost', 27017)
# db = client.collections


# # collections(영화제 수상작들) DB에서 가져오기
# def academy_men_db_find():
#     academy_men = db['academy_men']
#     academy_men_data = []
#
#     for rank in academy_men.find():
#         academy_men_data.append(rank)
#
#     return academy_men_data
#
# def jeonju_db_find():
#     jeonju = db['jeonju']
#     jeonju_data = []
#
#     for rank in jeonju.find():
#         jeonju_data.append(rank)
#
#     return jeonju_data
#
# def venice_film_db_find():
#     venice_film = db['venice_film']
#     venice_film_data = []
#
#     for rank in venice_film.find():
#         venice_film_data.append(rank)
#
#     return venice_film_data
#
#
# def academy_film_db_find():
#     academy_film = db['academy_film']
#     academy_film_data = []
#
#     for rank in academy_film.find():
#         academy_film_data.append(rank)
#
#     return academy_film_data
#
#
# def academy_women_db_find():
#     academy_women = db['academy_women']
#     academy_women_data = []
#
#     for rank in academy_women.find():
#         academy_women_data.append(rank)
#
#     return academy_women_data