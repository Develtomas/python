import fastapi
import db
import pydantic_models
import config
from fastapi import Request

api = fastapi.FastAPI()

response = {"Response":"Server returned"}
fake_database = {'users':[
    {
        "id":1,             # тут тип данных - число
        "name":"Anna",      # тут строка
        "nick":"Anny42",    # и тут
        "balance": 15300
     },

    {
        "id":2,             # у второго пользователя 
        "name":"Dima",      # такие же 
        "nick":"dimon2319", # типы 
        "balance": 160.23     # данных
     },

    {
        "id":3,             # у третьего
        "name":"Vladimir",  # юзера
        "nick":"Vova777",   # мы специально сделаем 
        "balance": "25000"     # нестандартный тип данных в его балансе
     }
]}

@api.get('/')       # метод для обработки get запросов
@api.post('/')      # метод для обработки post запросов
@api.put('/')       # метод для обработки put запросов
@api.delete('/')    # метод для обработки delete запросов
def index(request: Request):  # тут request - будет объектом в котором хранится вся информация о запросе
    return {"Request" : [request.method,    # тут наш API вернет клиенту метод, с которым этот запрос был совершен
                         request.headers]}  # а тут в ответ вернутся все хедеры клиентского запроса

@api.get("/users/")
def get_users(skip: int = 0, limit: int = 10):
    return fake_database['users'][skip : skip + limit]

@api.get("/user/{user_id}")
def read_user(user_id: str, query: str | None = None):
    """
    Тут значение по умолчанию для query будет None
    """
    if query:
        return {"user_id": user_id, "query": query}
    return {"user_id": user_id}


@api.get('/get_info_by_user_id/{id:int}')
def get_info_about_user(id):
    return fake_database['users'][id-1]

@api.get('/get_user_balance_by_id/{id:int}')
def get_user_balance(id):
    return fake_database['users'][id-1]['balance']

@api.get('/get_total_balance')
def get_total_balance():
    total_balance: float = 0.0
    for user in fake_database['users']:
        total_balance += pydantic_models.User(**user).balance 
    return total_balance

@api.post('/user/create')
def user_create(user: pydantic_models.User):
    """
    Когда в пути нет никаких параметров
    и не используются никакие переменные,
    то fastapi, понимая, что у нас есть аргумент, который
    надо заполнить, начинает искать его в теле запроса,
    в данном случае он берет информацию, которую мы ему отправляем
    в теле запроса и сверяет её с моделью pydantic, если всё хорошо,
    то в аргумент user будет загружен наш объект, который мы отправим
    на сервер.
    """
    fake_database['users'].append(user)
    return {'User Created!': user}