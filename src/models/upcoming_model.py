# from pymongo import MongoClient
#
#
# client = MongoClient('mongodb://test:test@localhost', 27017)
# # client = MongoClient('localhost',27017)
#
# upcoming = client.upcoming
#
#
# # 개봉예정영화 DB에서 가져오기
# def yes24_newly_db_find():
#     yes24_newly = upcoming['yes24_newly']
#     yes24_newly_data = []
#
#     for collection1 in yes24_newly.find():
#         yes24_newly_data.append(collection1)
#
#     return yes24_newly_data
#
# def daum_watcha_newly_db_find():
#     daum_watcha_newly = upcoming['daum_watcha_newly']
#     daum_watcha_newly_data = []
#
#     for collection1 in daum_watcha_newly.find():
#         daum_watcha_newly_data.append(collection1)
#
#     return daum_watcha_newly_data
#
# def netflix_newly_db_find():
#     netflix_newly = upcoming['daum_watcha_newly']
#     netflix_newly_data = []
#
#     for collection1 in netflix_newly.find():
#         netflix_newly_data.append(collection1)
#
#     return netflix_newly_data

