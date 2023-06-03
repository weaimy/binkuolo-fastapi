# -*- coding:utf-8 -*-
"""
@Time : 2022/5/5 1:30 AM
@Author: weaimy
@Des: 测试
"""
from core.Auth import create_access_token
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, status
from models.base import User
from core.Utils import check_password
from datetime import timedelta

async def test_oath2(data: OAuth2PasswordRequestForm = Depends()):

    user = await User.get_or_none(username=data.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"用户{data.username}密码验证失败!",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not user.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"用户{data.username}密码验证失败!",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not check_password(data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"用户{data.username}密码验证失败!",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not user.user_status:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"用户{data.username}已被管理员禁用!",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"user_id": user.id, "user_type": user.user_type})

    return {"access_token": access_token, "token_type": "bearer"}
