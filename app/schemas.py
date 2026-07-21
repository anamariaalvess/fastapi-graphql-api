from graphene_sqlalchemy import SQLAlchemyObjectType
from pydantic import BaseModel

from app import models
from app.models import Post


class PostSchema(BaseModel):
    title: str
    content: str


class PostModel(SQLAlchemyObjectType):
    class Meta:
        model = Post