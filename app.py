from flask import Flask, render_template, request 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


ENV = 'dev'
if ENV == 'dev':
    app.Debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:4511@localhost/Acumeal'

else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ziilzoitskpeci:98542aa19defccb8869ec427bd9acbd712db5e72466ca308a2b045d9ff3ef278@ec2-18-235-97-230.compute-1.amazonaws.com:5432/d1h26qqjgr07qc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(200))
    last = db.Column(db.String(200))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(200))
    email = db.Column(db.String(200))

    def __init__(self, first, last, age, gender, email):
        self.first = first
        self.last = last
        self.age = age
        self.gender = gender
        self.email = email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        first = request.form['first']
        last = request.form['last']
        age = request.form['age']
        gender = request.form['gender']
        email = request.form['email']
        if first == '' or email == '' or age == '' or last == '':
            return render_template('index.html', message='Please enter required fields')

        if db.session.query(Feedback).filter(Feedback.email == email).count() == 0: # if email does not exist
            data = Feedback(first, last, age, gender, email) # add all the data to the database
            db.session.add(data)
            db.session.commit() # adds data to the database
            # send_mail(first, last, email)
            return render_template('success.html')
    return render_template('index.html', message='You have already been added to the waitlist')       

if __name__ == '__main__':
    
    app.run(debug=True)