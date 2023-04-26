from flask import Flask, render_template, request, flash, session
from time import asctime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SECRET_KEY'] = "This is my secret key"
app.secret_key = "Secret key"
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///worklist.sqlite3"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class worklist(db.Model):
#     id = db.Column("id", db.Integer, primary_key = True)
#     work = db.Column(db.String(200), nullable=False)
#     description = db.Column(db.String(200), nullable=False)
#     writenTime = db.Column(db.String(100), nullable=False)

#     def __init__(self, work, description, writenTime):
#         self.work = work
#         self.description = description
#         self.writenTime = writenTime


#-------------Errors----------------
@app.errorhandler(404)  
def pageNotFound(e):
    return render_template('404Error.html'), 404

@app.errorhandler(500)
def serverError(e):
    return render_template('500Error.html'), 500


#----render web pages--------------
@app.route('/')
def index():
    return render_template('homePage.html')

@app.route('/', methods=['GET', 'POST'])
def homePage():
    userWork = None
    if request.method=='POST':
        userWork = request.form['userWork']
        userWorkDescription = request.form['workDescription']
        session['userWork'] = userWork
        session['userWorkDescription'] = userWorkDescription
        flash("Work is Added successfully")
        with open('listData.txt', 'a') as f:
            f.write(f"['{userWork}', '{userWorkDescription}']\n")

    return render_template('homePage.html', userKaWork=userWork, userWorkDescription=userWorkDescription, time=asctime())


@app.route('/list')
def workListPage():
    if "userWork" in session or 'userWorkDescription' in session:
        userWorkS = session['userWork']
        userWorkDescriptionS = session['userWorkDescription']

    return render_template('workList.html', userKaWork=userWorkS, userWorkKaDescription=userWorkDescriptionS, time=asctime())



if __name__ =="__main__":
    # db.create_all()
    app.run(debug=True)