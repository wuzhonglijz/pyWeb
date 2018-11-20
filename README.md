# 这是一个 Java web 程序设计的作业
本质上是一个响应式的 Python web 项目，用于自助式、协作式地提交班级报表
- 后端使用轻量级 Python 框架 flask
- 前端 UI 框架使用极轻量级的 css 库 milligram
- 前后端交互使用简洁优雅的 Axios
- 记录存储使用单文件轻量级数据库 SQLite3
- 对记录的操作使用了 RESTful 的接口
- - -
~~Demo: http://us2.wzl.cc~~
FCC certification: https://freecodecamp.cn/wuzhonglijz/front-end-certification  

## 已经实现的功能
1. 记录的提交, 查询, 简单的输入错误提示.  
2. 记录的删除按钮与实现.
3. 在每条记录后面加上操作按钮 "修改", "删除", 完整实现了基于 SQLAlchemy 的数据库的CRUD. (2018-5-31)
## 下一步需要实现/正在实现中的功能
1. 正则检测输入数据的正确性. 细化错误提示粒度.
2. 待定.
    
## 部署方法
### essential env (debian)
需要 python3+
```
$pip install flask  
$pip install flask_sqlalchemy
```

### dev
```
$python main.py
```
访问 http://127.0.0.1:5000

### prod
1. 安装 http 服务器 nginx, Wsgi 服务器 gunicorn, 并发框架 gevent.
```
$apt install nginx
$pip install gunicorn
$pip install gevent
```

2. 配置 nginx 反向代理:  

```$nano /etc/nginx/sites-available/default```
```
server {
        listen 80;
        server_name //your domain name eg. us2.wzl.cc//;

        location / {
                proxy_pass http://127.0.0.1:8000;
                proxy_redirect     off;
                proxy_set_header   Host                 $http_host;
                proxy_set_header   X-Real-IP            $remote_addr;
                proxy_set_header   X-Forwarded-For      $proxy_add_x_forwarded_for;
                proxy_set_header   X-Forwarded-Proto    $scheme;
        }
}
```
3. 重新启动 ngxin.
```
$service nginx restart
```
3. 运行 gunicorn, 同时启动 gevent.
```
$gunicorn -D -b 127.0.0.1:8000 -k gevent -w 2 main:app --error-logfile gunicorn_error.log
```
4. 停止服务器.
```
$service nginx stop
$killall gunicorn
```
