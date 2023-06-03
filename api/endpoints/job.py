# -*- coding:utf-8 -*-
"""
@Time : 2023/5/16 22:53 PM
@Author: weaimy
@Des: 招聘管理
"""
from tortoise.query_utils import Prefetch

from core.Response import success, fail, res_antd
from models.base import Job, Category
from schemas import job
from core.Auth import create_access_token, check_permissions
from fastapi import Request, Query, APIRouter, Security
from config import settings
from typing import List
from tortoise.queryset import F

router = APIRouter(prefix='/job')


@router.post("", summary="招聘添加", dependencies=[Security(check_permissions, scopes=["job_add"])])
async def job_add(post: job.CreateJob):
    """
    创建招聘
    :param post: CreateJob
    :return:
    """
    # 过滤招聘
    get_job = await Job.get_or_none(title=post.title)
    if get_job:
        return fail(msg=f"招聘名{post.title}已经存在!")

    # 创建招聘
    create_job = await Job.create(**post.dict())
    if not create_job:
        return fail(msg=f"招聘{post.title}创建失败!")
    return success(msg=f"招聘{create_job.title}创建成功")


@router.delete("", summary="招聘删除", dependencies=[Security(check_permissions, scopes=["job_delete"])])
async def job_del(req: Request, job_id: int):
    """
    删除招聘
    :param req:
    :param job_id: int
    :return:
    """
    delete_action = await Job.filter(pk=job_id).delete()
    if not delete_action:
        return fail(msg=f"招聘{job_id}删除失败!")
    return success(msg="删除成功")


@router.put("", summary="招聘修改", dependencies=[Security(check_permissions, scopes=["job_update"])])
async def job_update(post: job.UpdateJob):
    """
    更新招聘信息
    :param post:
    :return:
    """
    job_check = await Job.get_or_none(pk=post.id)
    # 超级管理员或不存在的招聘
    if not job or job_check.pk == 1:
        return fail(msg="招聘不存在")

    if job_check.title != post.title:
        check_job_title = await Job.get_or_none(title=post.title)
        if check_job_title:
            return fail(msg=f"招聘名{check_job_title.title}已存在")

    data = post.dict()
    data.pop("id")
    await Job.filter(pk=post.id).update(**data)
    return success(msg="更新成功!")


@router.get("",
            summary="招聘列表",
            # response_model=job.JobList,
            dependencies=[Security(check_permissions, scopes=["job_query"])]
            )
async def job_list(
        pageSize: int = 10,
        current: int = 1,
        title: str = Query(None),
        create_time: List[str] = Query(None)
):
    """
    获取所有管理员
    :return:
    """
    # 查询条件
    query = {}
    if title:
        query.setdefault('title', title)
    if create_time:
        query.setdefault('create_time__range', create_time)

    res = await Job.annotate(key=F("id")).filter(**query).order_by('-create_time').all().prefetch_related(
        Prefetch("category", queryset=Category.all())
    )
    data = res[pageSize * (current - 1):pageSize]
    # print(len(res))
    # print(type(data))
    data_list = []
    for item in data:
        job_item = {
            "id": item.id,
            "title": item.title,
            "work_address": item.work_address,
            "category_id": item.category_id,
            "category_title": item.category.title,
            "work_nature": item.work_nature,
            "work_education": item.work_education,
            "work_money": item.work_money,
            "work_age": item.work_age,
            "work_num": item.work_num,
            "update_time": item.update_time,
            "create_time": item.create_time,
            "content": item.content,
            "status": item.status,
        }
        data_list.append(job_item)

    # 总数
    total = len(data_list)
    # 查询
    data = data_list[pageSize * (current - 1):pageSize]

    return res_antd(code=True, data=data, total=total)
