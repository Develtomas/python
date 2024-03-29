import copy
from database import crud
import pydantic_models
import config
import fastapi

api = fastapi.FastAPI()


# GET
@api.get("/users")
@crud.db_session
def get_users():
    users = []
    for user in crud.User.select()[:]:
        users.append(user.to_dict())
    return users


@api.get('/get_info_by_user_id/{user_id:int}')
@crud.db_session
def get_info_about_user(user_id):
    return crud.get_user_info(crud.User[user_id])


@api.get('user_by_tg_id/{tg_id}')
@crud.db_session
def get_user_by_tg_id(tg_id: int = fastapi.Path()):
    return crud.get_user_by_tg_id(tg_id).to_dict()


@api.get('/get_user_balance_by_id/{user_id:int}')
@crud.db_session
def get_user_balance_by_id(user_id):
    crud.update_wallet_balance(crud.User[user_id].wallet)
    return crud.User[user_id].wallet.balance


@api.get('/get_total_balance')
@crud.db_session
def get_total_balance():
    balance = 0.0
    crud.update_all_wallets()
    for user in crud.User.select()[:]:
        balance += user.wallet.balance
    return balance


# POST
@api.post('/user/create')
# create user -> key is telegram
def create_user(user: pydantic_models.User_to_create = fastapi.Body()):
    return crud.create_user(tg_id=user.tg_ID, nick=user.nick if user.nick else None).to_dict()


@api.post('/create_transaction')
def create_transaction(transaction: pydantic_models.CreateTransaction = fastapi.Body()):
    user = crud.get_user_by_tg_id(transaction.tg_ID)
    return crud.create_transaction(
            sender=user,
            amount_btc_without_fee=transaction.amount_btc_without_fee,
            receiver_address=transaction.receiver_address,
            fee=transaction.fee if transaction.fee else None,
            testnet=transaction.testnet
    ).to_dict()


# PUT
@api.put('/user/{user_id}')
# change user and save
def update_user(user_id: int, user: pydantic_models.User_to_update = fastapi.Body()):
    return crud.update_user(user).to_dict()


# DELETE
@api.delete('/user/{user_id}')
@crud.db_session
def delete_user(user_id: int = fastapi.Path()):
    crud.get_user_by_id(user_id).delete()
    return True





