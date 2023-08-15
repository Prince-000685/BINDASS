# your_app/tasks.py

from celery import shared_task
from datetime import datetime
import pyrebase

from BindasPlay.adminviews import ATypeSubmit1, ATypeSubmit2, ATypeSubmit3, ATypeSubmitKalyan1, ATypeSubmitKalyan2, ATypeSubmitKalyan3


Config = {
   "apiKey": "AIzaSyDJ-DSPETfHzviczt2Y6qJ8Qzf3XC3cL2w",
  "authDomain": "automatic-77977.firebaseapp.com",
  "databaseURL": "https://automatic-77977-default-rtdb.firebaseio.com",
  "projectId": "automatic-77977",
  "storageBucket": "automatic-77977.appspot.com",
  "messagingSenderId": "631988995528",
  "appId": "1:631988995528:web:1d92fbf71ddec1ff7bacfd"
}

firebase = pyrebase.initialize_app(Config)
authe = firebase.auth()
db = firebase.database()


@shared_task
def daily_task():
    # Your code for the daily task goes here
    # For example, run your specific endpoint here

    # You can call your Django view function directly if needed
    # from your_app.views import your_view_function
    # your_view_function()

    # Alternatively, if you have a URL mapped to your endpoint, you can use requests library to trigger it
    # import requests
    # response = requests.get('http://your_domain/your_endpoint/')
    # print(response.status_code)

    # For demonstration purposes, just print the current datetime

    a=db.child('btn1').get()
    b=db.child('btn2').get()
    c=db.child('btn3').get()
    d=db.child('kbtn1').get()
    e=db.child('kbtn2').get()
    f=db.child('kbtn3').get()
    for x in a:
        value=x.val()
        if value=='automatic':
            ATypeSubmit1()

    for x in b:
        value=x.val()
        if value=='automatic':
            ATypeSubmit2()

    for x in c:
        value=x.val()
        if value=='automatic':
            ATypeSubmit3()
        
    for x in d:
        value=x.val()
        if value=='automatic':
            ATypeSubmitKalyan1()

    for x in e:
        value=x.val()
        if value=='automatic':
            ATypeSubmitKalyan2()

    for x in f:
        value=x.val()
        if value=='automatic':
            ATypeSubmitKalyan3()


