# -*- coding:utf-8 -*-
"""
@Time : 2022/4/27 5:29 PM
@Author: weaimy
@Des: schemas模型
"""
from datetime import datetime
from pydantic import Field, BaseModel
from typing import Optional, List
from schemas.base import BaseResp, ResAntTable


class CreateUser(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    password: str = Field(min_length=6, max_length=20)
    user_phone: Optional[str] = Field(regex="^1[34567890]\\d{9}$")
    user_status: Optional[bool]
    remarks: Optional[str]
    roles: Optional[List[int]]


class UpdateUser(BaseModel):
    id: int
    username: Optional[str] = Field(min_length=3, max_length=20)
    header_img: Optional[str]
    password: Optional[str] = Field(min_length=6, max_length=20)
    user_phone: Optional[str] = Field(regex="^1[34567890]\\d{9}$")
    user_status: Optional[bool]
    remarks: Optional[str]


class UpdateUserInfo(BaseModel):
    username: Optional[str] = Field(min_length=3, max_length=20)
    password: Optional[str] = Field(min_length=6, max_length=20)
    user_phone: Optional[str] = Field(regex="^1[34567890]\\d{9}$")
    user_status: Optional[bool]
    header_img: Optional[str]
    user_email: Optional[str]
    remarks: Optional[str]


class SetRole(BaseModel):
    user_id: int
    roles: Optional[str]


class AccountLogin(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    password: str = Field(min_length=6, max_length=20)


class UserInfo(BaseModel):
    username: str
    age: Optional[int]
    user_type: bool
    nickname: Optional[str]
    user_phone: Optional[str]
    user_email: Optional[str]
    full_name: Optional[str]
    scopes: Optional[List[str]]
    user_status: bool
    header_img: Optional[str]
    sex: int


class UserListItem(BaseModel):
    key: int
    id: int
    username: str
    age: Optional[int]
    user_type: bool
    nickname: Optional[str]
    user_phone: Optional[str]
    user_email: Optional[str]
    full_name: Optional[str]
    user_status: bool
    header_img: Optional[str]
    sex: int
    remarks: Optional[str]
    create_time: datetime
    update_time: datetime


class CurrentUser(BaseResp):
    data: UserInfo


class AccessToken(BaseModel):
    token: Optional[str]
    expires_in: Optional[int]


class UserLogin(BaseResp):
    data: AccessToken


class UserListData(ResAntTable):
    data: List[UserListItem]
