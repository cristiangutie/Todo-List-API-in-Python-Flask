import flask
import json
from flask import Flask
from flask import request
app = Flask(__name__)

todos = [
  { "label": "My first task", "done": False },
  { "label": "My second task", "done": False }
  ]

@app.route('/todos', methods=['GET'])
def get_todos():
  return flask.jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    return flask.jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    return flask.jsonify(todos)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
