localhost:8000

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
  
    ```json
    {
        
    }
    ```
  
    

#### 注册

+ url:`/users/register`

+ method:`POST`

+ 请求：

  ```json
  {
  	"username":"string,
  	"username":"string",
  	"password":"string"，
  	"email":"string",
  	"whatsup":"string",	//个性签名，微信是这么翻译的
  	"gender":"string",	//性别
  	"region":"string",	//地区
  }
  ```
  
  + response
  
    ```json
    {
        
    }
    ```
  
    

### 脚本库

#### 脚本列表

+ url:`/scripts

+ method:`GET`

+ 返回：

  ```json
{
  "data": [
    {
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


+ 返回：

  ```json
{
  "data":  {
      "title": "string",
      "description": "string",
      "author": "string",
      "stars": "number",
      "create_time": "datetime",
      "content":"string"
    }
  }
  ```