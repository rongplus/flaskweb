from flask import Flask, render_template, request, redirect, url_for
import markdown.extensions.fenced_code
#pip install Flask-Markdown

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