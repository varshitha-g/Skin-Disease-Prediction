# -*- coding: utf-8 -*-
"""
Created on Mon May 11 15:37:56 2020

@author: Admin
"""

import numpy as np
import os
from keras.models import load_model
from keras.preprocessing import image

import tensorflow as tf
global graph
#graph=tf.get_default_graph()
from flask import Flask,request,render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

app=Flask(__name__)
model=load_model("skindisease.h5")

@app.route('/')
def index():
    return render_template("base.html")

@app.route('/predict',methods=['GET','POST'])
def upload():
    if request.method=='POST':
        f=request.files['image']
        print("current path")
        basepath=os.path.dirname(__file__)
        print("current path",basepath)
        filepath=os.path.join(basepath,f.filename)
        f.save(filepath)
        img = image.load_img(filepath, target_size = (64, 64))
        '''img=image.load_img(filepath,target_size=(64,64))'''
        x=image.img_to_array(img)
        x=np.expand_dims(x,axis=0)
        
        
        preds=model.predict(x)
        '''print("prediction",preds)'''
        index = ['Acne','Melanoma','Peeling skin','Ring worm','Vitiligo']
        label=np.argmax(preds,axis=1)[0]
        text = "The Skin Disease is " + "\""+str(index[label]+"\"")
    return text
        
    
if __name__=='__main__':
    app.run(debug=True,threaded=False)