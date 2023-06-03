# -*- coding:utf-8 -*-
"""
@Time : 2022/5/18 1:03 AM
@Author: Donnie
@Des: 栏目管理
"""
from typing import List

from fastapi import APIRouter, Security, Query
from tortoise.queryset import F
from core.Auth import check_permissions
from core.Response import fail, success
from schemas import category, base
from models.base import Role, Category, CategoryType
from schemas.category import CreateCategory, UpdateCategory

router = APIRouter(prefix='/category')


@router.post("",
             summary="栏目添加",
             dependencies=[Security(check_permissions, scopes=["category_add"])]
             )
async def create_article(post: CreateCategory):
    """
    创建文章
    :param post: CreateArticle
    :return:
    """
    result = await Category.create(**post.dict())
    if not result:
        return fail(msg="创建失败!")
    return success(msg="创建成功!")


@router.get("",
            summary="栏目列表",
            dependencies=[Security(check_permissions, scopes=["category_query"])]
            )
async def category_list():
    """
    获取所有栏目
    :return:
    """
    result = await Category.annotate().order_by('-sort').all() \
        .values("id", "title", "parent_id", "type", "url", "sort", "status", "create_time", "update_time")
    # 总数
    total = len(result)
    tree_data = category_tree(result, 0)

    return success(msg="提取成功", data={"rows": tree_data})


@router.get("/tree/select",
            summary="栏目树形选择列表",
            dependencies=[Security(check_permissions, scopes=["category_tree_select"])]
            )
async def category_tree_select():
    """
    获取所有栏目
    :return:
    """
    result = await Category.annotate().all() \
        .values("id", "title", "parent_id", "type", "url", "sort", "status", "create_time", "update_time")
    # 总数
    total = len(result)
    tree_data = category_tree(result, 0)

    return success(msg="提取成功", data={"options": [{"label": "顶级菜单", "value": 0, "children": tree_data}]})


@router.put("", summary="角色修改", dependencies=[Security(check_permissions, scopes=["category_update"])])
async def update_role(post: UpdateCategory):
    """
    更新角色
    :param post:
    :return:
    """
    data = post.dict()
    data.pop("id")
    result = await Category.filter(pk=post.id).update(**data)
    if not result:
        return fail(msg="更新失败!")
    return success(msg="更新成功!")


def category_tree(data, pid):
    """
    遍历栏目树
    :param data: rule[]
    :param pid: 父ID
    :return: list
    """
    result = []
    for item in data:
        item["type_name"] = CategoryType(item["type"]).name
        item["label"] = str(item["title"])
        item["value"] = str(item["id"])
        if pid == item["parent_id"]:
            temp = category_tree(data, item["id"])
            if len(temp) > 0:
                item["children"] = temp
            result.append(item)
    return result