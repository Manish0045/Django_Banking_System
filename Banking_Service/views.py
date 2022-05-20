from django.shortcuts import render,redirect
from Banking_Service.models import  Customers, transactiondetail

# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'index.html')

def customers(request):
    customers = Customers.objects.all()
    if request.method == "POST":
        email = request.POST.get('email')
        semail = request.POST.get('semail')
        amt = request.POST.get('amt')
        try:
            amt = int(amt)
        except:
            print("enter amount")
        for i in customers:
            print(email)
            if i.email == email:
                j = i
                id = i.id
                break
        for i in customers:
            print(i.email,i.avail_bal,semail)
            if i.email==semail and amt< i.avail_bal and amt>0 :
                avail_bal = i.avail_bal - amt
                avail_bal2 = j.avail_bal + amt
                try:
                    query1 = transactiondetail(name=i.name, email=i.email,
                                                deb_amt=amt ,cr_amt=0 , ac_bal=avail_bal)

                    query2 = Customers(id=i.id, avail_bal=avail_bal, email=i.email
                                                    , name=i.name)
                    query3 = transactiondetail(name=j.name, email=j.email,
                                                deb_amt=0 ,cr_amt=amt , ac_bal=avail_bal2)
                    query4 = Customers(id=id, avail_bal=avail_bal2, email=j.email
                                                    , name=j.name)
                    query2.save()
                    query1.save()
                    query4.save()
                    query3.save()
                    
                    return render("{% url 'Transactions' %}")
                    break
                except:
                    print("transection failed")
                    break
        else:
            print("invalid data")
            return render(request,'customer.html')
         
    return render(request,'customer.html',{'customers':customers})

def trans(request):
    trans = transactiondetail.objects.all()
    return render(request,'transactions.html',{'trans':trans})