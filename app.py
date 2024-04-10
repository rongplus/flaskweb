from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mydb import *
import testapi
import webapi
app = Flask(__name__)

#web
app.add_url_rule('/', methods=["GET", "POST"], view_func=webapi.home)

@app.route("/about")
def about():
    return render_template("about.html")

app.add_url_rule("/add", methods=["GET", "POST"],view_func=webapi.add)
    
@app.route('/modulequestions')
def modulequestions():     
    data = getModule2Question()
    return render_template('modulequestions.html', records=data)   

#app.add_url_rule('/showone', methods=["GET", "POST"], view_func=webapi.showone)
app.add_url_rule('/search', methods=["GET", "POST"], view_func=webapi.search)
#called by add page
app.add_url_rule('/addRightAnserQuestion', methods=["GET", "POST"], view_func=webapi.addRightAnserQuestion)
app.add_url_rule('/addWrongAnserQuestion', methods=["GET", "POST"], view_func=webapi.addWrongAnserQuestion)

app.add_url_rule('/joke', methods=["GET", "POST"], view_func=webapi.tellJoke)
#app.add_url_rule('/askme', methods=["GET", "POST"], view_func=webapi.askQuestion)
app.add_url_rule('/save_text', methods=['POST'], view_func=webapi.save_text)

#api
app.add_url_rule('/test', methods=["GET", "POST"], view_func=testapi.test)
app.add_url_rule('/test1', methods=["GET", "POST"], view_func=testapi.test1)
app.add_url_rule('/artical', methods=["GET", "POST"], view_func=testapi.template)
app.add_url_rule('/demo', methods=["GET", "POST"], view_func=testapi.template2)

app.add_url_rule('/apiLogin', methods=["GET", "POST"], view_func=testapi.apiLogin)
app.add_url_rule('/apiGetData', methods=["GET", "POST"], view_func=testapi.apiGetData)


if __name__ == "__main__":    
    app.run(debug=True)
