from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests
from os import getenv
from sqlalchemy import desc

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
db = SQLAlchemy(app)

class Animals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    noise = db.Column(db.String(50), nullable=False)

# home route here
# must query the animal API for an animal and a noise – the noise should be based on the animal
@app.route('/')
@app.route('/home')
def home():
    animal = requests.get('http://animal_noises_api:5000/get_animal')
    noise = requests.post('http://animal_noises_api:5000/get_noise', data=animal.text)

    all_animals=Animals.query.order_by(desc(Animals.id)).limit(5).all()
    db.session.add(
        Animals(
            type=animal.text,
            noise=noise.text
            )
    )
    db.session.commit()

    return render_template('index.html', animal=animal.text, noise= noise.text, all_animals=all_animals)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)