from flask import Flask , render_template , request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///storage.db"



app.app_context()
db =SQLAlchemy(app)

class db_model(db.Model):
    sno =db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(500),nullable = False)
    date_of_task =db.Column(db.DateTime, default =datetime.utcnow)


    def __repr__(self) -> str:
        return "{self.sno}-{self.title}"


@app.route('/',methods =['GET','POST'])

def hello_world():
    if request.method =="POST":
        title= request.form['title']
        desc=request.form['desc']
        print("The title = {}".format(title))
        print("The Descrpton = {}".format(desc))
        task =db_model(title = title, desc=desc)
        db.session.add(task)
        db.session.commit()
    
    


    
    
    
  

    return render_template('index.html')


@app.route('/about')
def about():
    return 'This is a about page'



if __name__ =="__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)