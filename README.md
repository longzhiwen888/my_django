#项目
0.在你要放置项目的目录执行  django-admin.py startproject mysite 创建项目
1.在开始项目时，先要更改settings.py中的  TIME_ZONE 为 'Asia/Shanghai'，
USE_TZ 为 False
2. django默认会启用auto-reloader，所以不想用的时候要加上--noreload，即：
python manage.py runserver 0.0.0.0:8000 --noreload

启动httpserver时会看到警告,"You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them."

这时候你应该终止进程，执行完python manage.py migrate后再启动
3. 创建超级管理员账户
python manage.py createsuperuser --username=username --email=xxxxxxx@qq.com