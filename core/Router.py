# -*- coding:utf-8 -*-
"""
@Time : 2022/4/23 11:43 AM
@Author: weaimy
@Des: 路由聚合
"""
from api.api import api_router
from fastapi import APIRouter


router = APIRouter()
# API路由
router.include_router(api_router)

