from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.user import User
from app.schemas.user import UserCreate


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user_in: UserCreate):
    existing_user = get_user_by_email(db, user_in.email)
    if existing_user:
        raise ValueError("User with this email already exists")

    user = User(
        email=user_in.email,
        password_hash=hash_password(user_in.password),
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user