# -*- coding:utf-8 -*-
"""
@Time : 2023/5/16 22:51 PM
@Author: weaimy
@Des: role schemas
"""
from pydantic import BaseModel, Field
from typing import List, Optional
from schemas.base import ResAntTable
from datetime import datetime


class BaseArticle(BaseModel):
    title: str
    content: str
    img: Optional[str]
    seo_key: Optional[str]
    seo_desc: Optional[str]
    category_id: int
    tags: Optional[str]
    source: Optional[str]


class CreateArticle(BaseArticle):
    pass


class UpdateArticle(BaseArticle):
    id: int


class ArticleItem(BaseArticle):
    id: int
    key: int
    create_time: datetime
    update_time: datetime


class ArticleList(ResAntTable):
    data: List[ArticleItem]