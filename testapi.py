from flask import Flask, render_template, request, redirect, url_for
import markdown.extensions.fenced_code
#pip install Flask-Markdown
from openai import OpenAI
from ollama import generate
from ollama import AsyncClient


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



def tellJoke():
    response = generate('llama2', 'Tell me a funny joke')
    print(response['response'])
    return render_template("joke.html",joke=response['response'])

def tellJoke1():
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    temperature = 0.2,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke."}
    ]
    )

    #print(completion.choices[0].message)
    a = completion.choices[0].message.content.split('\n') 

    return render_template("joke.html",joke=a)

def askQuestion():
    question = ''
    if request.method == "POST":   
        question = request.form.get("question")
    if question:
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
        )
        return render_template("askme.html",joke=completion.choices[0].message.content)
    
    return render_template("askme.html")