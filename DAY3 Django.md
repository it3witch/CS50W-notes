# 📚 CS50W DAY 3 - Django 学习笔记

## 📌 学习内容总结

### Django
Django是一个python web框架，允许我们编写能够动态生成HTML和CSS的Python代码，最终使我们能够构建动态Web应用程序

使用HTML和CSS编写的是静态的代码，但实际我们需要动态的Web应用，要根据用户对其操作进行相应反馈

我们将创建一个软件，能够在Web服务器上运行，以便在其Web浏览器中运行的客户端可以向我们的Web服务器发出请求，我们的服务器对某种响应作出回应

HTTP,也称超文本传输协议，有关消息在互联网上传递的协议：
GET / HTTP/1.1
HOST: WWW.example.com
···

HTTP/1.1 200 OK
Content-Type: text/html
···

# HTTP Status Codes
<!DOCTYPE html>
<html lang = "en">
    <head>
        <title>Table</title>
        <style>
            table {
                border: 1px solid black;
                border-collapse: collapse;
            }
            td,th {
                border: 1px solid black;
            }
        </style>
    </head>
    <body>
        <table>
            <thead>
                <tr>
                    <th>Status Code</th>
                    <th>Description</th>
                </tr>   
            </thead>
            <tbody>
                <tr>
                    <td>200</td>
                    <td>OK</td>
                </tr>
                <tr>
                    <td>301</td>
                    <td>Moved permanently</td>
                </tr>
                <tr>
                    <td>403</td>
                    <td>Forbidden</td>
                </tr>
                <tr>
                    <td>404</td>
                    <td>Not Found</td>
                </tr>
                <tr>
                    <td>500</td>
                    <td>Internal Server Error</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
···

# 准备工作
安装Django
pip3 install Django

django-admin startproject Project_name

项目目录结构（Django_exercise）
<pre> ```plaintext 
Django_exercise/ ├── Django_exercise/ │ ├── __init__.py │ ├── asgi.py │ ├── settings.py │ ├── urls.py │ └── wsgi.py ├── manage.py
``` </pre>

· manage.py 文件通常不需要修改，我们可以在Django项目上使用这个文件来执行命令

· setting.py 包含了Django应用程序的重要配置设置，预装了一些默认设置，我们额可以修改或者添加功能

· urls.py 用于访问多个不同的url或路由

下列都是在项目最外层目录\cs50w-notes\Django_exercise中进行操作

### 运行manage.py
python manage.py runserver
注意配置环境，确保在有django的环境下运行

### 创建一个新的app
创建hello app
python manage.py startapp hello

找到setting.py中的 INSTALLED_APPS, 添加新的hello

hello/urls.py
```py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("it3witch", views.it3witch, name="it3witch"),
    path("roxy", views.roxy, name="roxy"),
    path("<str:name>", views.greet, name="greet")
]
```

hello/views.py
```py
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

def it3witch(request):
    return HttpResponse("Hello, it3witch!")

def roxy(request):
    return HttpResponse("Hello, roxy!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
```

# 将response和HTML从实际的python代码中分离
```py
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "hello/index.html")
```
然后在hello下新建templates/hello/index.html,
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello!</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
    </body>
</html>
```
这样index就指向了这个HTML界面

# django模板语言渲染HTML
可以利用django自带的模板语言，使得HTML带有变量，判断和循环等
views.py
```py
from django.http import HttpResponse
from django.shortcuts import render

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
```

/hello/urls.py
```py
from django.urls import path

from . import views

urlpatterns = [
    path("<str:name>", views.greet, name="greet")
]
render可以接受一个可选的第三个参数，称为上下文(context)，它可以提供给模板所有其中的信息，变量，实例等
```
hello/templates/hello/greet.html
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello!</title>
    </head>
    <body>
        <h1>Hello, {{ name }}!</h1>
    </body>
</html>
```

### 判断语句
写一个应用程序来检测今天是不是元旦

在django下运行python manage.py startapp newyear，会得到一个新的app，newyear

记得在/Django_exercise/setting.py的INSTALLED_APPS中添加'newyear'
同时在/Django_exercise/urls.py中添加path('newyear/', include("newyear.urls"))确保能获取到newyear的urls

在newyear中新建文件夹urls，编写基础的url

在view中编写：
```py
from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1
    })
```

然后编写index.html
```html
<!DOCTYPE html>
<html lang="en">

    <head>
        <title>Is it New Year's</title>
    </head>
    <body>
        {% if newyear %}
            <h1>YES</h1>
        {% else %}
            <h1>NO</h1>
        {% endif %}
    </body>
</html>
```

其原理是调用datetime库来获取当前的日期时间，然后向newyear/index.html传递一个信息，为newyear变量（布尔型），判断条件是当前日期是否为1月1日

在django的语法下判断语句使用{% if newyear %}，{% else %}来判断，在判断结束时使用{% endif %}来表示判断语句结束

### 添加css
在newyear文件夹下新建static/newyear

static/newyear/styles.css
```css
h1 {
    font-family: sans-serif;
    font-size: 90px;
    text-align: center;
}
```
然后再index.html顶部添加{% load static %}来表示为该页面加载静态文件
再在<head>中添加<link href="{% static 'newyear/styles.css'%}" rel="stylesheet">