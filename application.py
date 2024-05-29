from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mydb import *
import testapi
import webapi
import lifemodule.life
import financemodule.finance
import selflearning.selfleaning
import aimodule.ai
import tax.tax
app = Flask(__name__)

#web
app.add_url_rule('/', methods=["GET", "POST"], view_func=webapi.home)

# AI
app.add_url_rule('/ai', methods=["GET", "POST"], view_func=aimodule.ai.aihome)
app.add_url_rule('/ai-joke', methods=["GET"], view_func=aimodule.ai.telljoke)
app.add_url_rule('/ai-audio', methods=["GET"], view_func=aimodule.ai.audioupload)

# life
app.add_url_rule('/life', methods=["GET", "POST"], view_func=lifemodule.life.lifehome)

# finance
app.add_url_rule('/finance', methods=["GET", "POST"], view_func=financemodule.finance.financehome)
app.add_url_rule('/finance-creadit', methods=["GET", "POST"], view_func=financemodule.finance.financeCreadit)

#self learning
app.add_url_rule('/selflearning', methods=["GET", "POST"], view_func=  selflearning.selfleaning.selflearninghome)


#tax
app.add_url_rule('/tax', methods=["GET", "POST"], view_func=  tax.tax.taxhome)

@app.route("/about")
def about():
    return render_template("about.html")


#api
app.add_url_rule('/test', methods=["GET", "POST"], view_func=testapi.test)
app.add_url_rule('/test1', methods=["GET", "POST"], view_func=testapi.test1)
app.add_url_rule('/artical', methods=["GET", "POST"], view_func=testapi.template)
app.add_url_rule('/demo', methods=["GET", "POST"], view_func=testapi.template2)

app.add_url_rule('/apiLogin', methods=["GET", "POST"], view_func=testapi.apiLogin)
app.add_url_rule('/apiGetData', methods=["GET", "POST"], view_func=testapi.apiGetData)


if __name__ == "__main__":    
    app.run(debug=True,port=5001)
