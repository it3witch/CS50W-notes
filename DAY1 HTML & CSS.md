# 📚 CS50W DAY 1 - HTML & CSS 学习笔记

## 📌 学习内容总结

### HTML
- 了解了 HTML 是网页的结构。
- 学会了常见的标签：
  - `<html>`, `<head>`, `<body>`, `<h1>` ~ `<h6>`, `<p>`, `<a>`, `<img>`, `<ul>`, `<ol>`, `<li>`, `<div>`, `<span>`
- 学会使用链接、图片和表格。

# 1.Hello world!
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello!</title>
    </head>
    <body>
        Hello, world!
    </body>
</html>
```

# 2.hover 
### 鼠标放在上面会变化
```html
<pre> ```<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello!</title>
        <style>
            button {
                width: 200px;
                height: 50px;
                font-size: 24px;
                background-color: green;
            }
        button:hover {
            background-color: blue;
        }
        </style>
    </head>
    <body>
        <button>Click Me!</button>
    </body>
</html>``` </pre>
```
# 3.attribute
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello!</title>
        <style>
            a {
                color: blue;
            }      
            a[href="http://bilibili.com"] {
                color: red
            }
        </style>
    </head>
    <body>
        <ul><a href="http://google.com">Google</a></ul>
        <ul><a href="http://bilibili.com">Bilibili</a></ul>
        <ul><a href="http://baidu.com">Baidu</a></ul>
    </body>
</html>
```
-指定a标签内的特定来源使用a[]

# 4.class & id
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello!</title>
        <style>
            .baz {
                color:blue
            }
        </style>
    </head>
    <body>
        <h1 class="baz">Heading 1</h1>
        <h1 class="baz">Heading 2</h1>
        <h1>Heading 3</h1>
    </body>
</html>
```

```html
<html lang="en">
    <head>
        <title>Hello!</title>
        <style>
            #foo {
                color:blue
            }
        </style>
    </head>
    <body>
        <h1 id="foo">Heading 1</h1>
        <h1 id="boo">Heading 2</h1>
        <h1>Heading 3</h1>
    </body>
</html>
```

-指定class使用 .
-指定id使用 #

# 4.table
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
                    <th>Ocean</th>
                    <th>Average Depth</th>
                    <th>Maximum Depth</th>
                </tr>   
            </thead>
            <tbody>
                <tr>
                    <td>Pacific Ocean</td>
                    <td>4,280 m</td>
                    <td>10,911 m</td>
                </tr>
                <tr>
                    <td>Atlantic Ocean</td>
                    <td>3,646 m</td>
                    <td>8,486 m</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>

```html
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
                    <th>Ocean</th>
                    <th>Average Depth</th>
                    <th>Maximum Depth</th>
                </tr>   
            </thead>
            <tbody>
                <tr>
                    <td>Pacific Ocean</td>
                    <td>4,280 m</td>
                    <td>10,911 m</td>
                </tr>
                <tr>
                    <td>Atlantic Ocean</td>
                    <td>3,646 m</td>
                    <td>8,486 m</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
```

-  table表格分为thead & tbody，thead内部有<tr>表示table row（行），然后<th>表示表头
 在tbody中用<tr>区分行，然后每行中用<td> table data写每一格的数据

-  表格中可以用 border: 1px solid black;来画线 
 border-collapse: collapse;表示把线合并

# 5.响应式设计
-flexbox
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello!</title>
        <style>
            #container {
                display: flex;
                flex-wrap: wrap;
            }
            #container > div {
                background-color: springgreen;
                font-size: 20px;
                margin: 20px;
                padding: 20px;
                width: 200px;
            }
        </style>
    </head>
    <body>
        <div id="container">
             <div>1.This is some sample text inside of a div to demo Flexbox</div>
             <div>2.This is some sample text inside of a div to demo Flexbox</div>
             <div>3.This is some sample text inside of a div to demo Flexbox</div>
             <div>4.This is some sample text inside of a div to demo Flexbox</div>
             <div>5.This is some sample text inside of a div to demo Flexbox</div>
             <div>6.This is some sample text inside of a div to demo Flexbox</div>
             <div>7.This is some sample text inside of a div to demo Flexbox</div>
             <div>8.This is some sample text inside of a div to demo Flexbox</div>
             <div>9.This is some sample text inside of a div to demo Flexbox</div>
             <div>10.This is some sample text inside of a div to demo Flexbox</div>
             <div>11.This is some sample text inside of a div to demo Flexbox</div>
             <div>12.This is some sample text inside of a div to demo Flexbox</div>
        </div>
    </body>
</html>
```
-grid
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello!</title>
        <style>
            #grid {
                background-color: blue;
                display: grid;
                padding: 20px;
                grid-column-gap: 20px;
                grid-row-gap: 10px;
                grid-template-columns: 200px 200px auto;
            }
            .grid-item {
                background-color: white;
                font-size: 20px;
                padding: 20px
            }
        </style>
    </head>
    <body>
        <div id="grid">
            <div class="grid-item">1</div>
            <div class="grid-item">2</div>
            <div class="grid-item">3</div>
            <div class="grid-item">4</div>
            <div class="grid-item">5</div>
            <div class="grid-item">6</div>
            <div class="grid-item">7</div>
            <div class="grid-item">8</div>
            <div class="grid-item">9</div>
            <div class="grid-item">10</div>
            <div class="grid-item">11</div>
            <div class="grid-item">12</div>
        </div>
    </body>
</html>
```
# responsive
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello!</title>
        <style>
            @media (min-width: 600px) {
                body {
                    background-color: red;
                }
            }
            @media (max-width: 599px) {
                body {
                    background-color: blue;
                }
            }
        </style>
    </head>
    <body>
        <h1>Welcome to my Web Page!</h1>
    </body>
</html>
```
-可以保证在窗口在大于600的时候显示red，小于599的时候显示blue