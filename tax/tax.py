
from flask import Flask, render_template, request, redirect, url_for

def taxhome():   
   return render_template("/tax/tax.html")