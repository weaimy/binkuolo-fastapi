# -*- coding:utf-8 -*-
"""
@Time : 2022/4/24 10:40 AM
@Author: weaimy
@Des: 基础模型
"""
from enum import IntEnum, Enum
from typing import Any

from tortoise import fields
from tortoise.models import Model


class TimestampMixin(Model):
    create_time = fields.DatetimeField(auto_now_add=True, description='创建时间')
    update_time = fields.DatetimeField(auto_now=True, description="更新时间")

    class Meta:
        abstract = True


class User(TimestampMixin):
    role: fields.ManyToManyRelation["Role"] = \
        fields.ManyToManyField("base.Role", related_name="user", on_delete=fields.CASCADE)
    username = fields.CharField(null=True, max_length=20, description="用户名")
    user_type = fields.BooleanField(default=False, description="用户类型 True:超级管理员 False:普通管理员")
    password = fields.CharField(null=True, max_length=255)
    nickname = fields.CharField(default='weaimy', max_length=255, description='昵称')
    user_phone = fields.CharField(null=True, description="手机号", max_length=11)
    user_email = fields.CharField(null=True, description='邮箱', max_length=255)
    full_name = fields.CharField(null=True, description='姓名', max_length=255)
    user_status = fields.IntField(default=0, description='0未激活 1正常 2禁用')
    header_img = fields.CharField(null=True, max_length=255, description='头像')
    sex = fields.IntField(default=0, null=True, description='0未知 1男 2女')
    remarks = fields.CharField(null=True, max_length=30, description="备注")
    client_host = fields.CharField(null=True, max_length=19, description="访问IP")

    class Meta:
        table_description = "用户表"
        table = "user"


class Role(TimestampMixin):
    user: fields.ManyToManyRelation[User]
    role_name = fields.CharField(max_length=15, description="角色名称")
    access: fields.ManyToManyRelation["Access"] = \
        fields.ManyToManyField("base.Access", related_name="role", on_delete=fields.CASCADE)
    role_status = fields.BooleanField(default=False, description="True:启用 False:禁用")
    role_desc = fields.CharField(null=True, max_length=255, description='角色描述')

    class Meta:
        table_description = "角色表"
        table = "role"


class Access(TimestampMixin):
    role: fields.ManyToManyRelation[Role]
    access_name = fields.CharField(max_length=15, description="权限名称")
    parent_id = fields.IntField(default=0, description='父id')
    scopes = fields.CharField(unique=True, max_length=255, description='权限范围标识')
    access_desc = fields.CharField(null=True, max_length=255, description='权限描述')
    menu_icon = fields.CharField(null=True, max_length=255, description='菜单图标')
    is_check = fields.BooleanField(default=False, description='是否验证权限 True为验证 False不验证')
    is_menu = fields.BooleanField(default=False, description='是否为菜单 True菜单 False不是菜单')

    class Meta:
        table_description = "权限表"
        table = "access"


class AccessLog(TimestampMixin):
    user_id = fields.IntField(description="用户ID")
    target_url = fields.CharField(null=True, description="访问的url", max_length=255)
    user_agent = fields.CharField(null=True, description="访问UA", max_length=255)
    request_params = fields.JSONField(null=True, description="请求参数get|post")
    ip = fields.CharField(null=True, max_length=32, description="访问IP")
    note = fields.CharField(null=True, max_length=255, description="备注")

    class Meta:
        table_description = "用户操作记录表"
        table = "access_log"


class CategoryType(IntEnum):
    news = 1
    product = 2
    job = 3
    page = 4
    link = 5


class Category(TimestampMixin):
    title = fields.CharField(null=True, max_length=255, description="网站名称")
    parent_id = fields.IntField(default=0, description='父id')
    type = fields.IntEnumField(CategoryType, default=CategoryType.news, description="栏目类型")
    url = fields.TextField(null=True, description='链接地址')
    seo_key = fields.CharField(null=True, max_length=255, description='关键词')
    seo_desc = fields.CharField(null=True, max_length=255, description='描述')
    status = fields.BooleanField(default=True, description="状态")
    sort = fields.IntField(default=0, description="排序")
    # 类型提示，仅用于Code 联想字段 匹配 下方关联的related_name
    articles: fields.ReverseRelation["Article"]

    class Meta:
        table_description = "栏目表"
        table = "weaimy_category"


class Article(TimestampMixin):
    title = fields.CharField(null=True, max_length=255, description="标题")
    content = fields.TextField(null=True, description='正文内容')
    img = fields.TextField(null=True, description='缩略图')
    seo_key = fields.CharField(null=True, max_length=255, description='关键词')
    seo_desc = fields.CharField(null=True, max_length=255, description='描述')
    tags = fields.CharField(null=True, max_length=255, description='标签')
    source = fields.CharField(null=True, max_length=255, description="来源")
    category: fields.ForeignKeyRelation[Category] = fields.ForeignKeyField("base.Category",
                                                                           related_name='articles',
                                                                           description="所属栏目")

    class Meta:
        table_description = "文章表"
        table = "weaimy_article"


class Product(TimestampMixin):
    title = fields.CharField(null=True, max_length=255, description="标题")
    content = fields.TextField(null=True, description='正文内容')
    img = fields.TextField(null=True, description='缩略图')
    seo_key = fields.CharField(null=True, max_length=255, description='关键词')
    seo_desc = fields.CharField(null=True, max_length=255, description='描述')
    tags = fields.CharField(null=True, max_length=255, description='标签')
    source = fields.CharField(null=True, max_length=255, description="来源")
    category: fields.ForeignKeyRelation[Category] = fields.ForeignKeyField("base.Category",
                                                                           related_name='products',
                                                                           description="所属栏目")

    class Meta:
        table_description = "产品表"
        table = "weaimy_product"


class WorkNature(str, Enum):
    FULL = "全职"
    PART = "兼职"


class WorkEducation(str, Enum):
    UNLIMITED = "不限"
    HIGH_SCHOOL = "高中及以上"
    JUNIOR_COLLEGE = "大专及以上"
    UNDERGRADUATE = "本科及以上"


class WorkMoney(str, Enum):
    UNLIMITED = "面议"
    TWO_THOUSAND = "2000-3000元/月"
    THREE_THOUSAND = "3000-5000元/月"
    FIVE_THOUSAND = "5000-8000元/月"
    EIGHT_THOUSAND = "8000-10000元/月"
    TEN_THOUSAND = "10000-20000元/月"
    TWENTY_THOUSAND = "20000-50000元/月"
    FIFTY_THOUSAND = "50000元以上/月"


class WorkAge(str, Enum):
    UNLIMITED = "不限"
    ONE_YEAR = "1年以上"
    TWO_YEAR = "2年以上"
    THREE_YEAR = "3年以上"
    FOUR_YEAR = "4年以上"
    FIVE_YEAR = "5年以上"


class WorkNum(str, Enum):
    ONE_NUM = "1"
    TWO_NUM = "2"
    THREE_NUM = "3"
    FOUR_NUM = "4"
    FIVE_NUM = "5"
    SIX_NUM = "6"
    SEVEN_NUM = "7"
    EIGHT_NUM = "8"
    NINE_NUM = "9"
    TEN_NUM = "10"
    UNLIMITED = "若干"


class Status(IntEnum):
    NORMAL = 1
    HIDDEN = 0


class RichTextField(fields.TextField):
    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        self.amis_form_item_type = "input-rich-text"


class Job(TimestampMixin):
    title = fields.CharField(null=True, max_length=255, description="标题")
    content = RichTextField(null=True, description='工作内容')
    work_address = fields.CharField(null=True, max_length=255, description='工作地点')
    work_nature = fields.CharEnumField(WorkNature, default=WorkNature.FULL, description='工作性质')
    work_education = fields.CharEnumField(WorkEducation, default=WorkEducation.UNLIMITED, description='学历要求')
    work_money = fields.CharEnumField(WorkMoney, default=WorkMoney.UNLIMITED, description='薪资待遇')
    work_age = fields.CharEnumField(WorkAge, default=WorkAge.UNLIMITED, description='工作年限')
    work_num = fields.CharEnumField(WorkNum, default=WorkNum.UNLIMITED, description='招聘人数')
    category: fields.ForeignKeyRelation[Category] = fields.ForeignKeyField("base.Category",
                                                                           related_name='jobs',
                                                                           description="所属栏目")
    status = fields.IntEnumField(Status, default=Status.HIDDEN, description='状态')

    class Meta:
        table_description = "招聘表"
        table = "weaimy_job"


class Page(TimestampMixin):
    content = fields.TextField(null=True, description='正文内容')
    pic_list = fields.TextField(null=True, description='组图')
    category: fields.ForeignKeyRelation[Category] = fields.ForeignKeyField("base.Category",
                                                                           related_name='pages',
                                                                           description="所属栏目")

    class Meta:
        table_description = "招聘表"
        table = "weaimy_page"
