from flask import Flask, render_template,request,Response,flash
from  subprocess import call
import os
import datetime
import time
app = Flask(__name__)


@app.route("/")
def result():
	return render_template('/index.html')

@app.route("/run",methods=["GET","POST"])
def run():
        optest=request.form['optest']
        optest2=request.form['optest2']
        print optest,optest2
	call(['ls',optest])
	time.sleep(3)
	return render_template('/index.html')


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
