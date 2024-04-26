from flask import Flask, render_template, request, redirect, url_for
import markdown.extensions.fenced_code
#pip install Flask-Markdown
import requests
from flask import Flask, request, jsonify


import jwt
from datetime import datetime, timezone,timedelta
# 假设这是你的JWT密钥
JWT_SECRET_KEY = 'your-secret-key'


def post_request(api_url, data):
    """
    Send a POST request to the specified API URL with the given data.

    :param api_url: str - The URL of the API endpoint.
    :param data: dict - The data to be sent in the POST request.
    :return: requests.Response - The response object from the API.
    """
    try:
        response = requests.post(api_url, json=data)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")

def test():
    if request.method == "POST": 
           #country = request.get_json()     
           #print(country) 
           name = request.form.get("name") 
           print(name)
           return "test post"
    elif request.method =="GET":
        return "test get"
    
def test1():
    if request.method == "POST": 
           name = request.get_json()     
           #print(country) 
           #name = request.form.get("name") 
           print(name)
           return "welcome  " +name["name"]
    elif request.method =="GET":
        name = request.args.get('name') 
        #http://127.0.0.1:5000/test1?name=rong
        #http://127.0.0.1:5000/query_example?language=PHP&framework=Flask&website=flask.org
        #language = request.args.get('language') 
        #framework = request.args['framework'] 
        #website = request.args.get('website') 
        return "Hello " + name
    
def template():
    #dd
    name = request.args.get('name') 
    f = open("demofile.txt","r",encoding='utf-16')
    con = f.readline() #f.read()
    return render_template('template.html', content=con)

def template2():
    #dd
    #name = request.args.get('name') 
    readme_file  = open("demo.md","r")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code"]
    )
    #return md_template_string
    #<li> {{content|safe}}</li><br>
    #<li> {{content|markdown }}</li><br>
    return render_template('template.html', content=md_template_string )


def tellMeOllamaJoke():
     #use Ollama 2
    response = post_request('http://localhost:11434/api/generate', {"model":"llama2", "prompt":"Tell me a funny joke about Windows?", "stream": False})
    print(response.json()["response"])


def creatToken(username):
    payload = {
                'user_id': username,
                'exp': datetime.now(timezone.utc) + timedelta(minutes=30)
            }

            # 使用秘钥生成 JWT Token
    print(payload)
    
    jwt_token = jwt.encode(payload=payload, key=JWT_SECRET_KEY, algorithm='HS256')
    return jwt_token

def decodeToken(token):
    # 解码 Token
    decoded_token = jwt.decode(token, JWT_SECRET_KEY,algorithms=['HS256'],verify=True, options={'verify_exp':False})
    print("0-----------------------------")

    # 获取 Payload 中的数据
    user_id = decoded_token['user_id']
    expiration_time = decoded_token['exp']
    b = datetime.fromtimestamp(expiration_time,tz=timezone.utc)
    print(user_id,b)
    a = datetime.now(timezone.utc) 
    print(a,b)

    # 验证 Token 是否过期
    if a > b :
        print('Token 已过期')
        return user_id+" Token 已过期"
    else:
        print('Token 未过期')
        return user_id+" Token 未过期"
    
 

def apiLogin():
    if request.method == "POST": 
           
           web_json = request.get_json() 
           return creatToken(web_json['name'])
           print(web_json)
           ret = decodeToken(web_json["token"])
           return "welcome  " +web_json["name"] + ret
    elif request.method =="GET":
        name = request.args.get('name') 
        return "abcd"

def apiGetData():
    if request.method == "POST":            
           web_json = request.get_json()           
           print(web_json)
           ret = decodeToken(web_json["token"])
           return "welcome  " +web_json["name"] + ret
    elif request.method =="GET":
        name = request.args.get('name') 