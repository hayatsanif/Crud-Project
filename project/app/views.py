from django.shortcuts import render
from .models import User,Queryd

# Create your views here.
def home(request):
    return render(request,'app/home.html')
    
def about(request):
    return render(request,'app/about.html')

def service(request):
    return render(request,'app/service.html')

def register(request):
    
    return render(request,'app/register.html')

def contact(request):
    return render(request,'app/contact.html')

def signIN(request):
    return render(request,'app/signIn.html')

def submit(request):
     
    if request.method=='POST':
        Fname=request.POST['fname']
        Email=request.POST['email']
        City=request.POST['city']
        Password=request.POST['password']
        Contact=request.POST['contact']
        Lname=request.POST['lname']
        user= User.objects.filter(Email=Email)

        if user: 
            message = "User already exist"
            return render(request,"app/register.html",{'msg':message})
        else:
            if Password==Password:
                newuser = User.objects.create(Fname=Fname,Lname=Lname,Email=Email
                                    ,Contact=Contact,Password=Password,City=City)
                message2 = "User register Successfully"
                return render(request,"app/signIN.html",{'msg2':message2})
    
    
    return render(request,'app/signIn.html')
    

def login1(request):
    if request.method=="POST":
        Email=request.POST['email']
        Password=request.POST['password']
        user = User.objects.filter(Email=Email)
        if user:
            data = User.objects.get(Email=Email)
            if data.Password == Password:
                Fname=data.Fname
                Lname=data.Lname
                Email=data.Email
                Contact=data.Contact
                user={
                    'fname':Fname,
                    'email':Email,
                    'lname':Lname,
                    'contact':Contact
                }
                return render(request,'app/dashboard.html',user)
            
def logout(request):
    return render(request,'app/home.html')

def query(request):
    if request.method=='POST':
        email=request.POST['email']
        query=request.POST['Query']

        Queryd.objects.create(queryemail=email, query=query)
        data = User.objects.get(Email=email)
        Fname=data.Fname
        Lname=data.Lname
        Email=data.Email
        Contact=data.Contact
        user={
                    'fname':Fname,
                    'email':Email,
                    'lname':Lname,
                    'contact':Contact
                }
    return render(request,'app/dashboard.html',user)

def show(request,pk):
    # print (pk)
    data=Queryd.objects.filter(queryemail=pk)
    return render(request,'app/showdata.html',{'key1':data})

def delete(request,pk):
    data=Queryd.objects.get(id=pk)
    email=data.queryemail
    data.delete()
    data=Queryd.objects.filter(queryemail=email)
    return render(request,'app/showdata.html',{'key1':data})

def edit(request,pk):
    data=Queryd.objects.get(id=pk)
    email=data.queryemail
    user=User.objects.get(Email=email)
    Nm=user.Fname
    Eml=user.Email
    Cnt=user.Contact
    Pwd=user.Password
    
    user={
        'name':Nm,
        'Email':Eml,
        'Contact':Cnt,
        'Password':Pwd
    }

    all_data=Queryd.objects.filter(queryemail=email)
    return render(request,'app/update.html',{'edit':data,'key1':all_data,'user':user})

def update(request,pk):
    updata=Queryd.objects.get(id=pk)
    updata.queryemail=request.POST['hayaemail']
    updata.query=request.POST['updatequery']
    updata.save()
    data2=User.objects.get(Email=updata.queryemail)
    Nm=data2.Fname
    Eml=data2.Email
    Cnt=data2.Contact
    Pwd=data2.Password
    
    user={
        'name':Nm,
        'Email':Eml,
        'Contact':Cnt,
        'Password':Pwd
    }

    all_data=Queryd.objects.filter(queryemail=updata.queryemail)
    return render(request,'app/showdata.html',{'key1':all_data,'user':user})


