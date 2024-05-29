

from flask import Flask, render_template, request, redirect, url_for

def selflearninghome():   
    if request.method == "POST":
        print("post")
        audio = request.files['audio_data']
    else:
        return render_template("selfimprovment/self.html")