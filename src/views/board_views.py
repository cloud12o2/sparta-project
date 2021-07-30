import math
import time
from flask import Blueprint, render_template, request, redirect, flash, url_for
from pymongo import MongoClient, DESCENDING, ReturnDocument

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.board

board_list_page = Blueprint('board_list', __name__, url_prefix='/boardlist', template_folder='templates')

def bulletin_board_db_find():
    bulletin_board = db['bulletin_board']
    bulletin_board_data = []

    for rank in bulletin_board.find():
        bulletin_board_data.append(rank)

    return bulletin_board_data

@board_list_page.route('/')
def board_list():
    title = 'WM 게시판'
    bulletin_board = db['bulletin_board']
    page = request.args.get('page', type=int, default=1)
    limit = 10

    datas = bulletin_board.find({}).sort("_id", DESCENDING).skip((page - 1) * limit).limit(limit)
    tot_count = bulletin_board.find({}).count()
    last_page_num = math.ceil(tot_count / limit)

    block_size = 5
    block_num = int((page - 1) / block_size)
    block_start = (block_size * block_num) + 1
    block_end = block_start + (block_size - 1)

    datas_count = datas.count()

    return render_template(
        'boardList.html',
        title=title,
        datas=datas,
        limit=limit,
        page=page,
        block_start=block_start,
        block_end=block_end,
        last_page_num=last_page_num,
        datas_count=datas_count
        )



@board_list_page.route('/texteditor', methods=["GET", "POST"])
def text_editor():
    title = 'WM 글쓰기'
    if request.method == "POST":
        cur_time = time.strftime("20%y.%m.%d_%H:%M")
        title = request.form.get("title")
        contents = request.form.get("contents")
        writer = request.form.get("writer")
        password = request.form.get("password")
        views = 0
        to_db = {"title": title,
                 "writer": writer,
                 "password": password,
                 "contents": contents,
                 "update_time": cur_time,
                 "views": views
                 }
        db.bulletin_board.insert_one(to_db)
        return redirect('/boardlist')
    else:
        return render_template("textEditor.html", title=title)



@board_list_page.route('/textcontent?page=<page>/modify', methods=["GET", "POST"])
def text_content_modify(page):
    title = 'WM 글수정'
    bulletin_board_db = db.bulletin_board.find()[int(page) - 1]
    db_id = bulletin_board_db['_id']
    if request.method == "GET":
        return render_template(
            "textModify.html",
            page=page,
            writer=bulletin_board_db['writer']
        )

    if request.method == "POST":
        title = request.form.get("title")
        contents = request.form.get("contents")
        password = request.form.get("password")

        if(bulletin_board_db['password'] == password):
            db.bulletin_board.update_one({"_id": db_id}, {
                    "$set": {
                        "title": title,
                        "password": password,
                        "contents": contents,
                    }
                })
            flash("게시글이 수정되었습니다.")
            return redirect(url_for('board_list.text_content', page=page))
        else:
            flash("비밀번호가 잘못 입력되었습니다.")
            return redirect(url_for('board_list.text_content', page=page))
    else:
        return render_template("textModify.html", title=title)


@board_list_page.route('/textcontent')
def text_content():
    title = 'WM 게시판 글'
    page = request.args.get('page', type=int, default=1)
    bulletin_board_db = db.bulletin_board.find()[page - 1]
    db_id = bulletin_board_db['_id']

    datas = db.bulletin_board.find_one_and_update(
        {'_id': db_id},
        {"$inc": {"views": 1}},
        return_document=ReturnDocument.AFTER
    )


    content_title = datas['title']
    content_writer = datas['writer']
    content_update_time = datas['update_time']
    content_main = datas['contents']
    content_views = datas['views']
    return render_template(
        'textContent.html',
        title=title,
        page=page,
        content_title=content_title,
        content_writer=content_writer,
        content_update_time=content_update_time,
        content_main=content_main,
        content_views=content_views
    )

@board_list_page.route('/textcontent?page=<page>/delete')
def text_content_delete(page):
    bulletin_board_db = db.bulletin_board.find()[int(page) - 1]
    db_id = bulletin_board_db['_id']
    db.bulletin_board.find_one_and_delete({'_id': db_id})

    return redirect('/boardlist')