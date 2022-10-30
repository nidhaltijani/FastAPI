
from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from database import  SessionLocal,engine
import crud,models
app = FastAPI()
import schemas
models.Base.metadata.create_all(bind=engine) 

users = [
    {
  "username": "ala@gmail.com",
  "password": "ala123"
},
{
  "username": "nidha@gmail.com",
  "password": "nidha123"
},
{
  "username": "ahmed@gmail.com",
  "password": "ahmed123"
}
]
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()






@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/getall")
def read_root():
    return users


@app.get("/name")
def read_root(name : str):
    return {"name": name}

@app.get("/age/{age}")
def read_root(age : int):
    return {"age": age}


@app.post("/login")
def login(login :schemas.Login):
    usernames =[]
    for user in users :
        usernames.append(user['username'])
    if login.username not in usernames :
        return {"status" :404 ,'message':'not found'}
    else :
        for user in users :
            if login.username == user["username"] :
                if login.password == user["password"] :
                    return {"status" :200 ,'user':user}
                else :
                    return {"status" :401 ,'message':'password incorrect'}    
                break    



@app.put("/changepassword")
def login(newpwd :schemas.Changepwd):
    usernames =[]
    for user in users :
        usernames.append(user['username'])
    if newpwd.username not in usernames :
        return {"status" :404 ,'message':'not found'}
    else :
        for user in users :
            if newpwd.username == user["username"] :
                if newpwd.password == user["password"] :
                    user["password"] = newpwd.newpwd
                    return {"status" :200 ,'message':'success'}
                else :
                    return {"status" :401 ,'message':'password incorrect'}    
                break    


@app.delete("/delete")
def login(username:str):
    usernames =[]
    for user in users :
        usernames.append(user['username'])
    if username not in usernames :
        return {"status" :404 ,'message':'not found'}
    else :
        for i in range(len(users)) :
            if username == users[i]["username"] :
                users.pop(i)    
                break   
        return {"status" :200 ,'message':'success'}   

@app.get("/getall_db")
def read_root(db: Session = Depends(get_db)):
    return crud.get_users(db)      

@app.post("/create")
def read_root(user : schemas.User,db: Session = Depends(get_db)):
    return crud.create(db,user)     

@app.put("/update")
def read_root(user : schemas.User,db: Session = Depends(get_db)):
    return crud.update(db,user)     