# 后端接口设计文档

## 响应状态码列表

- 200: 请求成功
- 400: 请求参数错误
- 401: 用户未认证或认证失败
- 403: 用户权限不足，无法访问资源
- 404: 请求的资源不存在
- 500: 服务器内部错误

## 权限认证方式

使用JWT（JSON Web Token）进行认证，用户在登录后将获得一个有效的JWT Token，在后续请求中通过Authorization Header携带Token进行认证。

## API 定义

+ host: `localhost:8000`

### 用户

#### 登录

+ url:`/users/login`

+ method:`POST`

+ 请求：

  ```json
  {
  	"username":"string",
  	"password":"string"
  }
  ```
  
  + response
  
    + 状态码： 200

    ```json
    {
        "access_token": "string",
    }
    ```
  
    

#### 注册

+ url:`/users/register`

+ method:`POST`

+ 请求：

  ```json
  {
  	"username":"string",
  	"password":"string",
  	"email":"string",
  	"whatsup":"string",	//个性签名
  	"gender":"string",	//性别
  	"region":"string",	//地区
  }
  ```
  
  + response
  
    + 状态码： 200

    ```json
    {
        "user_id": "string"
    }
    ```
  
    

### 脚本库

#### 脚本列表

+ url:`/scripts`

+ 查询参数：

  - sort_by (string, optional): 排序依据，可选值为 "stars"、"create_time" 等，默认值 create_time
  - order (string, optional): 排序顺序，asc 为升序，desc 为降序，默认为升序
  - limit (int, optional): 返回条目的数量，默认值10
  - offset (int, optional): 返回条目的开始位置，默认值1

+ method:`GET`

+ 返回：

  +状态码： 200

  ```json
{
  "data": [
    {
      "id": "string",
      "title": "string",
      "description": "string",
      "author": "string",
      "stars": "number",
      "create_time": "datetime"
    },
      ...
     ]
  }
      
  
```



#### 脚本详情


+ url:`/scripts/detail?id={number}`

+ method:`GET`

+ 查询参数：

  - id (int, required): 脚本的 ID

+ 返回：

  +状态码： 200

  ```json
{
  "data":  {
      "id": "string",
      "title": "string",
      "description": "string",
      "author": "string",
      "stars": "number",
      "create_time": "datetime",
      "content":"string"
    }
  }
  ```