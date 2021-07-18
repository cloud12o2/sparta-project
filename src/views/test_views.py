from flask import Blueprint, render_template

test_page = Blueprint('test', __name__, url_prefix='/')


## API 역할을 하는 부분
# @app.route('/review', methods=['POST'])
# def default_post():
#     sample_receive = request.form['sample_give']
#     print(sample_receive)
#     return jsonify({'msg': '이 요청은 POST!'})
#
#
# @app.route('/review', methods=['GET'])
# def default_get():
#     sample_receive = request.args.get('sample_give')
#     print(sample_receive)
#     return jsonify({'msg': '이 요청은 GET!'})



@test_page.route('/test')
def test():
    title = 'test page'
    a_variable = 'variable1'
    return render_template(
        'test.html',
        title = title,
        a_variable=a_variable
        )