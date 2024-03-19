from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mydb import *
import testapi
import webapi
app = Flask(__name__)

#web
@app.route("/")
def home():
    all_routes = get_all_routes()
    print("List of all routes:")
    result=f"<br>"
    for route in all_routes:
        print(f"/{route}")
        result+= f"<a href=" + f"/{route}" + f">" + f"{route}" + f"</a><br>"
    return render_template("home.html", routes=all_routes)
    return "Welcome to the home page!" + result

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/add", methods=["GET", "POST"])
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

@app.route('/questions')
def questions():     
    data = getAllQuestion()
    return render_template('questions.html', records=data)
    
@app.route('/modulequestions')
def modulequestions():     
    data = getModule2Question()
    return render_template('modulequestions.html', records=data)   

app.add_url_rule('/showone', methods=["GET", "POST"], view_func=webapi.showone)
app.add_url_rule('/addRightAnserQuestion', methods=["GET", "POST"], view_func=webapi.addRightAnserQuestion)
app.add_url_rule('/addWrongAnserQuestion', methods=["GET", "POST"], view_func=webapi.addWrongAnserQuestion)

def get_all_routes():
    routes = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint != "static":
            routes.append(rule.endpoint)
    return routes

#api
app.add_url_rule('/test', methods=["GET", "POST"], view_func=testapi.test)
app.add_url_rule('/test1', methods=["GET", "POST"], view_func=testapi.test1)
app.add_url_rule('/artical', methods=["GET", "POST"], view_func=testapi.template)
app.add_url_rule('/demo', methods=["GET", "POST"], view_func=testapi.template2)

if __name__ == "__main__":    
    app.run(debug=True)
