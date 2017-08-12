# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class TblChat(models.Model):
    send_user = models.ForeignKey('TblUsers', models.DO_NOTHING, db_column='send_user', related_name='send_user')
    send_date = models.DateTimeField(default=timezone.now)
    receive_user = models.ForeignKey('TblUsers', models.DO_NOTHING, db_column='receive_user', related_name='receive_user')
    receive_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    message = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_chat'


class TblGeolocation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_geolocation'


class TblProduct(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    value = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    date = models.DateTimeField()
    category = models.ForeignKey('TblProductCategory', models.DO_NOTHING, db_column='category')

    class Meta:
        managed = False
        db_table = 'tbl_product'


class TblProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tbl_product_category'


class TblSharing(models.Model):
    send_user = models.ForeignKey('TblUsers', models.DO_NOTHING, db_column='send_user', related_name='send_user1')
    send_date = models.DateTimeField(default=timezone.now)
    receive_user = models.ForeignKey('TblUsers', models.DO_NOTHING, db_column='receive_user', related_name='receive_user1')
    receive_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey(TblProduct, models.DO_NOTHING, db_column='product')
    quantity = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_sharing'


class TblStorage(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.IntegerField()
    product = models.ForeignKey(TblProduct, models.DO_NOTHING, db_column='product')
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_storage'
        unique_together = (('id', 'user'),)


class TblUsers(models.Model):
    cpf = models.CharField(max_length=45)
    user = models.CharField(max_length=45)
    password = models.CharField(max_length=40)
    state = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    date = models.DateTimeField()
    email = models.CharField(max_length=45)
    distance = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_users'
