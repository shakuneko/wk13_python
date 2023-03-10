from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from router.schemas import ArticleRequestSchema, ArticleResponseSchema
from db.database import get_db
from db import db_artists
from typing import List

router = APIRouter(
    prefix='/api/articles',
    tags=['articles']
)


@router.post('', response_model=ArticleResponseSchema)
def create(request: ArticleRequestSchema, db: Session = Depends(get_db)):
    return db_artists.create(db, request)


@router.get('/feed', response_model=List[ArticleResponseSchema])
def feed_initial_articles(db: Session = Depends(get_db)):
    return db_artists.db_feed(db)


@router.get('/all', response_model=List[ArticleResponseSchema])
def get_all_articles(db: Session = Depends(get_db)):
    return db_artists.get_all(db)


@router.get("/id/{article_id}", response_model=ArticleResponseSchema)
def get_article_by_id(article_id: int, db: Session = Depends(get_db)):
    return db_artists.get_article_by_id(article_id, db)

@router.get("/{title}", response_model=List[ArticleResponseSchema])
def get_article_by_title(title: str, db: Session = Depends(get_db)):
    return db_artists.get_article_by_title(title, db)
