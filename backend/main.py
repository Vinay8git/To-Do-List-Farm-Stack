from fastapi import FastAPI, HTTPException, status, Query
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

@app.get('/api/v1/todos', status_code=status.HTTP_200_OK)
def getAllTodos(limit=Query(...), offset=Query(...)) -> List[dict]:
    return todos[offset:limit+offset]

@app.get('/api/v1/todos/title/{title}', status_code=status.HTTP_200_OK)
def getAllTodos(title: str) -> dict:
    for todo in todos:
        if todo['title'] == title:
            return todo
    raise HTTPException(status.HTTP_404_NOT_FOUND,
            f"Todo with title {title} not found")

@app.get('/api/v1/todos/status/{status}')
def getAllTodos(status: str) -> List:
    result=[]
    for todo in todos:
        if todo['status'] == status:
            result.append(todo)
    return result


# #Create Todo
# @app.post('/api/v1/todos')
# def createTodo(todo: dict) ->bool:
#     try:
#         todos.append(todo)
#         return True
#     except:
#         return False

# create a todo 
# enforcing title to be unique -> user defined constraint
# {"title": "wakeup","desc":"1" }
# {"title": "wakeup","desc":"2" }
@app.post('/api/v1/todos', status_code=status.HTTP_201_CREATED)
def create_todo(todo: dict) -> bool:
	if (getAllTodos(todo['title'])):
		
		message = f"todo with title {todo['title']} already exists."
		raise HTTPException(status.HTTP_400_BAD_REQUEST,message)
	todos.append(todo)
	print(todos)
	return True

@app.put('/api/v1/todos')
def update_todo(payload: dict) -> bool:
	update_idx = -1
	for idx,todo in enumerate(todos):
		if todo['title'] == payload['title']:
			update_idx = idx
			
	if update_idx == -1:
		raise HTTPException(status.HTTP_404_NOT_FOUND
										 ,f"todo with title {payload['title']} doesnt exist.")
	todos[update_idx]['status'] = payload['status']
	todos[update_idx]['desc'] = payload['desc']
	return True



@app.delete('/api/v1/todos/delete-by-title/{title}')
def delete_todo(title: str) -> bool:
	delete_idx = -1
	for idx,todo in enumerate(todos):
		if todo['title'] == title:
			delete_idx = idx
			
	if delete_idx == -1:
		raise HTTPException(status.HTTP_404_NOT_FOUND ,f"todo with title {title} doesnt exist.")
	# del todos[delete_idx]
	todos.pop(delete_idx)
	return True