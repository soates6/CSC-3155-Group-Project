from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .models import Base, User, engine, SessionLocal
from .schemas import UserCreate, UserResponse
from .utils import create_confirmation_token, send_confirmation_email, verify_confirmation_token

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    token = create_confirmation_token(new_user.email)
    send_confirmation_email(new_user.email, token)

    return UserResponse(email=new_user.email, confirmed=new_user.confirmed)

@app.get("/confirm/{token}")
def confirm_email(token: str, db: Session = Depends(get_db)):
    email = verify_confirmation_token(token)
    if email is None:
        raise HTTPException(status_code=400, detail="Invalid or expired token")

    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.confirmed = True
    db.commit()
    return {"message": "Email confirmed successfully!"}
