# Generated by Django 5.0.6 on 2024-07-13 12:15

import ckeditor.fields
import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=200)),
                ("title_tag", models.CharField(default="title tag", max_length=255)),
                (
                    "header_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="header_images/"
                    ),
                ),
                ("text", ckeditor.fields.RichTextField(blank=True, null=True)),
                (
                    "created_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("published_date", models.DateTimeField(blank=True, null=True)),
                ("category", models.CharField(default="coding", max_length=200)),
                ("snippet", models.CharField(max_length=100)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "likes",
                    models.ManyToManyField(
                        related_name="blog_posts", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
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
                    "author",
                    models.CharField(
                        max_length=200, verbose_name=django.contrib.auth.models.User
                    ),
                ),
                ("text", ckeditor.fields.RichTextField(blank=True, null=True)),
                (
                    "created_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("approved_comment", models.BooleanField(default=False)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="blog.post",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
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
                    "email",
                    models.EmailField(default="username@gmail.com", max_length=50),
                ),
                ("first_name", models.CharField(default="FirstName", max_length=50)),
                ("last_name", models.CharField(default="Lastname", max_length=50)),
                ("bio", ckeditor.fields.RichTextField(blank=True, null=True)),
                (
                    "profile_pic",
                    models.ImageField(
                        blank=True, null=True, upload_to="images/profile/"
                    ),
                ),
                (
                    "website_url",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "facebook_url",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "twitter_url",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("insta_url", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "followers",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="following",
                        to="blog.profile",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        default="user",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
