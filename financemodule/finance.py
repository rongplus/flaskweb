

from flask import Flask, render_template, request, redirect, url_for

def financehome():   
    if request.method == "POST":
        print("post")
        audio = request.files['audio_data']
    else:
        return render_template("finance/finance.html")
    

def financeCreadit():
    return render_template("finance/creaditcard.html")