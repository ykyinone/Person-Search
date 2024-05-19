# Generated by Django 4.2.11 on 2024-05-11 08:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import searchapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Admin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=32, verbose_name="用户名")),
                ("password", models.CharField(max_length=64, verbose_name="密码")),
                (
                    "role",
                    models.SmallIntegerField(
                        choices=[(1, "用户"), (2, "管理员")], default=1, verbose_name="角色"
                    ),
                ),
                ("name", models.CharField(max_length=16, verbose_name="姓名")),
                ("age", models.IntegerField(verbose_name="年龄")),
                (
                    "gender",
                    models.SmallIntegerField(
                        choices=[(1, "男"), (2, "女")], verbose_name="性别"
                    ),
                ),
                ("mobile", models.CharField(max_length=32, verbose_name="手机号")),
                (
                    "create_time",
                    models.DateField(
                        default=django.utils.timezone.now, verbose_name="创建时间"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PersonSet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "img",
                    models.FileField(
                        max_length=128, upload_to="original_imgs/", verbose_name="行人图片"
                    ),
                ),
                (
                    "img_result",
                    models.JSONField(
                        default=searchapp.models.default_img_result, verbose_name="识别结果"
                    ),
                ),
                ("img_name", models.CharField(max_length=128, verbose_name="图片名称")),
                (
                    "processed_img",
                    models.FileField(
                        max_length=128,
                        null=True,
                        upload_to="processed_imgs/",
                        verbose_name="检测图片",
                    ),
                ),
                (
                    "admin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="searchapp.admin",
                        verbose_name="用户",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BoxSet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "img",
                    models.FileField(
                        max_length=128, upload_to="boxes_imgs/", verbose_name="检测框"
                    ),
                ),
                (
                    "img_info",
                    models.CharField(default="", max_length=128, verbose_name="图片信息"),
                ),
                (
                    "feature",
                    models.FileField(
                        null=True, upload_to="npy_files/", verbose_name="特征向量"
                    ),
                ),
                (
                    "admin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="searchapp.admin",
                        verbose_name="用户",
                    ),
                ),
                (
                    "source_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="boxes",
                        to="searchapp.personset",
                        verbose_name="用户",
                    ),
                ),
            ],
        ),
    ]
