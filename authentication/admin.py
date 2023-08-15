from django.contrib import admin
# Register your models here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth
from django.views.decorators.clickjacking import xframe_options_exempt
import pyrebase
import requests

Config = {
    "apiKey": "AIzaSyBDRyktE8ZTcnEXEp0URJjTtkeJF9tWnpc",
  "authDomain": "auto-user-3765b.firebaseapp.com",
  "databaseURL": "https://auto-user-3765b-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "auto-user-3765b",
  "storageBucket": "auto-user-3765b.appspot.com",
  "messagingSenderId": "463223116683",
  "appId": "1:463223116683:web:3dee8bd7363d63bf52558e"
}

firebase = pyrebase.initialize_app(Config)
authe = firebase.auth()
db = firebase.database()

@xframe_options_exempt
def adminLogin(request):
   
  try: 
    data = db.child("admin").get()
    username=""
    password=""
    for x in data.each():
      username = x.key()
      password = x.val()
    
    user = request.GET['username']
    pwd = request.GET["password"]

    if user == username and pwd==password:
      usersData = db.child("users").get()

      rows = []
      for x in usersData.each():
        info = []
        info.append(x.key())
        info.append(x.val())
        rows.append(info)

      return render(request, "usersData.html",{'rows':rows})
    else:
      return render(request, "adminLogin.html",{'msg':'Wrong Username/Password'})
        
  except Exception as e:
    print('errr--',e)
    return render(request, "adminLogin.html")
  

# def updatePassword(request):
#     user = request.GET['username']
#     new_password = request.GET["password"]

#     try:
#         data = db.child("users").get()
        
#         credentials = []
#         for x in data.each():
#             credentials.append(x.key())

#         usersData = db.child("users").get()
#         rows = []
#         for x in usersData.each():
#           info = []
#           info.append(x.key())
#           info.append(x.val())
#           rows.append(info)

#         # Check if the provided username matches the stored username
#         if user in credentials:
#             db.child("users").update({user: new_password})

#             return render(request, "usersData.html",{'msg': 'Password updated successfully',"rows":rows})
#         else:
#             return render(request, "usersData.html", {'msg': 'Invalid username',"rows":rows})

#     except Exception as e:
#         print('Error:', e)
#         return render(request, "usersData.html")

from django.contrib.auth import logout
def updateAdminPasspage(request):
   return render(request,'updateAdminPass.html')

def updateAdminPass(request):
   cPass=request.GET['cPassword']
   new_pass=request.GET['newPassword']
   try:
      data=db.child('admin').get()
      for x in data:
         key=x.key()
         oldPass=x.val()
         if oldPass==cPass:
          db.child('admin').update({key:new_pass})

          return render(request,'updateAdminPass.html',{'msg':'Password Updated Successfully'})
         else:
          return render(request,"updateAdminPass.html",{'msg':'Please enter correct currentPassowrd'})
      
   except Exception as e:
      print('er00 : ',e)
      return render(request,'updateAdminPass.html')

def updatePassword(request):
    user = request.GET['username']
    new_password = request.GET["password"]

    action = request.GET['action']
    
    try:
      if action == "update":
      
          data = db.child("users").get()

          credentials = []
          for x in data.each():
              credentials.append(x.key())

          usersData = db.child("users").get()
          rows = []
          for x in usersData.each():
              info = []
              info.append(x.key())
              info.append(x.val())
              rows.append(info)

          # Check if the provided username matches the stored username
          if user in credentials:
              # Update the user's password in the Firebase database
              db.child("users").update({user: new_password})
              usersData = db.child("users").get()
              rows = []
              for x in usersData.each():
                info = []
                info.append(x.key())
                info.append(x.val())
                rows.append(info)

              # Check if the user has an active session
              if request.user.is_authenticated and request.user.username == user:
                  # If the user has an active session and their password was changed by the admin,
                  # invalidate the session to force re-authentication
                  logout(request)

              return render(request, "usersData.html", {'msg': 'Password updated successfully', "rows": rows})
          else:
              return render(request, "usersData.html", {'msg': 'Invalid username', "rows": rows})
          
      elif action == "delete":
        userList ={}
        usersData = db.child("users").get()

        for x in usersData.each():
          userList.update({x.key():x.val()})
        
        userList.pop(user)

        db.child('users').set(userList)

        data = db.child("users").get()
        rows = []
        for x in data.each():
          info = []
          info.append(x.key())
          info.append(x.val())
          rows.append(info)

        return render(request, "usersData.html", {'msg': 'User deleted successfully', "rows": rows})
      
    except Exception as e:
      print('Error:', e)
      return render(request, "usersData.html")

def AddUserPage(request):
   return render(request,"AddUser.html")

def AddUser(request):
   try:
      username = request.GET['username']
      password = request.GET['password']

      userList ={}
      usersData = db.child("users").get()

      for x in usersData.each():
        userList.update({x.key():x.val()})

      userList.update({username:password})

      db.child('users').update(userList)

      
      return render(request, "AddUser.html",{'msg': 'User Added successfully'})
   except Exception as e:
      print("user error:",e)
      return render(request, "AddUser.html",{'msg': 'User Not Added'})



