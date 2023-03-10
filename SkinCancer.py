# -*- coding: utf-8 -*-
"""Ref.no.0201_software.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b1JZ9baYE-ZijoCQCeiOW7mzCM6fHtgQ

# Importing of the libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from PIL import Image
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.svm import SVC
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization
import tensorflow as tf
from tensorflow import keras
import warnings
from sklearn.ensemble import RandomForestClassifier
warnings.filterwarnings('ignore')

"""# Define path for image dataset"""

for dirname, _, filenames in os.walk('C:/Users/User/SkinCancer/data/'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

benigndir=os.listdir("C:/Users/User/SkinCancer/data/train/benign")+os.listdir("C:/Users/User/SkinCancer/data/test/benign")

len(benigndir)

image1=Image.open("C:/Users/User/SkinCancer/data/train/benign/3.jpg")
plt.imshow(image1)

image2=Image.open("C:/Users/User/SkinCancer/data/train/benign/12.jpg")
plt.imshow(image2)

image3=Image.open("C:/Users/User/SkinCancer/data/test/benign/61.jpg")
plt.imshow(image3)

image4=Image.open("C:/Users/User/SkinCancer/data/test/benign/16.jpg")
plt.imshow(image4)

image5=Image.open("C:/Users/User/SkinCancer/data/test/benign/250.jpg")
plt.imshow(image5)

"""# Visualization of images of Full directory"""

malignantdir=os.listdir("C:/Users/User/SkinCancer/data/train/malignant")+os.listdir("C:/Users/User/SkinCancer/data/test/malignant")

image6=Image.open("C:/Users/User/SkinCancer/data/train/malignant/36.jpg")
plt.imshow(image6)

image7=Image.open("C:/Users/User/SkinCancer/data/train/malignant/63.jpg")
plt.imshow(image7)

image8=Image.open("C:/Users/User/SkinCancer/data/test/malignant/185.jpg")
plt.imshow(image8)

"""# Loading of the image dataset"""

def load_images(path):
    images=[]
    label=[]
    Folders=os.listdir(path)
    for i in Folders:
        sub_folders=os.listdir(path+'/'+i)
        for j in sub_folders[:1000]:
            every_img=Image.open(path+i+'/'+j)
            every_img=every_img.resize(size=(64,64))
            every_img=every_img.convert('L')
            images.append(np.array(every_img).flatten())
            label.append(i)
            del every_img
    return np.array(images),label

X,y=load_images('C:/Users/User/SkinCancer/data/train/')
y=pd.Series(y,dtype='category')

y=y.cat.codes

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=123,shuffle=True)

X_train.shape

X_test.shape

"""# ANN"""

ann=Sequential()

ann.add(Dense(130,activation='sigmoid',input_dim=X_train.shape[1]))

ann.add(Dense(5,activation='softmax'))

ann.compile(loss='sparse_categorical_crossentropy',optimizer='RMSprop',metrics=['accuracy'])

ann.summary()

history=ann.fit(X_train,y_train,epochs=10, validation_data = (X_test, y_test))

y_pred=ann.predict(X_test)

y_pred=np.argmax(y_pred,axis=1)

acc_ann=accuracy_score(y_pred,y_test)

acc_ann

cm = confusion_matrix(y_test, y_pred)

cm

sns.heatmap(cm,annot=True)

print(classification_report(y_test,y_pred))

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs_range = range(10)

plt.figure(figsize=(5, 5))
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

epochs_range

plt.figure(figsize=(5, 5))
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()

