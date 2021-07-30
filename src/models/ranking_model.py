# from pymongo import MongoClient
#
#
# client = MongoClient('mongodb://test:test@localhost', 27017)
# # client = MongoClient('localhost', 27017)
#
# db = client.ranking
#
#
# # 영화 순위 DB에서 가져오기
# def box_office_db_find():
#     box_office = db['box_office']
#     box_office_data = []
#
#     for rank in box_office.find():
#         box_office_data.append(rank)
#
#     return box_office_data
#
# def watcha_db_find():
#     watcha = db['watcha']
#     watcha_data = []
#
#     for rank in watcha.find():
#         watcha_data.append(rank)
#
#     return watcha_data
#
# def netflix_db_find():
#     netflix = db['netflix']
#     netflix_data = []
#
#     for rank in netflix.find():
#         netflix_data.append(rank)
#
#     return netflix_data