from fastapi import FastAPI
from typing import List
app=FastAPI()

todos = [{
          "title": "wakeup"
          ,"desc": "time to wakeup"
          , "status": "done"
         }
        , {
          "title": "class"
          ,"desc": "we have class on FSD now"
          ,"status": "in-progress"
          }]
@app.get('/')
def greet():
    return "Hello, World!"

@app.get('/greet/{name}')
def greetBYName(name : str):
    return f'hello{name}'

@app.get('/api/v1/todos')
def getAllTodos() -> List[dict]:
    return todos

@app.get('/api/v1/todos/title/{title}')
def getAllTodos(title: str) -> dict:
    for todo in todos:
        if todo['title'] == title:
            return todo
    return {}

@app.get('/api/v1/todos/status/{status}')
def getAllTodos(status: str) -> List:
    result=[]
    for todo in todos:
        if todo['status'] == status:
            result.append(todo)
    return result


#Create Todo
@app.post('/api/v1/todos')
def createTodo(todo: dict) ->bool:
    try:
        todos.append(todo)
        return True
    except:
        return False
