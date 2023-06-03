# -*- coding:utf-8 -*-
"""
@Time : 2023/5/16 22:53 PM
@Author: weaimy
@Des: 招聘管理
"""
from enum import Enum
from tortoise import fields
from tortoise.query_utils import Prefetch

import models
from core.Response import success, fail, res_antd
from models.base import WorkNature, WorkEducation, WorkMoney, WorkAge, WorkNum, Status, Job
from schemas import job
from core.Auth import create_access_token, check_permissions
from fastapi import Request, Query, APIRouter, Security
from config import settings
from typing import List

router = APIRouter(prefix='/service')


@router.get("/schema", dependencies=[Security(check_permissions)], summary="获取表单项")
async def get_schema(model_name: str, schema_type: str):
    model = globals()[model_name]
    body = []
    data = {}
    for k, v in model._meta.fields_map.items():
        print(k, type(v))
        if not isinstance(v, fields.data.CharEnumFieldInstance):
            print(k, type(v))
        if isinstance(v, models.base.RichTextField):
            if v.amis_form_item_type:
                print(v.amis_form_item_type)
        # if isinstance(v, fields.IntField):
        #     print(k, fields.IntField.__dict__)
        if isinstance(v, fields.data.CharField):
            if v.default:
                value = v.default.value
                data[k] = value
            body.append({
                "type": "input-text",
                "name": k,
                "label": v.description,
            })
        if isinstance(v, fields.data.CharEnumFieldInstance):
            # print(v.default.value, v.description)
            value = v.default.value
            options = []
            for ik, iv in v.enum_type.__members__.items():
                # print(ik, iv.value)
                options.append({"label": iv.value, "value": iv.value})
            data[k] = value
            body.append({
                "type": "select",
                "name": k,
                "label": v.description,
                "options": options
            })
        # if isinstance(field, fields.ForeignKeyField):
        #     if value:
        #         value = value.id
        #     else:
        #         value = None
        # data[k] = v
    return success(data={"data": data, "body": body})
