# Skin Disease Prediction

This repository contains a deep learning project that uses a Convolutional Neural Network (CNN) to detect various skin diseases from images. The goal of this project is to assist healthcare professionals by providing a model that can classify skin diseases, enhancing accessibility to diagnostics through machine learning.

## Table of Contents

   Overview
   
   Dataset
   
   Model Architecture
   
   Technologies Used
   
   Results
   
   Installation
   
   Usage
   
  
## Overview

Skin disease detection is crucial for early diagnosis and treatment. This project implements a CNN model to classify images into five skin disease categories with an accuracy of approximately 70%. The model is deployed via a user-friendly web application built with Flask, enabling users to upload images and receive real-time predictions.

## Dataset

Source: The dataset used in this project contains images of skin diseases across five categories.

Size: 500 images.

Preprocessing: Images were resized and normalized. Data augmentation techniques were applied to improve model robustness.
## Model Architecture

The model uses a Convolutional Neural Network (CNN) implemented with TensorFlow and Keras, optimized for image classification tasks. The architecture includes:

Multiple convolutional layers with ReLU activations and max pooling.

Dense layers for classification, with a final softmax layer for outputting probabilities across the five categories.

Data augmentation for reducing overfitting.

### Key Layers:
Convolutional Layers: For feature extraction from images.

Pooling Layers: To reduce the spatial dimensions of the feature maps.

Dense Layers: Fully connected layers for decision-making.
## Technologies Used

Python: For programming.

TensorFlow & Keras: For building and training the CNN model.

Flask: For deploying the model as a web application.

Pandas & NumPy: For data processing.

Matplotlib & Seaborn: For visualization and analysis.
## Results

Accuracy: Achieved a 70% classification accuracy across five skin disease types.

Evaluation: Model performance was assessed using metrics such as accuracy and a confusion matrix.

Challenges: The limited size of the dataset posed challenges for generalization, addressed by data augmentation.

## Installation

To run this project locally, follow these steps:

### 1. Clone the repository:
            git clone https://github.com/varshitha-g/Skin-Disease-Prediction.git
            cd Skin-Disease-Prediction
### 2. Create a virtual environment:
            python -m venv env
            source env/bin/activate  # On Windows, use `env\Scripts\activate`
### 3. Install the dependencies:
            pip install -r requirements.txt
## Usage

### 1. Training the Model: Run train.py to train the model using the dataset.
                     python train.py
### 2. Running the Flask App: To start the web application and make predictions through the UI, run:
                     python app.py
Open your browser and navigate to http://127.0.0.1:5000 to access the application.
### 3. Uploading Images: 

Use the interface to upload images of skin lesions, and the model will return a classification along with a confidence score.



