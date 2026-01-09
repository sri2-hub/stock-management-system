from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
import time
from django.utils import timezone
from django.db.models import Q
def getadmin(request):
    if(request.session.has_key('aemail')):
        eid=request.session['aemail']
        adm=smsadmin.objects.get(email=eid)
        return adm
    else:
        return None

def dashboard(request):
    adm=getadmin(request)
    if(adm):
        ts=smsfinalsale.objects.all().count()
        tp=smsfinalpurchase.objects.all().count()
        tc=smscustomer.objects.all().count()
        tpr=smsproduct.objects.all().count()
        return render(request,'dashboard.html',{'adm':adm,'ts':ts,'tp':tp,'tpr':tpr,'tc':tc})
    else:
        messages.warning(request, 'Please Login')
        return redirect ('/adminlogin')

def addadmin(request):
    adm=getadmin(request)
    if(adm):
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            phonenumber = request.POST.get("phonenumber")
            address = request.POST.get("address")
            password = request.POST.get("password")
            img = request.FILES.get("img")
            emailcheck=smsadmin.objects.filter(email=email)
            if(emailcheck):
                    messages.warning(request, 'Data already exists.')
                    return redirect ('/addadmin')
            else:
                sms=smsadmin(name=name,email=email,phonenumber=phonenumber,address=address,password=password,img=img)
                sms.save()
                messages.success(request, 'data is inserted.')
                return redirect ('/addadmin')
        else:
            sms=smsadmin.objects.all()
            return render (request,'addadmin.html',{'sms':sms,'adm':adm})
    else:
        messages.warning(request, 'Please Login')
        return redirect ('/adminlogin')
def editadmin(request,id):
    adm=getadmin(request)
    if(adm):
        sms=smsadmin.objects.get(id=id)
        if (request.method=='POST'):
            name = request.POST.get("name")
            email = request.POST.get("email")
            phonenumber = request.POST.get("phonenumber")
            address = request.POST.get("address")
            img = request.FILES.get("img")
            sms.name=name
            sms.email=email
            sms.phonenumber=phonenumber
            sms.address=address
            sms.img=img 
            sms.save()
            messages.success(request,'User data is edited.')

            return redirect('/addadmin')
        else:
            return render(request,'editadmin.html',{'sms':sms,'adm':adm})   
    else:
        messages.warning(request, 'Please Login')
        return redirect ('/adminlogin')     
  

def deleteadmin(request,id):
    sms=smsadmin.objects.get(id=id)
    sms.delete()
    messages.success(request, 'User data deleted') 
    return redirect("/addadmin") 

def addcategory(request):
    adm=getadmin(request)
    if(adm):
        if request.method == "POST":
            categoryname = request.POST.get("category")
            categorynamecheck=smscategory.objects.filter(categoryname=categoryname)
            if(categorynamecheck):
                messages.warning(request, 'Category already exists.')
                return redirect ('/addcategory')
            else:
                sms=smscategory(categoryname=categoryname)
                sms.save()
                messages.success(request, 'Category is inserted.')
                return redirect ('/addcategory')
        else:
            sms=smscategory.objects.all()
            return render (request,'addcategory.html',{'sms':sms, 'adm':adm})
    else:
        messages.warning(request, 'Please Login')
        return redirect ('/adminlogin') 
def editcategory(request,id):
    adm=getadmin(request)
    if(adm):
        sms=smscategory.objects.get(id=id)
        if (request.method=='POST'):
            categoryname = request.POST.get("category")
            sms.categoryname=categoryname 
            sms.save()
            messages.success(request,'data is edited.')
            return redirect('/addcategory')
        else:
            return render(request,'editcategory.html',{'sms':sms, 'adm':adm})
    else:
        messages.warning(request, 'Please Login')
        return redirect ('/adminlogin') 
def deletecategory(request,id):
    sms=smscategory.objects.get(id=id)
    sms.delete()
    messages.success(request, 'category is deleted.')
    return redirect('/addcategory')  
     
def addsubcategory(request):
    adm=getadmin(request)
    if(adm):
        if request.method == "POST":
            categoryname = request.POST.get("category")
            subcategoryname = request.POST.get("subcategory")
            subcategorynamecheck=smssubcategory.objects.filter(subcategoryname=subcategoryname)
            if(subcategorynamecheck):
                messages.warning(request, 'Subcategory already exists.')
                return redirect ('/addsubcategory')
            else:
                sms=smssubcategory(categoryname=categoryname,subcategoryname=subcategoryname)
                sms.save()
                messages.success(request, 'subcategory is inserted.')
                return redirect ('/addsubcategory')
        else:
            sms=smssubcategory.objects.all()
            cat=smscategory.objects.all()
            return render (request,'addsubcategory.html',{'cat':cat,'sms':sms, 'adm':adm})
    else:
        messages.warning(request, 'Please Login')
        return redirect ('/adminlogin')  
def editsubcategory(request,id):
    adm=getadmin(request)
    if(adm):
        sms=smssubcategory.objects.get(id=id)
        if (request.method=='POST'):
            subcategoryname = request.POST.get("subcategory")
            sms.subcategoryname=subcategoryname 
            sms.save()
            messages.success(request,'data is edited.')
            return redirect('/addsubcategory')
        else:
            return render(request,'editsubcategory.html',{'sms':sms, 'adm':adm})
    else:
        messages.warning(request, 'Please Login')
        return redirect ('/adminlogin')   

def deletesubcategory(request,id):
    sms=smssubcategory.objects.get(id=id)
    sms.delete()
    messages.success(request, 'Subcategory is deleted.')
    return redirect('/addsubcategory')    

def addproduct(request):
    adm=getadmin(request)
    if(adm):
        if request.method == "POST":
            productname = request.POST.get("productname")
            category = request.POST.get("category")
            subcategory = request.POST.get("subcategory")
            mrp = request.POST.get("mrp")
            hsn = request.POST.get("hsn")
            color = request.POST.get("color")
            brand = request.POST.get("brand")
            warrenty = request.POST.get("warrenty")
            expiry = request.POST.get("expiry")
            description = request.POST.get("description")
            image = request.FILES.get("image")

            productcheck = smsproduct.objects.filter(productname=productname)
            if productcheck:
                messages.warning(request, 'Product already exists.')
                return redirect('/addproduct')
            else:
                sms = smsproduct(productname=productname,category=category,subcategory=subcategory, mrp=mrp, hsn=hsn,color=color,brand=brand,warrenty=warrenty,expiry=expiry,description=description,image=image)
                sms.save()
                messages.success(request, 'Product added ')
                return redirect('/addproduct')

        else:
            sms=smsproduct.objects.all()
            cat=smssubcategory.objects.all()
            subcat=smssubcategory.objects.all()
            return render (request,'addproduct.html',{'product':sms,'cat':cat,'subcat':subcat, 'adm':adm})
    else:
        messages.warning(request, 'Please Login')
        return redirect ('/adminlogin')   

def editproduct(request,id):
    adm=getadmin(request)
    if(adm):
        sms=smsproduct.objects.get(id=id)
        if (request.method=='POST'):
            productname = request.POST.get("productname")
            sms.productname=productname 
            sms.save()
            messages.success(request,'data is edited.')
            return redirect('/addproduct')
        else:
            return render(request,'editproduct.html',{'sms':sms, 'adm':adm}) 
    else:
        messages.warning(request, 'Please Login')
        return redirect ('/adminlogin')  

def deleteproduct(request,id):
    sms=smsproduct.objects.get(id=id)
    sms.delete()
    messages.success(request, 'Product is deleted.')
    return redirect('/addproduct') 
def addcustomer(request):
    adm=getadmin(request)
    if(adm):
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            phonenumber = request.POST.get('phonenumber')
            address = request.POST.get('address')
            customercheck = smscustomer.objects.filter(name=name)
            if customercheck:
                messages.warning(request, 'customer already exists.')
                return redirect('/addcustomer')
            else:
                sms = smscustomer(
                name=name,
                email=email,
                phonenumber=phonenumber,
                address=address)
                sms.save()
                messages.success(request, 'Add Custumer Details')
                return redirect('/addcustomer')

        else:
            sms=smscustomer.objects.all()
            return render (request,'addcustomer.html',{'sms':sms, 'adm':adm})
    else:
        messages.warning(request, 'Please Login')
        return redirect ('/adminlogin')

def editcustomer(request, id):
    adm=getadmin(request)
    if(adm):
        sms=smscustomer.objects.get(id=id)
        if (request.method == "POST"):
            name = request.POST.get("name")
            sms.name=name 
            sms.save()
            messages.success(request,'data is edited.')
            return redirect('/addcustomer')
        else:
            return render(request,'editcustomer.html',{'sms':sms, 'adm':adm})
    else:
        messages.warning(request, 'Please Login')
        return redirect ('/adminlogin')   
def deletecustomer(request, id):
    sms=smscustomer.objects.get(id=id)
    sms.delete()
    messages.success(request, 'customer is deleted.')
    return redirect('/addcustomer')

# ____________________________________Code of purchase____________________________________________

def purchase(request):
    adm=getadmin(request)
    if(adm):
        if request.method == "POST":
            b = str(time.time())
            billno=b.split('.')[0]
            sid = request.POST.get('supplier')
        # insert into accounts
            status = "purchase"
        
            accountcheck=smsaccounts.objects.filter(billno=billno)
            if(accountcheck):
                messages.warning(request, 'Account already exists.')
                return redirect('purchase/')
            else:
                sms=smsaccounts(status=status,billno=billno,customerid=sid,amount=0,date=timezone.now())
                messages.success(request, 'Select your product')
                sms.save()
                return redirect('/finalpurchase/'+billno)
        else:
            sms=smscustomer.objects.all()
            purchase=smsaccounts.objects.filter(status='purchase',amount=0)
            d={}
            for i in purchase:
                custid=i.customerid
                billno=i.billno
                date=i.date
                cust=smscustomer.objects.get(id=custid)
                d[billno]={'cust_name':cust.name,'date':date}
            return render(request,'purchase.html',{'sms':sms ,'purchase':d, 'adm':adm})
    else:
        messages.warning(request, 'Please Login')
        return redirect ('/adminlogin') 

      # _______________________________________Delete finapurchase_________________________
def deletepurchase(request,id,billno):
    sms=smstemppurchase.objects.get(id=id)
    sms.delete()
    messages.success(request, 'purchase is deleted.')
    return redirect('/finalpurchase/'+billno)
    
def finalpurchase(request,billno):
    adm=getadmin(request)
    if(adm):
        if request.method == "POST":
            productname = request.POST.get('productname')
            quantity = request.POST.get('quantity')
            price = request.POST.get('price')
        
            finalpurchasecheck=smstemppurchase.objects.filter(billno=billno,productname=productname)
            if(finalpurchasecheck):
                messages.warning(request, 'Product is already exists.')
                return redirect('/finalpurchase/'+billno)
            else:
            
                sms=smstemppurchase(billno=billno,productname=productname,quantity=quantity,price=price)
                sms.save()
                
                messages.success(request, 'Add another product')
                return redirect('/finalpurchase/'+billno)
        else:
            sms=smsproduct.objects.all()
            temp=smstemppurchase.objects.filter(billno=billno)
            return render(request,'finalpurchase.html',{'sms':sms,'billno':billno,'temp':temp, 'adm':adm})
    else:
        messages.warning(request, 'Please Login')
        return redirect ('/adminlogin') 

def purchasecomplete(request,billno):
        if request.method == "POST":
            purchasedetails=smstemppurchase.objects.filter(billno=billno)
            a=0
            for i in purchasedetails:
                productname=i.productname
                quantity=i.quantity
                price=i.price
                a=a+int(quantity)*int(price) #total amount
                sms=smsfinalpurchase(billno=billno,productname=productname,quantity=quantity,price=price)
                sms.save()
                productdetails=smsproduct.objects.get(productname=productname)
                category=productdetails.category
                subcategory=productdetails.subcategory
                stockcheck=stock.objects.filter(category=category,subcategory=subcategory,productname=productname)
                if(stockcheck):
                    stockdetails=stock.objects.get(category=category,subcategory=subcategory,productname=productname)
                    stockdetails.quantity=int(stockdetails.quantity)+int(quantity)
                    stockdetails.save()
                else:
                    stockdetails=stock(category=category,subcategory=subcategory,productname=productname,quantity=quantity)
                    stockdetails.save() 
                purchasedelete=smstemppurchase.objects.get(id=i.id)
                purchasedelete.delete()
                accountupdate=smsaccounts.objects.get(billno=billno)
                accountupdate.amount=a
                accountupdate.save()
            messages.warning(request, 'puchases completed')
            return redirect('/purchase')

        else:
            
            return redirect('/finalpurchase/'+billno)

# ______________________________________Code of Sale________________________________________________

def sale(request):
    adm=getadmin(request)
    if(adm):
        if request.method == "POST":
            b = str(time.time())
            billno=b.split('.')[0]
            sid = request.POST.get('supplier')
        # insert into accounts
            status = "sale"
        
            accountcheck=smsaccounts.objects.filter(billno=billno)
            if(accountcheck):
                messages.warning(request, 'Account already exists.')
                return redirect('sale/')
            else:
                sms=smsaccounts(status=status,billno=billno,customerid=sid,amount=0,date=timezone.now())
                messages.success(request, 'Select your product')
                sms.save()
                return redirect('/finalsale/'+billno)
        else:
            sms=smscustomer.objects.all()
            sale=smsaccounts.objects.filter(status='sale',amount=0)
            d={}
            for i in sale:
                custid=i.customerid
                billno=i.billno
                date=i.date
                cust=smscustomer.objects.get(id=custid)
                d[billno]={'cust_name':cust.name,'date':date}
            return render(request,'sale.html',{'sms':sms ,'sale':d, 'adm':adm})
    else:
        messages.warning(request, 'Please Login')
        return redirect ('/adminlogin') 
    
def finalsale(request,billno):
    adm=getadmin(request)
    if(adm):
        if request.method == "POST":
            productname = request.POST.get('productname')
            quantity = request.POST.get('quantity')
            price = request.POST.get('price')
        
            finalsalecheck=smstempsale.objects.filter(billno=billno,productname=productname)
            if(finalsalecheck):
                messages.warning(request, 'sale is already exists.')
                return redirect('/finalsale/'+billno)
            else:
            
                sms=smstempsale(billno=billno,productname=productname,quantity=quantity,price=price)
                sms.save()
                
                messages.success(request, 'Add another sale')
                return redirect('/finalsale/'+billno)
        else:
            sms=smsproduct.objects.all()
            temp=smstempsale.objects.filter(billno=billno)
            return render(request,'finalsale.html',{'sms':sms,'billno':billno,'temp':temp, 'adm':adm})
    else:
        messages.warning(request, 'Please Login')
        return redirect ('/adminlogin') 

def salecomplete(request,billno):
        if request.method == "POST":
            purchasedetails=smstempsale.objects.filter(billno=billno)
            a=0
            for i in purchasedetails:
                productname=i.productname
                quantity=i.quantity
                price=i.price
                a=a+int(quantity)*int(price) #total amount
                sms=smsfinalsale(billno=billno,productname=productname,quantity=quantity,price=price)
                sms.save()
                productdetails=smsproduct.objects.get(productname=productname)
                category=productdetails.category
                subcategory=productdetails.subcategory
                stockcheck=stock.objects.filter(category=category,subcategory=subcategory,productname=productname)
                if(stockcheck):
                    stockdetails=stock.objects.get(category=category,subcategory=subcategory,productname=productname)
                    stockdetails.quantity=int(stockdetails.quantity)-int(quantity)
                    stockdetails.save()
                else:
                    stockdetails=stock(category=category,subcategory=subcategory,productname=productname,quantity=quantity)
                    stockdetails.save() 
                saledelete=smstempsale.objects.get(id=i.id)
                saledelete.delete()
                accountupdate=smsaccounts.objects.get(billno=billno)
                accountupdate.amount=a
                accountupdate.save()
            messages.warning(request, 'sales completed')
            return redirect('/sale')

        else:
            
            return redirect('/finalsale/'+billno)
def deletesale(request,id,billno):
    sms=smstempsale.objects.get(id=id)
    sms.delete()
    messages.success(request, 'sale is deleted.')
    return redirect('/finalsale/'+billno)       

#_______________________________Stock___________________________________________

def allstock(request):
    adm=getadmin(request)
    if(adm):
        if request.method == "POST":
            productname = request.POST.get('productname')
            category = request.POST.get('category')
            subcategory = request.POST.get('subcategory')
            quantity = request.POST.get('quantity')
            sms = stock(productname=productname, category=category, subcategory=subcategory, quantity= quantity)
            sms.save()
            return redirect('/stock')
        else:
            sms=stock.objects.all()
            temp=stock.objects.all()
            return render (request,'allstock.html',{'temp':temp, 'adm':adm})
    else:
        messages.warning(request, 'Please Login')
        return redirect ('/adminlogin') 
def allpurchase(request):
    adm=getadmin(request)
    if(adm):
        acc=smsaccounts.objects.filter(status="purchase",amount__gt=0)
        d={}
        for i in acc:
            billno=i.billno
            custid=i.customerid
            fsales=smsfinalpurchase.objects.filter(billno=billno)
            pname=""                   
            tamt=0
            quantity=""
            price=""
            tprice=""

            for i in fsales:
                pname=pname+i.productname+"\n"
                quantity=quantity+i.quantity+"\n"
                price=price+i.price+"\n"
                tprice=tprice+str(int(i.price)*int(i.quantity))+"\n"
                tamt=tamt+int(i.price)*int(i.quantity)
            cus=smscustomer.objects.get(id=custid)
            d[billno]={'cust_name':cus.name,'address':cus.address,'phno':cus.phonenumber,'pname':pname,'quantity':quantity,'price':price,'totalprice':tprice,'tamt':tamt}
        return render (request,'allpurchase.html',{'temp':d, 'adm':adm})
    else:
        messages.warning(request, 'Please Login')
        return redirect ('/adminlogin')         

def deletetemppurchase(request,billno):
    sms1=smsaccounts.objects.filter(billno=billno)
    temp1=smstemppurchase.objects.filter(billno=billno) 
    if(sms1):
        sms=smsaccounts.objects.get(billno=billno)                    
        sms.delete()
    if(temp1):
        temp=smstemppurchase.objects.get(billno=billno) 
        temp.delete()
    messages.success(request, 'customer is deleted.')
    return redirect('/purchase')   
 
def deletetempsale(request,billno):
    sms1=smsaccounts.objects.filter(billno=billno)
    temp1=smstempsale.objects.filter(billno=billno) 
    if(sms1):
        sms=smsaccounts.objects.get(billno=billno)                    
        sms.delete()
    if(temp1):
        temp=smstempsale.objects.get(billno=billno) 
        temp.delete()
    messages.success(request, 'customer sale is deleted.')
    return redirect('/sale')    

def allsale(request):
    adm=getadmin(request)
    if(adm):
        acc=smsaccounts.objects.filter(status="sale",amount__gt=0)
        d={}
        for i in acc:
            billno=i.billno
            custid=i.customerid
            fsales=smsfinalsale.objects.filter(billno=billno)
            pname=""                    
            tamt=0
            quantity=""
            price=""
            tprice=""

            for i in fsales:
                pname=pname+i.productname+"\n"
                quantity=quantity+i.quantity+"\n"
                price=price+i.price+"\n"
                tprice=tprice+str(int(i.price)*int(i.quantity))+"\n"
                tamt=tamt+int(i.price)*int(i.quantity)
            cus=smscustomer.objects.get(id=custid)
            d[billno]={'cust_name':cus.name,'address':cus.address,'phno':cus.phonenumber,'pname':pname,'quantity':quantity,'price':price,'totalprice':tprice,'tamt':tamt}
        return render (request,'allsale.html',{'temp':d, 'adm':adm})
    else:
        messages.warning(request, 'Please Login')
        return redirect ('/adminlogin')         

def allaccount(request):
    adm=getadmin(request)
    if(adm):
        acc=smsaccounts.objects.filter(amount__gt=0,)
        d={}
        for i in acc:
            billno=i.billno
            custid=i.customerid
            ttype=i.status
            tamt=i.amount
            cus=smscustomer.objects.get(id=custid)
            d[billno]={'ttype':ttype,'address':cus.address,'cust_name':cus.name,'phno':cus.phonenumber,'tamt':tamt}
        return render (request,'allaccount.html',{'temp':d, 'adm':adm})
    else:
        messages.warning(request, 'Please Login')
        return redirect ('/adminlogin')     

def adminlogin(request):
    if request.session.has_key('aemail'):
        del request.session['aemail']
    if request.method == "POST":
        eid = request.POST.get('eid')
        pw = request.POST.get('pw')
        check=smsadmin.objects.filter(email=eid,password=pw)
        if(check):
            request.session['aemail']=eid
            messages.success(request, 'Login Successfull')
            return redirect('/dashboard')
        else:
            messages.warning(request, 'Login unSuccessfull')
            return redirect('/adminlogin')
    else:
        return render(request,'adminlogin.html')    
        
        
# Create your views here.