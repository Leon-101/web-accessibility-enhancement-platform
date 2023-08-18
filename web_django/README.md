### 环境

在环境中

```bash
pip install django
pip install mysqlclient
```

或者

```bash
pip install -r requirements.txt
```

### 启动

1. 创建数据库，并根据情况修改`settings.py`中的`DATABASES`项

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'web_scripts',  # 数据库的名字
           'USER': 'root',
           'PASSWORD': '123456',
           'HOST': '127.0.0.1',
           'PORT': 3306,
       }
   }
   ```

2. 在`manage.py`所在的目录下，

   ``` bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

3. 访问`http://127.0.0.1:8000/makedata`初始化数据