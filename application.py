from bottle import route, post, run, template, redirect, request
import database

# Initialize the database
database.initialize_database()

@route("/")
def get_index():
    redirect("/projects")

@route("/projects")
def get_projects():
    projects = database.get_all_projects()
    return template("/workspaces/Finalproject/templates", projects=projects)

@route("/projects/add")
def get_add_project():
    return template("/workspaces/Finalproject/add_project.tpl")

@post("/projects/add")
def post_add_project():
    title = request.forms.get("title")
    description = request.forms.get("description")
    member_id = request.forms.get("member_id")
    database.add_project(title, description, member_id)
    redirect("/projects")

@route("/projects/<project_id>")
def get_project_details(project_id):
    project = database.get_project_details(project_id)
    return template("project_details.tpl", project=project)

@route("/projects/<project_id>/update")
def get_update_project(project_id):
    project = database.get_project_details(project_id)
    return template("/workspaces/Finalproject/update_project.tpl", project=project)

@post("/projects/<project_id>/update")
def post_update_project(project_id):
    title = request.forms.get("title")
    description = request.forms.get("description")
    member_id = request.forms.get("member_id")
    database.update_project(project_id, title, description, member_id)
    redirect("/projects")

@route("/projects/<project_id>/delete")
def get_delete_project(project_id):
    database.delete_project(project_id)
    redirect("/projects")

run(host='localhost', port=8080)
