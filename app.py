print("starting flask....")
from flask import Flask,request,render_template

app = Flask(__name__) #Make name for app

@app.route("/",methods=["GET","POST"])
def Index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    #database
    return(render_template("main.html"))

@app.route("/dbs",methods=["GET","POST"])
def dbs():
    q = float(request.form.get("q"))
    return(render_template("dbs.html",r=(-50.6*q)+90.2))

if __name__ == "__main__":
    app.run() #ensure that you want to run the app on the cloud