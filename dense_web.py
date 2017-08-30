from flask import Flask, render_template,request,Response,flash
from  subprocess import call
import os
import datetime
import time
app = Flask(__name__,
        static_url_path='', 
            static_folder='data',
            template_folder='templates')
# app=Flask(__name__)

@app.route("/")
def result():
	return render_template('/index.html')

@app.route("/run",methods=["GET","POST"])
def run():
        checkpoint=request.form['checkpoint']
        if not checkpoint:
            checkpoint="checkpoint.t7"
        image_size=request.form['image_size']
        if not image_size:
            image_size="720"
        gpu=request.form['gpu']
        if not gpu:
            gpu=0
        input_dir=request.form['input_dir']
        if not input_dir:
            input_dir=""
        input_image=request.form['input_image']
        if not input_image:
            input_image="tt.jpg"
        num_proposals=request.form['num_proposals']
        if not num_proposals:
            num_proposals=1000
        print checkpoint
        cmd=['th','run_model.lua','-checkpoint',checkpoint,'-image_size',image_size,'-gpu',0,'-input_image',input_image]
	call(['python','test.py'])
	return render_template('/index.html')


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)
