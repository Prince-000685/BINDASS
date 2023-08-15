from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth
from django.views.decorators.clickjacking import xframe_options_exempt
import pyrebase

Config1 = {
   "apiKey": "AIzaSyBDRyktE8ZTcnEXEp0URJjTtkeJF9tWnpc",
  "authDomain": "auto-user-3765b.firebaseapp.com",
  "databaseURL": "https://auto-user-3765b-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "auto-user-3765b",
  "storageBucket": "auto-user-3765b.appspot.com",
  "messagingSenderId": "463223116683",
  "appId": "1:463223116683:web:3dee8bd7363d63bf52558e"
}

Config2 = {
   "apiKey": "AIzaSyDJ-DSPETfHzviczt2Y6qJ8Qzf3XC3cL2w",
  "authDomain": "automatic-77977.firebaseapp.com",
  "databaseURL": "https://automatic-77977-default-rtdb.firebaseio.com",
  "projectId": "automatic-77977",
  "storageBucket": "automatic-77977.appspot.com",
  "messagingSenderId": "631988995528",
  "appId": "1:631988995528:web:1d92fbf71ddec1ff7bacfd"
}

firebase1 = pyrebase.initialize_app(Config1)
authe1 = firebase1.auth()
db1 = firebase1.database()

firebase2 = pyrebase.initialize_app(Config2)
authe2 = firebase1.auth()
db2 = firebase1.database()


def checkUserCredentials(username,password):
  data = db1.child("users").get()
  # data2=db1.child("admin").get()
  # for x in data2:
  #    key=x.key()
  #    value=x.val()
  #    if username==key and password==value:
  #       return True
  credentials = []
  for x in data.each():
      info = []
      key = x.key()
      value = x.val()
      credentials.append
      # print(key,value)
      if username == key and password == value:
         return True
  return False


@xframe_options_exempt
def userLogin(request):   
  try: 
    data1 = db2.child('btn1').child('b1').get()
    btn1=data1.val()
    data2 = db2.child('btn2').child('b2').get()
    btn2=data2.val()
    data3= db2.child('btn3').child('b3').get()
    btn3=data3.val()

    d1 = db2.child('kBtn1').child('b1').get()
    b1=d1.val()
    d2 = db2.child('kBtn2').child('b2').get()
    b2=d2.val()
    d3= db2.child('kBtn3').child('b3').get()
    b3=d3.val()
    
    username = request.POST['username']
    passw = request.POST['pass1'] 
    
    auth = checkUserCredentials(username,passw)

    if auth :
        if "bindas" in username:
          request.session['current_username'] = username
          request.session['current_password'] = passw
          return render(request, "dasboard.html",{"btn1":btn1,"btn2":btn2,"btn3":btn3})
        elif "kalyan" in username:
           request.session['current_username'] = username
           request.session['current_password'] = passw
           return render(request, "kalyandasboard.html",{"b1":b1,"b2":b2,"b3":b3})
    else:
      return render(request, "Userinterface.html",{'msg':'Wrong Username/Password'})
  except Exception as e:
    print('errr--',e)
    return render(request, "Userinterface.html")
        
  

