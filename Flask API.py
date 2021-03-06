# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 13:26:20 2021

@author: Ryan
"""
import cv2
from scipy.ndimage import variance
from skimage.color import rgb2gray
from skimage.filters import laplace
from skimage.transform import resize
import flask
from flask import Flask,request,jsonify
import skimage.io              # form 2, load skimage.io module only
from skimage import io
from PIL import Image
import matplotlib.image as mpimg

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    response = {'success': False}
    if flask.request.method == "POST":
        if flask.request.files.get("image"):
            file = request.files["image"]
            image = io.imread(file)
            image = resize(image, (400, 600))
            image = rgb2gray(image)
            edge_laplace = laplace(image, ksize=3)
            result = variance(edge_laplace)    
            print (result)
            threshold=0.0013
            if result > threshold:
                text="Not Blurry!"
            elif result <= threshold:
                text="Blurry!"
            response={
                "class": text,
                "Variance": result
                }
            response['success'] = True
    return jsonify(response)

if __name__ == "__main__":
    print(("* Loading Keras model and Flask starting server..."
        "please wait until server has fully started"))
    app.run(port=5000)