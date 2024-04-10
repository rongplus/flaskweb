from flask import Flask, render_template, request, redirect, url_for
from mydb import *

import requests

def home():   
    return render_template("home.html")


def showone(): 
    global cursor  # Use the global cursor

    if request.method == "POST":
        next_button = request.form.get("next_button")
        if next_button:
            record = cursor.fetchone()
            if record:
                return render_template("question.html", question=record[1],
                                       answera=record[2],answerb=record[3],answerc=record[4],answerd=record[5],
                                       answer=record[6],rotation=record[7])
            else:
                return "No more records."
        return redirect(url_for("showone"))

    cursor.execute("SELECT * FROM insuranceB where module=2")
    record = cursor.fetchone()
   
    return render_template("question.html", question=record[1],
                                       answera=record[2],answerb=record[3],answerc=record[4],answerd=record[5],
                                       answer=record[6],rotation=record[7])
    
def getModule2Question():
    global cursor  # Use the global cursor

    if request.method == "POST":
        next_button = request.form.get("next_button")
        if next_button:
            record = cursor.fetchone()
            if record:
                return render_template("modulequestions.html", question=record[1],
                                       answera=record[2],answerb=record[3],answerc=record[4],answerd=record[5],
                                       answer=record[6],rotation=record[7])
            else:
                return "No more records."
        return redirect(url_for("showone"))

    cursor.execute("SELECT * FROM insuranceB where module=2")
    record = cursor.fetchone()
   
    return render_template("modulequestions.html", question=record[1],
                                       answera=record[2],answerb=record[3],answerc=record[4],answerd=record[5],
                                       answer=record[6],rotation=record[7])


def addright():
    if request.method == "POST":        
           return "addright"
    elif request.method =="GET":
        return "ABC"

    return render_template("addright.html")

def addwrong():
     
    if request.method == "POST":
        question = request.form.get("question")
        answers = request.form.get("answers")
        rotation = request.form.get("rotation")
        if question:
            save_note_to_db1(question,answers,rotation)
            return redirect(url_for("addwrong"))

    return render_template("addwrong.html")

def search():
    if request.method == "POST":
        con= request.form.get("question")
        record = searchDB(con)
        if record:
            return render_template("question.html", question=record[1],
                                       answera=record[2],answerb=record[3],answerc=record[4],answerd=record[5],
                                       answer=record[6],rotation=record[7])
        else:
            render_template("search.html")
    return render_template("search.html")


def addRightAnserQuestion():
    if request.method == "POST":
         con= request.form.get("question")
         cor = 1
         
         if con:
            pos1 = con.find('a)')
            question = con[:pos1]
            pos2 = con.find('b)')
            ans_a = con[pos1:pos2]
            pos1 = pos2
            pos2 = con.find('c)')
            ans_b = con[pos1:pos2]
            pos1 = pos2
            pos2 = con.find('d)')
            ans_c = con[pos1:pos2]
            pos1 = pos2
            pos2 =  con.find('YOUR ANSWER')
            ans_d = con[pos1:pos2]
            pos1 = pos2
            pos2 = con.find('Rationale:')
            answer = con[pos1+10:pos2]
            rotation = con[pos2+10:]
            
            saveQuestions(question,ans_a,ans_b,ans_c,ans_d,answer,rotation,cor,2)
            return render_template("index.html", questions=[question,ans_a,ans_b,ans_c,ans_d,answer,rotation,"Right"])
          

    return render_template("index.html")

def addWrongAnserQuestion():
    if request.method == "POST":
         con= request.form.get("question")
         cor = 0   
         if con:
            pos1 = con.find('a)')
            question = con[:pos1]
            pos2 = con.find('b)')
            ans_a = con[pos1:pos2]
            pos1 = pos2
            pos2 = con.find('c)')
            ans_b = con[pos1:pos2]
            pos1 = pos2
            pos2 = con.find('d)')
            ans_c = con[pos1:pos2]
            pos1 = pos2
            pos2 =  con.find('YOUR ANSWER')
            ans_d = con[pos1:pos2]
            pos1 = pos2
            pos2 = con.find('Rationale:')
            answer = con[pos1+10:pos2]
            rotation = con[pos2+10:]
            
            saveQuestions(question,ans_a,ans_b,ans_c,ans_d,answer,rotation,cor,2)
            return render_template("index.html", questions=[question,ans_a,ans_b,ans_c,ans_d,answer,rotation,"Wrong"])
          

    return render_template("index.html")

def tellJoke():
    response = post_request('http://localhost:11434/api/generate', {"model":"llama2", "prompt":"Tell me a funny joke about Windows?", "stream": False})
    print(response.json()["response"])
    return render_template("joke.html",joke=response.json()["response"])

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



def save_text():
    text_data = request.json.get('text', '')
    # Save the text_data to a file or database
    return 'Text saved successfully', 200


def get_all_routes():
    routes = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint != "static":
            routes.append(rule.endpoint)
    return routes



def add():
     if request.method == "POST":
         con= request.form.get("question")
         cor = 0
         if request.form.get("correct"):
             cor = 1
         
         if con:
            pos1 = con.find('a)')
            question = con[:pos1]
            pos2 = con.find('b)')
            ans_a = con[pos1:pos2]
            pos1 = pos2
            pos2 = con.find('c)')
            ans_b = con[pos1:pos2]
            pos1 = pos2
            pos2 = con.find('d)')
            ans_c = con[pos1:pos2]
            pos1 = pos2
            pos2 =  con.find('YOUR ANSWER')
            ans_d = con[pos1:pos2]
            pos1 = pos2
            pos2 = con.find('Rationale:')
            answer = con[pos1+10:pos2]
            rotation = con[pos2+10:]
            
            saveQuestions(question,ans_a,ans_b,ans_c,ans_d,answer,rotation,cor,2)
            return render_template("index.html", questions=[question,ans_a,ans_b,ans_c,ans_d,answer,rotation])
          

     return render_template("index.html")



#@app.route('/questions')
def questions():     
    data = getAllQuestion()
    return render_template('questions.html', records=data)