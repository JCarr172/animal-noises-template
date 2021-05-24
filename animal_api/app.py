from flask import Flask, request
import random

app = Flask(__name__)

# animal generator route here
@app.route('/get_animal', methods = ['GET'])
def animals():
    return random.choice(['cow','pig','horse'])


# animal noise generator route here
@app.route('/get_noise', methods = ['POST'])
def noises():
    noises = {'horse':'neigh','pig':'oink','cow':'moo','chicken':'cluck'}
    return noises[request.data.decode('utf-8')]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)