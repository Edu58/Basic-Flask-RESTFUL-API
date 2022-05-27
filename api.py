from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


hello = {
    1:{'name': 'hello'},
    2:{'name': 'hi there'}
}


class Todos(Resource):
    def get(self):
        return hello
    
    def post(self):
        data = request.json
        itemId = len(hello.keys()) + 1
        hello[itemId] = {'name': data['name']}
        return hello
        
class ToDo(Resource):
    def get(self, todo_id):
        data = hello[todo_id]
        return data
    
    def put(self, todo_id):
        data = request.json
        hello[todo_id]['name'] = data['name']
        return hello
    
    def delete(self, todo_id):
        del hello[todo_id]
        return hello
        
api.add_resource(Todos, '/')
api.add_resource(ToDo, '/<int:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)