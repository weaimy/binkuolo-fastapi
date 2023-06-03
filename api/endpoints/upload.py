# -*- coding:utf-8 -*-
"""
@Time : 2022/5/18 1:03 AM
@Author: weaimy
@Des: 权限管理
"""
from fastapi import APIRouter, Security, Request, File, UploadFile
from core.Auth import check_permissions
from core.Response import fail, success
from core.Utils import random_str
from config import settings
import os
import time

router = APIRouter(prefix='/upload')


@router.post("",
             dependencies=[Security(check_permissions, scopes=["upload_file"])],
             summary="文件上传")
async def file_upload(req: Request, file: UploadFile = File(...)):
    """
    头像上传
    :param req:
    :param file:
    :return:
    """
    # 文件存储路径
    path = f"{settings.STATIC_DIR}/upload"
    start = time.time()
    filename = random_str() + '.' + file.filename.split(".")[1]
    try:
        if not os.path.isdir(path):
            os.makedirs(path, 0o777)
        res = await file.read()
        with open(f"{path}/{filename}", "wb") as f:
            f.write(res)
        data = {
            'time': time.time() - start,
            'url': f"/upload/{filename}"}
        return success(msg="文件上传成功", data=data)
    except Exception as e:
        print("文件上传失败:", e)
        return fail(msg=f"{file.filename}上传失败!")
