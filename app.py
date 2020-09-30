from flask import Flask,request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"


@app.route("/candidates",methods=['POST'])
def candidates():
    data = request.data
    print(data)
    return "candidates pushed"

if __name__ == '__main__':
    app.run(debug=True)