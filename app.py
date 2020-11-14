from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Weight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    weight = db.Column(db.Integer)

    def __repr__(self):
        return '<Weight %r>' % self.id


class Water(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    water = db.Column(db.Integer)

    def __repr__(self):
        return '<Water %r>' % self.id


class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    activity = db.Column(db.Integer)

    def __repr__(self):
        return '<Activity %r>' % self.id


class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    repast_name = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(2000), nullable=False)
   
    def __repr__(self):
        return '<Meal %r>' % self.id


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        daily_weight = request.form['weight']
        new_weight = Weight(weight=daily_weight)

        db.session.add(new_weight)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('index.html')



# @app.route('/foods', methods=["POST"])
# def food():
    

if __name__ == "__main__":
    app.run(debug=True)
