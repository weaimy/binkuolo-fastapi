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


class BaseJob(BaseModel):
    title: str
    content: str
    work_address: Optional[str]
    work_nature: Optional[str]
    work_education: Optional[str]
    work_money: Optional[str]
    work_age: Optional[str]
    work_num: Optional[str]
    category_id: int
    status: int


class CreateJob(BaseJob):
    pass


class UpdateJob(BaseJob):
    id: int


class JobItem(BaseJob):
    id: int
    key: int
    create_time: datetime
    update_time: datetime


class JobList(ResAntTable):
    data: List[JobItem]