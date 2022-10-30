
from sqlalchemy.orm import Session
import models,schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session):
    return db.query(models.User).all()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create(db: Session,user :schemas.User):
    user = models.User(name=user.name, email=user.username,password=user.password)
    db.add(user)
    db.commit()
    return True

def update(db: Session,user :schemas.User):
    db_user = get_user(db, user.id)
    db_user.name = user.name
    db.commit()
    return get_user(db, user.id)
