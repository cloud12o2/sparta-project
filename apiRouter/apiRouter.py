from flask import Flask, jsonify, request

app = Flask(__name__)


## API 역할을 하는 부분
@app.route('/review', methods=['POST'])
def default_post():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': '이 요청은 POST!'})


@app.route('/review', methods=['GET'])
def default_get():
    sample_receive = request.args.get('sample_give')
    print(sample_receive)
    return jsonify({'msg': '이 요청은 GET!'})
