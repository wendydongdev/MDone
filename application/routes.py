from application import app, db, api
from flask import render_template, request, json, jsonify, Response, redirect, flash, url_for, session
from application.models import User, Course, Enrollment,Task
from application.forms import LoginForm, RegisterForm,ADDNewTaskForm
from flask_restx import Resource,fields
from application.task_list import task_list
from random import *


#######################################

@api.route('/api', '/api/')
class GetAndPost(Resource):

    def get(self):
        return jsonify(User.objects.all())

    #post
    # def post(self):
    #     data = api.payload
    #     user = User(user_id=data['user_id'], email=data['email'], first_name=data['first_name'],
    #                 last_name=data['last_name'])
    #     user.set_password(data['password'])
    #     user.save()
    #     return jsonify(User.objects(user_id=data['user_id']))


@api.route('/api/<idx>')
class GetUpdateDelete(Resource):

    # GET ONE
    def get(self, idx):
        return jsonify(User.objects(user_id=idx))

    # PUT
    # def put(self, idx):
    #     data = api.payload
    #     User.objects(user_id=idx).update(**data)
    #     return jsonify(User.objects(user_id=idx))

    # DELETE
    # def delete(self, idx):
    #     User.objects(user_id=idx).delete()
    #     return jsonify("User is deleted!")

    #######################################

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index=True)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if session.get('username'):
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.objects(email=email).first()
        if user and user.get_password(password):
            flash(f"{user.first_name}, you are successfully logged in!", "success")
            session['user_id'] = user.user_id
            session['username'] = user.first_name
            return redirect("/index")
        else:
            flash("Sorry, something went wrong.", "danger")
    return render_template("login.html", title="Login", form=form, login=True)


@app.route("/logout")
def logout():
    session['user_id'] = False
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route("/tasks/")
# @app.route("/tasks/<phase>")
def tasks(phase=None):
    task = Task.objects.order_by("-deadline")
    return render_template("tasks.html", taskData=task, tasks=True)


@app.route("/register", methods=['POST', 'GET'])
def register():
    if session.get('username'):
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user_id = User.objects.count()
        user_id += 1

        email = form.email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        position = form.position.data

        user = User(user_id=user_id, email=email, first_name=first_name, last_name=last_name, position=position)
        user.set_password(password)
        user.save()
        flash("You are successfully registered!", "success")
        return redirect(url_for('index'))
    return render_template("register.html", title="Register", form=form, register=True)

@app.route("/task-detail", methods=['POST', 'GET'])
def settask():
    if not session.get('username'):
        return redirect(url_for('index'))
    form = ADDNewTaskForm()
    if form.validate_on_submit():
        taskID = int(randint(1, 1000))
        title = form.title.data
        description = form.description.data
        phase = form.phase.data
        deadline = form.deadline.data

        task = Task(taskID=taskID, title=title, description=description, phase=phase, deadline=deadline)
        task.save()
        flash("You are successfully settle!", "success")
        return redirect(url_for('index'))
    return render_template("task_detail.html", title="Task Detail", form=form, register=True)

@app.route("/enrollment", methods=["GET", "POST"])
def enrollment():
    if not session.get('username'):
        return redirect(url_for('login'))

    taskID = request.form.get('taskID')
    title = request.form.get('title')
    user_id = session.get('user_id')

    if taskID:
        if Enrollment.objects(user_id=user_id, taskID=taskID):
            flash(f"Oops! You are already registered in this task {title}!", "danger")
            return redirect(url_for("tasks"))
        else:
            Enrollment(user_id=user_id, taskID=taskID).save()
            flash(f"You are enrolled in {title}!", "success")

    joinedTasks = task_list(user_id)

    return render_template("enrollment.html", enrollment=True, title="Enrollment", tasks=joinedTasks)


# @app.route("/api/")
# @app.route("/api/<idx>")
# def api(idx=None):
#     if (idx == None):
#         jdata = courseData
#     else:
#         jdata = courseData[int(idx)]
#
#     return Response(json.dumps(jdata), mimetype="application/json")


@app.route("/user")
def user():
    # User(user_id=1, first_name="Christian", last_name="Hur", email="christian@uta.com", password="abc1234").save()
    # User(user_id=2, first_name="Mary", last_name="Jane", email="mary.jane@uta.com", password="password123").save()
    users = User.objects.all()
    return render_template("user.html", users=users)

@app.route("/test")
def test():
    return render_template("test.html")