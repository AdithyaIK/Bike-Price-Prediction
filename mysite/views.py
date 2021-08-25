from django.shortcuts import render
import joblib

def webpage(request):
    return render(request,'webpage.html')

def bikes(request):
    return render(request,'bikes.html')

def contact(request):
    return render(request,'contact.html')



def form(request):
    return render(request,"form.html")

def result(request):
    cls = joblib.load('Bikefinalized_model.sav')
    lis=[]
    lis.append(request.GET['Bike_company'])
    lis.append(request.GET['Bike_model'])
    lis.append(request.GET['Manufactured_year'])
    lis.append(request.GET['Engine_warranty'])
    lis.append(request.GET['Engine_type'])
    lis.append(request.GET['Fuel_type'])
    lis.append(request.GET['CC(Cubic capacity)'])
  

    #print(lis)

    ans = cls.predict([lis])
    ans=int(ans)
    
    return render(request,"result.html",{'ans':ans,'lis':lis})

def bajaj(request):
    return render(request,'bajaj.html')

def hero(request):
    return render(request,"hero.html")

def honda(request):
    return render(request,"honda.html")

def royalenfield(request):
    return render(request,"royalenfield.html")

def mahindra(request):
    return render(request,"mahindra.html")

def tvs(request):
    return render(request,"tvs.html")

def yamaha(request):
    return render(request,"yamaha.html")

def suzuki(request):
    return render(request,"suzuki.html")

def aboutus(request):
     return render(request,'aboutus.html')

# Create your views here.
