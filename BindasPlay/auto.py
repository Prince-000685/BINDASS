from django.shortcuts import render
from django.contrib import messages
from random import randrange
import pyrebase
import datetime
from django.contrib.auth import authenticate
from authentication.views import checkUserCredentials



Config2 = {
  "apiKey": "AIzaSyBDRyktE8ZTcnEXEp0URJjTtkeJF9tWnpc",
  "authDomain": "auto-user-3765b.firebaseapp.com",
  "databaseURL": "https://auto-user-3765b-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "auto-user-3765b",
  "storageBucket": "auto-user-3765b.appspot.com",
  "messagingSenderId": "463223116683",
  "appId": "1:463223116683:web:3dee8bd7363d63bf52558e"
}


Config = {
   "apiKey": "AIzaSyDJ-DSPETfHzviczt2Y6qJ8Qzf3XC3cL2w",
  "authDomain": "automatic-77977.firebaseapp.com",
  "databaseURL": "https://automatic-77977-default-rtdb.firebaseio.com",
  "projectId": "automatic-77977",
  "storageBucket": "automatic-77977.appspot.com",
  "messagingSenderId": "631988995528",
  "appId": "1:631988995528:web:1d92fbf71ddec1ff7bacfd"
}


firebase1 = pyrebase.initialize_app(Config2)
auth = firebase1.auth()
db1 = firebase1.database()


firebase = pyrebase.initialize_app(Config)
authe = firebase.auth()
db = firebase.database()


 

def TypeSubmit1(request):
    try:
        username = request.session.get('current_username')
        passw = request.session.get('current_password')
        print(username,passw)
        # print(username)
        # data1 = db.child('btn1').child('b1').get()
        # btn1=data1.val()
        # data2 = db.child('btn2').child('b2').get()
        # btn2=data2.val()
        # data3= db.child('btn3').child('b3').get()
        # btn3=data3.val()
        # if(btn1=="automatic"):
        #     row={"b1":"manual"}
        #     db.child('btn1').set(row)

        # elif(btn1=="manual"):
        #     row={"b1":"automatic"}
        #     db.child('btn1').set(row)
        today = datetime.date.today()
        d = today.strftime("%y/%m/%d")
        
        L = ["10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30","19:00","19:30","20:00","20:30","21:00","21:30","22:00"]
        
        weekday = today.weekday()
        t_date=""
        for i in range(0,len(d)):
            if d[i]=='/':
                t_date+="-"
            else:
                t_date+=d[i]

        now = datetime.datetime.now()
        time = now.time()
        hour = time.hour
        
        min= time.minute

        
        user = checkUserCredentials(username,passw)
        print("8888 : " ,user)
        if user==False:
            messages.error(request, 'Username or password is incorrect. Please login again.')
            # If authentication fails, return an error response
            return render(request,"Userinterface.html")
        for t in L:
            h = int(t[0:2])
            m = int(t[3:])
            if(h>hour):
                number = randrange(0,100)
                y = str(number)
                if(len(y)==1):
                    y = "0"+y
                
                if(weekday!=6):
                    row={"num1":y}
                    db.child('data1').child(t_date).child(t).set(row)
            elif(h==hour and m>=min):
                number = randrange(0,100)
                y = str(number)
                if(len(y)==1):
                    y = "0"+y
                
                if(weekday!=6):
                    row={"num1":y}
                    db.child('data1').child(t_date).child(t).set(row)

                # d1 = db.child('btn1').child('b1').get()
                # b1=d1.val()
            
        return render(request,"dasboard.html")
        # return render(request,"dasboard.html",{"btn1":b1,"btn2":btn2,"btn3":btn3})
    except Exception as e:
        print("errrr:",e)
        return render(request,"dasboard.html")


def TypeSubmit2(request):
    try:
        username = request.session.get('current_username')
        passw = request.session.get('current_password')
        # data1 = db.child('btn1').child('b1').get()
        # btn1=data1.val()
        # data2 = db.child('btn2').child('b2').get()
        # btn2=data2.val()
        # data3= db.child('btn3').child('b3').get()
        # btn3=data3.val()
        # if(btn2=="automatic"):
        #     row={"b2":"manual"}
        #     db.child('btn2').set(row)

        # elif(btn2=="manual"):
        #     row={"b2":"automatic"}
        #     db.child('btn2').set(row)
        today = datetime.date.today()
        d = today.strftime("%y/%m/%d")
        
        L = ["10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30","19:00","19:30","20:00","20:30","21:00","21:30","22:00"]
        
        weekday = today.weekday()
        t_date=""
        for i in range(0,len(d)):
            if d[i]=='/':
                t_date+="-"
            else:
                t_date+=d[i]
    
    
        now = datetime.datetime.now()
        time = now.time()
        hour = time.hour
        
        min= time.minute

        user = checkUserCredentials(username,passw)
        if user==False:
            messages.error(request, 'Username or password is incorrect. Please login again.')
            # If authentication fails, return an error response
            return render(request,"Userinterface.html")
        for t in L:
            h = int(t[0:2])
            m = int(t[3:])
            if(h>hour):
                number = randrange(0,100)
                y = str(number)
                if(len(y)==1):
                    y = "0"+y
                
                if(weekday!=6):
                    row={"num2":y}
                    db.child('data2').child(t_date).child(t).set(row)
            elif(h==hour and m>=min):
                number = randrange(0,100)
                y = str(number)
                if(len(y)==1):
                    y = "0"+y
                
                if(weekday!=6):
                    row={"num2":y}
                    db.child('data2').child(t_date).child(t).set(row)

            # d2 = db.child('btn2').child('b2').get()
            # b2=d2.val()
        return render(request,"dasboard.html")
        # return render(request,"dasboard.html",{"btn1":btn1,"btn2":b2,"btn3":btn3})
    except Exception as e:
        print("errrr:",e)
        return render(request,"dasboard.html")

def TypeSubmit3(request):
    try:
        username = request.session.get('current_username')
        passw = request.session.get('current_password')
        # data1 = db.child('btn1').child('b1').get()
        # btn1=data1.val()
        # data2 = db.child('btn2').child('b2').get()
        # btn2=data2.val()
        # data3= db.child('btn3').child('b3').get()
        # btn3=data3.val()
        # if(btn3=="automatic"):
        #     row={"b3":"manual"}
        #     db.child('btn3').set(row)

        # elif(btn3=="manual"):
        #     row={"b3":"automatic"}
        #     db.child('btn3').set(row)
        today = datetime.date.today()
        d = today.strftime("%y/%m/%d")
        
        L = ["10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30","19:00","19:30","20:00","20:30","21:00","21:30","22:00"]
        
        weekday = today.weekday()
        t_date=""
        for i in range(0,len(d)):
            if d[i]=='/':
                t_date+="-"
            else:
                t_date+=d[i]
    
    
        now = datetime.datetime.now()
        time = now.time()
        hour = time.hour
        
        min= time.minute

        user = checkUserCredentials(username,passw)
        if user==False:
            messages.error(request, 'Username or password is incorrect. Please login again.')
            # If authentication fails, return an error response
            return render(request,"Userinterface.html")
        for t in L:
            h = int(t[0:2])
            m = int(t[3:])
            if(h>hour):
                number = randrange(0,100)
                y = str(number)
                if(len(y)==1):
                    y = "0"+y
                
                if(weekday!=6):
                    row={"num3":y}
                    db.child('data3').child(t_date).child(t).set(row)
            elif(h==hour and m>=min):
                number = randrange(0,100)
                y = str(number)
                if(len(y)==1):
                    y = "0"+y
                
                if(weekday!=6):
                    row={"num3":y}
                    db.child('data3').child(t_date).child(t).set(row)
            
            # d3 = db.child('btn3').child('b3').get()
            # b3=d3.val()
            
        return render(request,"dasboard.html")
        # return render(request,"dasboard.html",{"btn1":btn1,"btn2":btn2,"btn3":b3})
    except Exception as e:
        print("errrr:",e)
        return render(request,"dasboard.html")

def TypeSubmitKalyan1(request):
    try:
        username = request.session.get('current_username')
        passw = request.session.get('current_password')
        print(username,passw)
        # da1 = db.child('kBtn1').child('b1').get()
        # bt1=da1.val()
        # da2 = db.child('kBtn2').child('b2').get()
        # bt2=da2.val()
        # da3= db.child('kBtn3').child('b3').get()
        # bt3=da3.val()
        
        # if(bt1=="automatic"):
        #     row={"b1":"manual"}
        #     db.child('kBtn1').set(row)

        # elif(bt1=="manual"):
        #     row={"b1":"automatic"}
        #     db.child('kBtn1').set(row)

        today = datetime.date.today()
        d = today.strftime("%y/%m/%d")
        
        L = ["12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00"]
        
        weekday = today.weekday()
        t_date=""
        for i in range(0,len(d)):
            if d[i]=='/':
                t_date+="-"
            else:
                t_date+=d[i]
    
        now = datetime.datetime.now()
        time = now.time()
        hour = time.hour
        
        min= time.minute

        user = checkUserCredentials(username,passw)
        if user==False:
            messages.error(request, 'Username or password is incorrect. Please login again.')
            # If authentication fails, return an error response
            return render(request,"Userinterface.html")

        for t in L:
            h = int(t[0:2])
            m = int(t[3:])
            if(h>hour):
                number = randrange(0,100)
                y = str(number)
                if(len(y)==1):
                    y = "0"+y
                
                if(weekday!=6):
                    row={"num1":y}
                    db.child('kalyandata1').child(t_date).child(t).set(row)
            elif(h==hour and m>=min):
                number = randrange(0,100)
                y = str(number)
                if(len(y)==1):
                    y = "0"+y
                
                if(weekday!=6):
                    row={"num1":y}
                    db.child('kalyandata1').child(t_date).child(t).set(row)

            # dat1= db.child('kBtn1').child('b1').get()
            # btn1=dat1.val()
            
        return render(request,"kalyandasboard.html")
        # return render(request,"kalyandasboard.html",{"b1":btn1,"b2":bt2,"b3":bt3})
    except Exception as e:
        print("errrr:",e)
        return render(request,"kalyandasboard.html")


def TypeSubmitKalyan2(request):
    try:
        username = request.session.get('current_username')
        passw = request.session.get('current_password')
        # da1 = db.child('kBtn1').child('b1').get()
        # bt1=da1.val()
        # da2 = db.child('kBtn2').child('b2').get()
        # bt2=da2.val()
        # da3= db.child('kBtn3').child('b3').get()
        # bt3=da3.val()
        # if(bt2=="automatic"):
        #     row={"b2":"manual"}
        #     db.child('kBtn2').set(row)

        # elif(bt2=="manual"):
        #     row={"b2":"automatic"}
        #     db.child('kBtn2').set(row)

        today = datetime.date.today()
        d = today.strftime("%y/%m/%d")
        
        L = ["12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00"]
        
        weekday = today.weekday()
        t_date=""
        for i in range(0,len(d)):
            if d[i]=='/':
                t_date+="-"
            else:
                t_date+=d[i]
    
        now = datetime.datetime.now()
        time = now.time()
        hour = time.hour
        
        min= time.minute

        user = checkUserCredentials(username,passw)
        if user==False:
            messages.error(request, 'Username or password is incorrect. Please login again.')
            # If authentication fails, return an error response
            return render(request,"Userinterface.html")


        for t in L:
            h = int(t[0:2])
            m = int(t[3:])
            if(h>hour):
                number = randrange(0,100)
                y = str(number)
                if(len(y)==1):
                    y = "0"+y
                
                if(weekday!=6):
                    row={"num2":y}
                    db.child('kalyandata2').child(t_date).child(t).set(row)
            elif(h==hour and m>=min):
                number = randrange(0,100)
                y = str(number)
                if(len(y)==1):
                    y = "0"+y
                
                if(weekday!=6):
                    row={"num2":y}
                    db.child('kalyandata2').child(t_date).child(t).set(row)

            # d2= db.child('kBtn2').child('b2').get()
            # btn2=d2.val()
            
        return render(request,"kalyandasboard.html")
        # return render(request,"kalyandasboard.html",{"b1":bt1,"b2":btn2,"b3":bt3})
    except Exception as e:
        print("errrr:",e)
        return render(request,"kalyandasboard.html")


def TypeSubmitKalyan3(request):
    try:
        username = request.session.get('current_username')
        passw = request.session.get('current_password')
        # da1 = db.child('kBtn1').child('b1').get()
        # bt1=da1.val()
        # da2 = db.child('kBtn2').child('b2').get()
        # bt2=da2.val()
        # da3= db.child('kBtn3').child('b3').get()
        # bt3=da3.val()
        # if(bt3=="automatic"):
        #     row={"b3":"manual"}
        #     db.child('kBtn3').set(row)

        # elif(bt3=="manual"):
        #     row={"b3":"automatic"}
        #     db.child('kBtn3').set(row)

        today = datetime.date.today()
        d = today.strftime("%y/%m/%d")
        
        L = ["12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00"]
        
        weekday = today.weekday()
        t_date=""
        for i in range(0,len(d)):
            if d[i]=='/':
                t_date+="-"
            else:
                t_date+=d[i]
    
        now = datetime.datetime.now()
        time = now.time()
        hour = time.hour
        
        min= time.minute

        user = checkUserCredentials(username,passw)
        if user==False:
            messages.error(request, 'Username or password is incorrect. Please login again.')
            # If authentication fails, return an error response
            return render(request,"Userinterface.html")

        for t in L:
            h = int(t[0:2])
            m = int(t[3:])
            if(h>hour):
                number = randrange(0,100)
                y = str(number)
                if(len(y)==1):
                    y = "0"+y
                
                if(weekday!=6):
                    row={"num3":y}
                    db.child('kalyandata3').child(t_date).child(t).set(row)
            elif(h==hour and m>=min):
                number = randrange(0,100)
                y = str(number)
                if(len(y)==1):
                    y = "0"+y
                
                if(weekday!=6):
                    row={"num3":y}
                    db.child('kalyandata3').child(t_date).child(t).set(row)

            # d3= db.child('kBtn3').child('b3').get()
            # btn3=d3.val()
            
        return render(request,"kalyandasboard.html")
        # return render(request,"kalyandasboard.html",{"b1":bt1,"b2":bt2,"b3":btn3})
    except Exception as e:
        print("errrr:",e)
        return render(request,"kalyandasboard.html")


