from flask import Flask, render_template, request, redirect, url_for

def lifehome():   
    return render_template("life.html")