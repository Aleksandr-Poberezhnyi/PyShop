from flask_sqlalchemy import SQLAlchemy
from flask import Flask,render_template,request
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///users.db'
db = SQLAlchemy(app)  # Database
 
class User(db.Model):  #magic tablichka Model = Table
    id = db.Column(db.Integer, primary_key=True) # primary key для связи с другими табличками корзины и пользователя
    username = db.Column(db.String(20), unique=True, nullable=False) #unique указать что имя уже существует или нет  
    password = db.Column(db.String(500), nullable=False) #nullable указать что имя не может быть пустым
    email = db.Column(db.String(40), unique=True, nullable=False) 
 
    def __repr__(self):
        return f"User('{self.username}', '{self.password}', '{self.email}')" # я лучше ентер нажимать не буду
 
# with app.app_context(): 
 
#     db.create_all()  # создаем все таблицы
#     db.session.add(User(username='admin', password='admin', email='kenaa@example.com')) # аналог подключения
#     users = User(username='hello', password='202a', email='world@example.com')
#     db.session.add(users)
#     db.session.commit()  # записываем в базу данных



@app.route("/users")
def index():
    users = User.query.all()
    print(users)
    return render_template("users.html", users = users)

@app.route("/reg",methods = ["GET","POST"])
def register():
    if request.method == "POST":
        print(request.form) 
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        db.session.add(User(username= username, password= password, email= email))
        db.session.commit()
        return "Вы успешно зарегистрировались"
    return render_template("register.html")


@app.route('/')
def main():
    return render_template("main.html", main = main)



app.run(debug=True)  # запуск сервера