from flask import Flask, jsonify, request
app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    text = request.get('text')
    return jsonify({'result' : "test output: " + text})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)