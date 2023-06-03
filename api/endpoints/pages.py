# -*- coding:utf-8 -*-
"""
@Time : 2023/5/11 18:29 PM
@Author: weaimy
@Des: 栏目管理
"""
from typing import List

from fastapi import APIRouter, Security, Query, Request
from tortoise.queryset import F
from core.Auth import check_permissions
from core.Response import fail, success
from schemas import category, base
from models.base import Role, Category, CategoryType, Access

router = APIRouter(prefix='/pages')


@router.get("",
            summary="页面列表",
            dependencies=[Security(check_permissions)]
            )
async def page_list(req: Request):
    """
    获取所有栏目
    :return:
    """
    visible = True

    # 非超级管理员
    access = []
    if not req.state.user_type:
        visible = False

        # 二级菜单权限
        two_level_access = await Access.filter(role__user__id=req.state.user_id, is_check=True).values_list("parent_id")
        two_level_access = [i[0] for i in two_level_access]
        # 一级菜单权限
        one_level_access = await Access.filter(id__in=list(set(two_level_access))).values_list("parent_id")
        one_level_access = [i[0] for i in one_level_access]

        query_access = await Access.filter(id__in=list(set(one_level_access + two_level_access))).values_list("scopes")
        access = [i[0] for i in query_access]

    pages = [
        {"label": "Home", "url": "/", "redirect": "/index"},
        {
            "label": "系统管理",
            "children": [
                {
                    "label": "导航面板",
                    "url": "/index",
                    "schemaApi": "get:/admin/pages/console.json"
                },
                {
                    "label": "用户中心",
                    "url": "/user",
                    "rewrite": "/user/list",
                    "visible": visible if visible else "user" in access,
                    "children": [
                        {
                            "label": "用户管理",
                            "url": "/user/list",
                            "schemaApi": "get:/admin/pages/user.json",
                            "visible": visible if visible else "user_m" in access,
                        },
                        {
                            "label": "角色管理",
                            "url": "/role/list",
                            "schemaApi": "get:/admin/pages/role.json",
                            "visible": visible if visible else "role_m" in access,
                        }
                    ]
                }
            ]
        },
        {
            "label": "网站管理",
            "children": [
                {
                    "label": "栏目管理",
                    "url": "/category",
                    "schemaApi": "get:/admin/pages/category.json",
                    # "visible": "category" in access,
                },
                {
                    "label": "内容管理",
                    "url": "/article",
                    "rewrite": "/article/list",
                    "children": [
                        {
                            "label": "文章管理",
                            "url": "/article/list",
                            "schemaApi": "get:/admin/pages/article.json",
                        },
                        {
                            "label": "产品管理",
                            "url": "/product/list",
                            "schemaApi": "get:/admin/pages/product.json",
                        },
                        {
                            "label": "招聘管理",
                            "url": "/job/list",
                            "schemaApi": "get:/admin/pages/job.json",
                        },
                        {
                            "label": "单页管理",
                            "url": "/page/list",
                            "schemaApi": "get:/admin/pages/page.json",
                        }
                    ]
                },
            ],
            # "visible": "web" in access,
        }
    ]



    return success(msg="提取成功", data={"pages": pages, "access": access})


def page_tree(data, pid):
    """
    遍历栏目树
    :param data: rule[]
    :param pid: 父ID
    :return: list
    """
    result = []
    for item in data:
        if pid == item["parent_id"]:
            temp = page_tree(data, item["id"])
            if len(temp) > 0:
                item["children"] = temp
            result.append(item)
    return result