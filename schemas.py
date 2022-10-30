from pydantic import BaseModel

class Login(BaseModel) :
    username : str
    password:str

class Changepwd(BaseModel) :
    username : str
    password:str
    newpwd:str

class User(BaseModel) :
    id :int
    username : str
    password:str
    name :str