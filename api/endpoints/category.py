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
from core.Utils import get_tree

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
    tree_data = get_tree(result, 0)

    return success(msg="提取成功", data={"rows": tree_data})