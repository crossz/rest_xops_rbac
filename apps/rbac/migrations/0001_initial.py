# Generated by Django 3.2.13 on 2022-04-12 15:59

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='菜单名')),
                ('icon', models.CharField(blank=True, max_length=50, null=True, verbose_name='图标')),
                ('path', models.CharField(blank=True, max_length=158, null=True, verbose_name='链接地址')),
                ('is_frame', models.BooleanField(default=False, verbose_name='外部菜单')),
                ('is_show', models.BooleanField(default=True, verbose_name='显示标记')),
                ('sort', models.IntegerField(blank=True, null=True, verbose_name='排序标记')),
                ('component', models.CharField(blank=True, max_length=200, null=True, verbose_name='组件')),
                ('pid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rbac.menu', verbose_name='父菜单')),
            ],
            options={
                'verbose_name': '菜单',
                'verbose_name_plural': '菜单',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='权限名')),
                ('method', models.CharField(blank=True, max_length=50, null=True, verbose_name='方法')),
                ('pid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rbac.permission', verbose_name='父权限')),
            ],
            options={
                'verbose_name': '权限',
                'verbose_name_plural': '权限',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='角色')),
                ('desc', models.CharField(blank=True, max_length=50, null=True, verbose_name='描述')),
                ('menus', models.ManyToManyField(blank=True, to='rbac.Menu', verbose_name='菜单')),
                ('permissions', models.ManyToManyField(blank=True, to='rbac.Permission', verbose_name='权限')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='名称')),
                ('type', models.CharField(choices=[('company', '公司'), ('department', '部门')], default='company', max_length=20, verbose_name='类型')),
                ('pid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rbac.organization', verbose_name='父类组织')),
            ],
            options={
                'verbose_name': '组织架构',
                'verbose_name_plural': '组织架构',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(default='', max_length=20, verbose_name='姓名')),
                ('mobile', models.CharField(default='', max_length=11, verbose_name='手机号码')),
                ('email', models.EmailField(max_length=50, verbose_name='邮箱')),
                ('image', models.ImageField(blank=True, default='image/default.png', null=True, upload_to='static/%Y/%m')),
                ('position', models.CharField(blank=True, max_length=50, null=True, verbose_name='职位')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rbac.organization', verbose_name='部门')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('roles', models.ManyToManyField(blank=True, to='rbac.Role', verbose_name='角色')),
                ('superior', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='上级主管')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'ordering': ['id'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
