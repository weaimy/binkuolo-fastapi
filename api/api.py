# -*- coding:utf-8 -*-
"""
@Created on : 2022/4/22 22:02
@Author: weaimy
@Des: api路由
"""
from fastapi import APIRouter
from api.endpoints.test import test_oath2
from api.endpoints import user, role, access, websocket, upload, category, pages, article, content, job, service

api_router = APIRouter(prefix="/api/v1")
api_router.post("/test/oath2", tags=["测试oath2授权"])(test_oath2)
api_router.include_router(user.router, prefix='/admin', tags=["用户管理"])
api_router.include_router(role.router, prefix='/admin', tags=["角色管理"])
api_router.include_router(access.router, prefix='/admin', tags=["权限管理"])
api_router.include_router(upload.router, prefix='/admin', tags=["文件管理"])
api_router.include_router(websocket.router, prefix='/ws', tags=["WebSocket"])
api_router.include_router(category.router, prefix='/admin', tags=["栏目管理"])
api_router.include_router(pages.router, prefix='/admin', tags=["页面管理"])
api_router.include_router(article.router, prefix='/admin', tags=["文章管理"])
api_router.include_router(content.router, prefix='/admin', tags=["内容管理"])
api_router.include_router(job.router, prefix='/admin', tags=["招聘管理"])
api_router.include_router(service.router, prefix='/admin', tags=["表单项管理"])

