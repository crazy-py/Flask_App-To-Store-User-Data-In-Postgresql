from flask import Flask ,request, render_template
#from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
app=Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:aditya100@localhost/datascience'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://ljyivlroueunur:aa64c511630149e2cf4ad5363c53b86607e4e4ef2f785a02ec16fd3d4712fa11@ec2-50-19-95-77.compute-1.amazonaws.com:5432/d8cfv9q65n96id?sslmode=require'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id = db.Column(db.Integer, primary_key=True)
    email= db.Column(db.String, unique=True, nullable=False)
    height=db.Column(db.Integer, unique=False, nullable=False)
    weight=db.Column(db.Integer, unique=False,nullable=False)
    country=db.Column(db.String, unique=False,nullable=True)
    
    def __init__(self,email,height,weight,country):
        self.email=email
        self.height=height
        self.weight=weight
        self.country=country

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/submit/", methods=['POST'])
def redirect():
    if request.method=='POST':
        email=request.form["email_address"]
        height=request.form["height"]
        weight=request.form["weight"]
        country=request.form["country"]
        data=Data(email,height,weight,country)
        if db.session.query(Data).filter(Data.email==email).count()==0:
            #print(request.form)
            db.session.add(data)
            db.session.commit()
            return render_template("redirect.html")
    return render_template("index.html",text="User Data Already Exists")

if __name__ == "__main__":
    app.debug=True
    app.run()