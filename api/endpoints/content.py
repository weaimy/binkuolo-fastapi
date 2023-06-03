# -*- coding:utf-8 -*-
"""
@Time : 2022/5/18 1:03 AM
@Author: Weaimy
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

router = APIRouter(prefix='/content')


@router.get("/nav",
            summary="栏目列表",
            dependencies=[Security(check_permissions, scopes=["content_nav"])]
            )
async def category_list():
    """
    获取所有栏目
    :return:
    """
    result = await Category.annotate().order_by('-sort').all() \
        .values("id", "title", "parent_id", "type")
    # 总数
    total = len(result)
    tree_data = category_tree(result, 0)

    return success(msg="提取成功", data=tree_data)


@router.get("/initData",
            summary="栏目内容",
            # dependencies=[Security(check_permissions, scopes=["content_body"])]
            )
async def content_body(id:int):
    """
    获取所有栏目表单
    :return:
    """
    return success(msg="提取成功", data={"id": id})


def category_tree(data, pid):
    """
    遍历栏目树
    :param data: rule[]
    :param pid: 父ID
    :return: list
    """
    result = []
    for item in data:
        item["label"] = str(item["title"])
        item["to"] = "?id=" + str(item["id"])
        item["icon"] = ''
        if pid == item["parent_id"]:
            temp = category_tree(data, item["id"])
            if len(temp) > 0:
                item["children"] = temp
            result.append(item)
    return result

