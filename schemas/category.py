from datetime import datetime
from pydantic import Field, BaseModel, validator
from typing import Optional, List, Any
from schemas.base import BaseResp


class CreateCategory(BaseModel):
    title: Optional[str]
    parent_id: int
    type: int
    url: Optional[str]
    seo_key: Optional[str]
    seo_desc: Optional[str]
    sort: int
    status: Optional[str]


class UpdateCategory(BaseModel):
    id: int
    title: Optional[str]
    parent_id: int
    type: int
    url: Optional[str]
    seo_key: Optional[str]
    seo_desc: Optional[str]
    sort: int
    status: Optional[str]


class CategoryItem(BaseModel):
    id: int
    title: Optional[str]
    parent_id: int
    type: int
    url: Optional[str]
    seo_key: Optional[str]
    seo_desc: Optional[str]
    sort: int
    status: Optional[str]


class CategoryList(BaseResp):
    code: int = Field(description="状态码")
    data: List[CategoryItem]
