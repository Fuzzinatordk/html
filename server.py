import json

from flask import Flask, request, jsonify

todos = [
    {"name": "Fix out-of-memory bug", "done": True},
    {"name": "Calibrate coffee intake", "done": False},
]

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    with open("index.html") as f:
        return f.read()


@app.route("/todos", methods=["GET"])
def todos_get():
    return json.dumps(todos)


@app.route("/todos", methods=["POST"])
def todos_post():
    foo = request.json
    todos.append(foo)
    return ""
@app.route("/todos",methods=["DELETE"])
def todos_delete():
    data = request.get_json()
    del_name = data.get("name") if data else None
    todo_to_delete = next((todo for todo in todos if todo["name"] == del_name),None)
    if todo_to_delete:
        todos.remove(todo_to_delete)
        return jsonify(success=True)
    return jsonify(succes=False)

    
if __name__ == "__main__":
    app.run(debug=True)
