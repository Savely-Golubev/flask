from flask import Flask, render_template, url_for, redirect
from forms import LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'among us'

@app.route("/<title>")
@app.route("/index/<title>")
def index(title):
    return render_template('index.html', title=title)


@app.route("/training/<prof>")
def training(prof):
    return render_template(
        "trainings.html", title="Тренировка", prof=prof.lower())

@app.route("/list_prof/<list>")
def list_prof(list):
    return render_template(
        "list_prof.html", title="Список профессий", list=list)

@app.route("/answer")
@app.route("/auto_answer")
def answer():
    data = {
        "title": "Анкета",
        "surname": "Watny",
        "name": "Mark",
        "education": "выше среднего",
        "profession": "штурман марсохода",
        "sex": "male",
        "motivation": "Всегда мечтал застрять на Марсе!",
        "ready": True
    }
    return render_template("auto_answer.html", data=data)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect("/success")
    return render_template("login.html", form=form, title="Аварийный доступ")

@app.route("/distribution")
def distribution():
    crew = [
        "Риддли Скотт",
        "Эдни Уирр",
        "Марк Уотни",
        "Венката Капур",
        "Тэдди Сандерс",
        "Шон Бин",
    ]
    return render_template(
        "distribution.html", title="Размещение по каютам", crew=crew)

@app.route("/table/<gender>/<int:age>")
def table(gender, age):
    return render_template(
        "table.html", title="Оформление каюты", gender=gender, age=age)

@app.route("/galery", methods=["GET", "POST"])
def galery():
    form = FileForm()
    if form.validate_on_submit():
        form.filename.data.save(
            f"{os.getcwd()}/static/img/carousel/{form.filename.data.filename}")
    files = [f"/img/carousel/{file}"
             for file in os.listdir(f"{os.getcwd()}/static/img/carousel")]
    return render_template(
        "galery.html", title="Красная планета", form=form, files=files)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
