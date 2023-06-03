# -*- coding:utf-8 -*-
"""
@Time : 2022/4/23 8:33 PM
@Author: weaimy
@Des: views home
"""
from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


# @router.get("/admin", tags=["登录页面"], response_class=HTMLResponse)
# async def login(request: Request):
#     """
#     门户首页
#     :param request:
#     :return:
#     """
#     # return request.app.state.views.TemplateResponse("admin/login.html", {"request": request})
#     return templates.get_template("index.html").render({"request": request, "id": id})
#
#
# @router.get("/admin/index", tags=["后台首页"], response_class=HTMLResponse)
# async def login(request: Request):
#     """
#     门户首页
#     :param request:
#     :return:
#     """
#     return request.app.state.views.TemplateResponse("admin/index.html", {"request": request})