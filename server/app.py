from flask import Flask, render_template
import requests

app = Flask(__name__)


# home route here
# must query the animal API for an animal and a noise – the noise should be based on the animal
@app.route('/')
@app.route('/home')
def home():
    animal = requests.get('http://animal_noises_api:5000/get_animal')
    noise = requests.post('http://animal_noises_api:5000/get_noise', data=animal.text) 
    return render_template('index.html', animal=animal.text, noise= noise.text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)