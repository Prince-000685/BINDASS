from calendar import weekday
from django.shortcuts import render
from random import randrange
import pyrebase
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib import messages
from authentication.views import checkUserCredentials


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

def displayResultKalyan(request):
    try:
        today = datetime.date.today()
        d= today.strftime("%y/%m/%d")
        
        curr=""
        for i in range(0,len(d)):
            if d[i]=='/':
                curr+="-"
            else:
                curr+=d[i]

        
        data1 = db.child('kalyandata1').child(curr).get()
        data2 = db.child('kalyandata2').child(curr).get()
        data3 = db.child('kalyandata3').child(curr).get()
        
        rows1=[]
        for x in data1.each():
            data_list=[]
            data_list.append(x.key())
            y = x.val()
            data_list.append(y['num1'])
            rows1.append(data_list)

        rows2=[]
        for x in data2.each():
            data_list=[]
            data_list.append(x.key())
            y = x.val()
            data_list.append(y['num2'])
            rows2.append(data_list)
        
        rows3=[]
        for x in data3.each():
            data_list=[]
            data_list.append(x.key())
            y = x.val()
            data_list.append(y['num3'])
            rows3.append(data_list)

        new=[]
        for i in range (len(rows1)):
            all=[]
            all.append(rows1[i][1])
            all.append(rows2[i][1])
            all.append(rows3[i][1])
            all.append(rows1[i][0])
            new.append(all)           
        now = datetime.datetime.now()
        time = now.time()
        hour = time.hour
        
        min= time.minute

        res=[]
        for row in new:
            x = row[3]
            l = x.split(":")
            
            h_s = l[0]
            m_s = l[1]
            
            h = int(h_s)
            m = int(m_s)
            
            if(h < hour):
                if(h==12):
                    Ho = str(h)
                    Mi = str(m)
                    if(len(Ho)==1):
                        Ho = "0"+Ho
                    if(len(Mi)==1):
                        Mi = "0"+Mi
                    t=Ho+":"+Mi+"pm"
                    row[3] = t
                elif(h>12):
                    h=h-12
                    Ho = str(h)
                    Mi = str(m)
                    if(len(Ho)==1):
                        Ho = "0"+Ho
                    if(len(Mi)==1):
                        Mi = "0"+Mi
                    t=Ho+":"+Mi+"pm"
                    row[3] = t
                else:
                    Ho = str(h)
                    Mi = str(m)
                    if(len(Ho)==1):
                        Ho = "0"+Ho
                    if(len(Mi)==1):
                        Mi = "0"+Mi
                    t=Ho+":"+Mi+"am"
                    row[3] = t
                res.append(row)
            elif(h==hour and m<=min):
                if(h==12):
                    Ho = str(h)
                    Mi = str(m)
                    if(len(Ho)==1):
                        Ho = "0"+Ho
                    if(len(Mi)==1):
                        Mi = "0"+Mi
                    t=Ho+":"+Mi+"pm"
                    row[3] = t
                elif(h>12):
                    h=h-12
                    Ho = str(h)
                    Mi = str(m)
                    if(len(Ho)==1):
                        Ho = "0"+Ho
                    if(len(Mi)==1):
                        Mi = "0"+Mi
                    t=Ho+":"+Mi+"pm"
                    row[3] = t
                else:
                    Ho = str(h)
                    Mi = str(m)
                    if(len(Ho)==1):
                        Ho = "0"+Ho
                    if(len(Mi)==1):
                        Mi = "0"+Mi
                    t=Ho+":"+Mi+"am"
                    row[3] = t
                res.append(row)
        return render(request,"kalyandisplayresult.html",{"rows":res}) 
    except Exception as e:
        print('err:  ',e)
        return render(request,"kalyandisplayresult.html")


def saveResultKalyan(request):

    try:
        username = request.session.get('current_username')
        passw = request.session.get('current_password')
        print(username,passw)
        today = datetime.date.today()
        d= today.strftime("%y/%m/%d")
        
        curr=""
        for i in range(0,len(d)):
            if d[i]=='/':
                curr+="-"
            else:
                curr+=d[i]

        time2=request.GET['kalyantime']
        number1=request.GET['kalyannumber1']
        number2=request.GET['kalyannumber2']
        number3=request.GET['kalyannumber3']
        if(len(number1)==1):
            number1 = "0"+number1
        if(len(number2)==1):
            number2 = "0"+number2
        if(len(number3)==1):
            number3 = "0"+number3

        curr_hour = time2[0:2]
        curr_min = time2[3:]
        h = int(curr_hour) 
        m = int(curr_min)
        now = datetime.datetime.now()
        time = now.time()
        hour = time.hour
        
        user = checkUserCredentials(username,passw)
        if user==False:
            messages.error(request, 'Username or password is incorrect. Please login again.')
            # If authentication fails, return an error response
            return render(request,"Userinterface.html")
        if(hour < h):
            if(number1):
                if(weekday!=6):
                    row={"num1":number1}
                    db.child('kalyandata1').child(curr).child(time2).set(row)
            if(number2):
                if(weekday!=6):
                    row={"num2":number2}
                    db.child('kalyandata2').child(curr).child(time2).set(row)
            if(number3):
                if(weekday!=6):
                    row={"num3":number3}
                    db.child('kalyandata3').child(curr).child(time2).set(row)
        
        return render(request,"kalyandasboard.html",{'status':True})
    except Exception as e:
       print("errrrrrrrrr",e)
       return render(request,"kalyandasboard.html", {'status': False})



def SearchByDateKalyan(request):
    try:
        today = datetime.date.today()
        d = today.strftime("%y/%m/%d")
        t_date=""
        for i in range(0,len(d)):
            if d[i]=='/':
                t_date+="-"
            else:
                t_date+=d[i]

        date = request.GET['date'] 
        curr=date[2:] 

        curr_str = str(curr)

        c_list = curr_str.split("-")
        t_list = t_date.split("-")

        t_y = int(t_list[0])
        t_m = int(t_list[1])
        t_d = int(t_list[2])

        c_y = int(c_list[0])
        c_m = int(c_list[1])
        c_d = int(c_list[2])
        
        data1 = db.child('kalyandata1').child(curr).get()
        data2 = db.child('kalyandata2').child(curr).get()
        data3 = db.child('kalyandata3').child(curr).get()
        rows1=[]
        for x in data1.each():
            data_list=[]
            data_list.append(x.key())
            y = x.val()
            data_list.append(y['num1'])
            rows1.append(data_list)

        rows2=[]
        for x in data2.each():
            data_list=[]
            data_list.append(x.key())
            y = x.val()
            data_list.append(y['num2'])
            rows2.append(data_list)
        
        rows3=[]
        for x in data3.each():
            data_list=[]
            data_list.append(x.key())
            y = x.val()
            data_list.append(y['num3'])
            rows3.append(data_list)

        new=[]
        for i in range (len(rows1)):
            all=[]
            all.append(rows1[i][1])
            all.append(rows2[i][1])
            all.append(rows3[i][1])
            all.append(rows1[i][0])
            new.append(all)           
        now = datetime.datetime.now()
        time = now.time()
        hour = time.hour
        
        min= time.minute
        

        res=[]
        if (c_y<t_y):
            for row in new:
                    x = row[3]
                    l = x.split(":")
                    
                    h_s = l[0]
                    m_s = l[1]
                    
                    h = int(h_s)
                    m = int(m_s)
                    
                    
                    if(h==12):
                        Ho = str(h)
                        Mi = str(m)
                        if(len(Ho)==1):
                            Ho = "0"+Ho
                        if(len(Mi)==1):
                            Mi = "0"+Mi
                        t=Ho+":"+Mi+"pm"
                        row[3] = t
                    elif(h>12):
                        h=h-12
                        Ho = str(h)
                        Mi = str(m)
                        if(len(Ho)==1):
                            Ho = "0"+Ho
                        if(len(Mi)==1):
                            Mi = "0"+Mi
                        t=Ho+":"+Mi+"pm"
                        row[3] = t
                    else:
                        Ho = str(h)
                        Mi = str(m)
                        if(len(Ho)==1):
                            Ho = "0"+Ho
                        if(len(Mi)==1):
                            Mi = "0"+Mi
                        t=Ho+":"+Mi+"am"
                        row[3] = t
                    res.append(row)

        elif (c_m<t_m and c_y==t_y):
            for row in new:
                    x = row[3]
                    l = x.split(":")
                    
                    h_s = l[0]
                    m_s = l[1]
                    
                    h = int(h_s)
                    m = int(m_s)
                    
                    
                    if(h==12):
                        Ho = str(h)
                        Mi = str(m)
                        if(len(Ho)==1):
                            Ho = "0"+Ho
                        if(len(Mi)==1):
                            Mi = "0"+Mi
                        t=Ho+":"+Mi+"pm"
                        row[3] = t
                    elif(h>12):
                        h=h-12
                        Ho = str(h)
                        Mi = str(m)
                        if(len(Ho)==1):
                            Ho = "0"+Ho
                        if(len(Mi)==1):
                            Mi = "0"+Mi
                        t=Ho+":"+Mi+"pm"
                        row[3] = t
                    else:
                        Ho = str(h)
                        Mi = str(m)
                        if(len(Ho)==1):
                            Ho = "0"+Ho
                        if(len(Mi)==1):
                            Mi = "0"+Mi
                        t=Ho+":"+Mi+"am"
                        row[3] = t
                    res.append(row)

        elif (c_m==t_m and c_y==t_y):

            if(c_d <t_d):
                for row in new:
                    x = row[3]
                    l = x.split(":")
                    
                    h_s = l[0]
                    m_s = l[1]
                    
                    h = int(h_s)
                    m = int(m_s)
                    
                    
                    if(h==12):
                        Ho = str(h)
                        Mi = str(m)
                        if(len(Ho)==1):
                            Ho = "0"+Ho
                        if(len(Mi)==1):
                            Mi = "0"+Mi
                        t=Ho+":"+Mi+"pm"
                        row[3] = t
                    elif(h>12):
                        h=h-12
                        Ho = str(h)
                        Mi = str(m)
                        if(len(Ho)==1):
                            Ho = "0"+Ho
                        if(len(Mi)==1):
                            Mi = "0"+Mi
                        t=Ho+":"+Mi+"pm"
                        row[3] = t
                    else:
                        Ho = str(h)
                        Mi = str(m)
                        if(len(Ho)==1):
                            Ho = "0"+Ho
                        if(len(Mi)==1):
                            Mi = "0"+Mi
                        t=Ho+":"+Mi+"am"
                        row[3] = t
                    res.append(row)

            elif (c_d==t_d):
                for row in new:
                    x = row[3]
                    l = x.split(":")
                    
                    h_s = l[0]
                    m_s = l[1]
                    
                    h = int(h_s)
                    m = int(m_s)
                    
                    if(h == hour and m<=min):
                        if(h==12):
                            Ho = str(h)
                            Mi = str(m)
                            if(len(Ho)==1):
                                Ho = "0"+Ho
                            if(len(Mi)==1):
                                Mi = "0"+Mi
                            t=Ho+":"+Mi+"pm"
                            row[3] = t
                        elif(h>12):
                            h=h-12
                            Ho = str(h)
                            Mi = str(m)
                            if(len(Ho)==1):
                                Ho = "0"+Ho
                            if(len(Mi)==1):
                                Mi = "0"+Mi
                            t=Ho+":"+Mi+"pm"
                            row[3] = t
                        else:
                            Ho = str(h)
                            Mi = str(m)
                            if(len(Ho)==1):
                                Ho = "0"+Ho
                            if(len(Mi)==1):
                                Mi = "0"+Mi
                            t=Ho+":"+Mi+"am"
                            row[3] = t
                        res.append(row)
                    elif(h<hour):
                        if(h==12):
                            Ho = str(h)
                            Mi = str(m)
                            if(len(Ho)==1):
                                Ho = "0"+Ho
                            if(len(Mi)==1):
                                Mi = "0"+Mi
                            t=Ho+":"+Mi+"pm"
                            row[3] = t
                        elif(h>12):
                            h=h-12
                            Ho = str(h)
                            Mi = str(m)
                            if(len(Ho)==1):
                                Ho = "0"+Ho
                            if(len(Mi)==1):
                                Mi = "0"+Mi
                            t=Ho+":"+Mi+"pm"
                            row[3] = t
                        else:
                            Ho = str(h)
                            Mi = str(m)
                            if(len(Ho)==1):
                                Ho = "0"+Ho
                            if(len(Mi)==1):
                                Mi = "0"+Mi
                            t=Ho+":"+Mi+"am"
                            row[3] = t
                        res.append(row)

        return render(request,"kalyanResultByDate.html",{'rows':res}) 
    except Exception as e:
        print('errooooor:',e)
        return render(request,'kalyanResultByDate.html')

def SearchAllKalyan(request):
    try:
        date = request.GET['date']
        curr=date[2:]
        
        data1 = db.child('kalyandata1').child(curr).get()
        data2 = db.child('kalyandata2').child(curr).get()
        data3 = db.child('kalyandata3').child(curr).get()
        rows1=[]
        for x in data1.each():
            data_list=[]
            data_list.append(x.key())
            y = x.val()
            data_list.append(y['num1'])
            rows1.append(data_list)

        rows2=[]
        for x in data2.each():
            data_list=[]
            data_list.append(x.key())
            y = x.val()
            data_list.append(y['num2'])
            rows2.append(data_list)
        
        rows3=[]
        for x in data3.each():
            data_list=[]
            data_list.append(x.key())
            y = x.val()
            data_list.append(y['num3'])
            rows3.append(data_list)

        new=[]
        for i in range (len(rows1)):
            all=[]
            all.append(rows1[i][1])
            all.append(rows2[i][1])
            all.append(rows3[i][1])
            all.append(rows1[i][0])
            new.append(all)       

        res=[]
        for row in new:
           
            l = row[3].split(":")
            
            h_s = l[0]
            m_s = l[1]
            
            h = int(h_s)
            m = int(m_s)
            
            
            if(h==12):
                Ho = str(h)
                Mi = str(m)
                if(len(Ho)==1):
                    Ho = "0"+Ho
                if(len(Mi)==1):
                    Mi = "0"+Mi
                t=Ho+":"+Mi+"pm"
                row[3] = t
            elif(h>12):
                h=h-12
                Ho = str(h)
                Mi = str(m)
                if(len(Ho)==1):
                    Ho = "0"+Ho
                if(len(Mi)==1):
                    Mi = "0"+Mi
                t=Ho+":"+Mi+"pm"
                row[3] = t
            else:
                Ho = str(h)
                Mi = str(m)
                if(len(Ho)==1):
                    Ho = "0"+Ho
                if(len(Mi)==1):
                    Mi = "0"+Mi
                t=Ho+":"+Mi+"am"
                row[3] = t
            res.append(row)

        return render(request,"editresultKalyan.html",{'rows':res}) 
    except Exception as e:
        print('erreeee:  ',e)
        return render(request,'editresultKalyan.html')

