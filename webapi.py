from flask import Flask, render_template, request, redirect, url_for
from mydb import *

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
            return render_template("index.html", questions=[question,ans_a,ans_b,ans_c,ans_d,answer,rotation])
          

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
            return render_template("index.html", questions=[question,ans_a,ans_b,ans_c,ans_d,answer,rotation])
          

    return render_template("index.html")