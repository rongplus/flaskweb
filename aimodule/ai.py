

from flask import Flask, render_template, request, redirect, url_for

def aihome():     
    return render_template("ai/ai.html")
    


def telljoke():   
    if request.method == "POST":
        print("post")
        audio = request.files['audio_data']
    else:
        return render_template("ai/ai.html")

def audioupload():   
    if request.method == "POST":
        print("post")
        audio = request.files['audio_data']
    else:
        return render_template("ai.html")