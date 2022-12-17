# from router.schemas import LikeRequestSchema
from sqlalchemy.orm.session import Session
from db.models import DbLike
from .likes_feed import likes

def db_feed(db: Session):
    new_like_list = [DbLike(
        article_id=like["article_id"],
        user_id = like["user_id"]
    ) for like in likes]
    db.query(DbLike).delete()
    db.commit()
    db.add_all(new_like_list)
    db.commit()
    return db.query(DbLike).all()

