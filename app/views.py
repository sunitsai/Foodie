from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from .models import *
from random import randint
from .utils import *
# Create your views here.
def IndexPage(request):
    return render(request,"app/index-2.html")

def LoginPage(request):
    return render(request,"app/login.html")

def LoginChefPage(request):
    return render(request,"app/loginchef.html")


def SingupPage(request):
    return render(request,"app/signup.html")


def SingupChefPage(request):
    return render(request,"app/signupchef.html")


def Showpage(request):
    return render(request,"app/show.html")

def ChefEditProfilePage(request):
    return render(request,"app/chef/edit-profile.html")

def ChefProduct_add(request):
    return render(request,"app/chef/product-add.html")

def CustomerShop_page(request):
    return render(request,"app/shop-page.html")

def Product_Page(request):
    return render(request,"app/chef/product.html")


def Insertdata(request):
        try:
            if request.POST['role']=="Customer":

               role = request.POST['role']
               email = request.POST['email']
               password = request.POST['pass']
               cpassword = request.POST['cpass']
               fname = request.POST['fname']
               lname = request.POST['lname']
               contact = request.POST['contact']
               
               
               

               user = User.objects.filter(Email=email)
               if user:
                    message = "Email  does not exist"
                    return render(request,"app/signup.html",{'msg':message})
               else:
                    if password==cpassword:
                        otp = randint(10000,99999)
                        newuser = User.objects.create(Email=email,Password=password,Otp=otp,Role=role)
                        newcust = Customer.objects.create(user_id=newuser,Firstname=fname,Lastname=lname,Contact=contact)
                        # email_subject = "food Finder : Customer Verification"
                        # sendmail(email_subject, 'mail_templates', email, {'name': fname, 'otp': otp,})
                             
                        return render(request,"app/login.html")
                    else:
                        message = "Password and confirm password does not match"
                        return render(request,"app/signup.html",{'msg':message})
            else:
                if request.POST['role']=="Chef":

                   role = request.POST['role']
                   email = request.POST['email']
                   password = request.POST['pass']
                   cpassword = request.POST['cpass']
                   fname = request.POST['fname']
                   lname = request.POST['lname']
                   contact = request.POST['contact']
                   
                   
               

                   user = User.objects.filter(Email=email)
                   if user:
                        message = "Email  does not exist"
                        return render(request,"app/index.html",{'msg':message})
                   else:
                        if password==cpassword:
                            otp = randint(10000,99999)
                            newuser = User.objects.create(Email=email,Password=password,Otp=otp,Role=role)
                            newchef = Chef.objects.create(user_id=newuser,Firstname=fname,Lastname=lname,Contact=contact)
                            email_subject = "food Finder : Chef Verification"
                            sendmail(email_subject, 'mail_templates', email, {'name': fname, 'otp': otp,})
                            return HttpResponseRedirect(reverse('loginchef'))
                        else:
                            message = "Password and confirm password does not match"
                            return render(request,"app/index.html",{'msg':message})
               

        except Exception as e:
                    print("registration exception----->",e)


def LoginUser(request):
    try:
        if request.POST['role']=="Customer":
                print("==========1==========")
                email = request.POST['email']
                password = request.POST['password']

                user = User.objects.get(Email=email)
                if user:
                    print("=======2=======")
                    try:
                        if user.Password==password and user.Role=="Customer":
                            print("=======3=======")
                            cust = Customer.objects.filter(user_id=user)
                            request.session['Firstname'] = cust[0].Firstname
                            request.session['Email'] = user.Email
                            request.session['Role'] = user.Role
                            request.session['id'] = user.id
                            return render(request,"app/index.html")
                            print("==========4============")
                        else:
                            message = "Password Does not match"
                            return render(request,"app/login.html",{'msg':message})
                    except Exception as e4:
                        print("Customer Login Exception----------->",e4)
                    
                else:
                    message = " User Does not match"
                    return render(request,"app/login.html",{'msg':message})
        else:
            if request.POST['role']=="Chef":
                print("=========5=========")
                email = request.POST['email']
                password = request.POST['password']

                user = User.objects.get(Email=email)
                if user:
                    print("========6========")
                    try:
                        if user.Password==password and user.Role=="Chef":
                            print("==========7========")
                            chef = Chef.objects.filter(user_id=user)
                            request.session['Firstname'] = chef[0].Firstname
                            request.session['Lastname'] = chef[0].Lastname
                            request.session['Email'] = user.Email
                            request.session['Role'] = user.Role
                            request.session['id'] = user.id
                            return render(request,"app/chef/index.html")

                            print("=============8===========")
                        else:
                            message = "Password Does not match"
                            return render(request,"app/login.html",{'msg':message})
                    except Exception as e5:
                        print("Exception Chef------------->",e5)


                        
                    
                else:
                    message = " User Does not match"
                    return render(request,"app/login.html",{'msg':message})

            else:
                print("no user found")
    except Exception as e3:
        print("Login Exception ------->",e3)

def DisplayData(request,pk):
    all_data = Customer.objects.get(pk=pk)
    return render(request,"app/show.html",{'key1':all_data})


def EditPage(request,pk):
    if 'Email' in request.session and 'Role' in request.session:
        if request.session['Role'] == "Customer":
            cust = Customer.objects.get(pk=pk)
            return render(request,"app/customeredit.html",{'key1':cust})
        
           
       



def ChefAlldata(request,pk):
    if 'Email' in request.session and 'Role' in request.session:
        if request.session['Role'] == "Chef":
            chef = Chef.objects.get(pk=pk)
            print("Chef--------------->",chef)
            return render(request,"app/chef/edit-profile.html",{'key2':chef})



def UpdateData(request,pk):
    if request.session['Role'] == "Customer":
        udata = Customer.objects.get(pk=pk)
        udata.Firstname = request.POST['fname']
        udata.Lastname = request.POST['lname']
        udata.Email = request.POST['email']
        udata.Contact = request.POST['contact']
        udata.City = request.POST['city']
        udata.State = request.POST['state']
        udata.Address = request.POST['address']
        
        udata.save()
        return HttpResponseRedirect(reverse('edit'))

    else:
        if request.session['Role'] == "Chef":
            cdata = Chef.objects.get(pk=pk)
            cdata.Firstname = request.POST['fname']
            cdata.Lastname = request.POST['lname']
            cdata.Email = request.POST['email']
            cdata.Contact = request.POST['contact']
            cdata.City = request.POST['city']
            cdata.State = request.POST['state']
            cdata.Address = request.POST['address']
            cdata.Ability = request.POST['Ability']
            cdata.Gender = request.POST['gender']

            cdata.save()
            return HttpResponseRedirect(reverse('edit'))

def Addproduct(request,pk):
    udata = User.objects.get(id=pk)
    if udata.Role == "Chef":

        chef_id = Chef.objects.get(user_id=udata)
        print("Chef_id-------------->",chef_id)
        productname = request.POST['Productname']
        Expirydate = request.POST['Expirydate']
        Mfgdate = request.POST['Mfgdate']
        Category = request.POST['Category']
        Price = request.POST['Price']
        Discount = request.POST['discount']
        ProductDescription = request.POST['ProductDescription']
        Detail = request.POST['Detail']
        Status = request.POST['Status']
        img = request.FILES['Image']
        Keyword = request.POST['Keyword']

        newproduct = Product.objects.create(chef_id=chef_id,Productname=productname,Expirydate=Expirydate,Mfgdate=Mfgdate,Category=Category,Price=Price,discount=Discount,ProductDescription=ProductDescription,Detail=Detail,Status=Status,Image=img,Keywords=Keyword)
        message = "Product Add Success"
        return render(request,"app/chef/product-add.html",{'msg':message})



def ShowProduct(request):
    print("--------------ShowProduct---------------")
    all_pro = Product.objects.all()
   
    return render(request,"app/shop-page.html",{'key3':all_pro})
   


def ProductDescription(request,pk):
    pro = Product.objects.get(pk=pk)
    print("Product----------------------->",pro)
    return render(request,"app/shop-single.html",{'key4':pro})



def ShopSinglePage(request):
    return render(request,"app/shop-single.html")


def ChefShowProduct_Page(request,pk):
    print("--------------ShowProductPage---------------")
    pdata = User.objects.get(id=pk)
    if pdata.Role == "Chef":
        page_id = Chef.objects.get(user_id=pdata)
        pro = Product.objects.all().filter(chef_id=page_id)
        return render(request,"app/chef/product.html",{'key5':pro})



def EditProduct(request,pk):
    pdata = Product.objects.get(pk=pk)
    return render(request,"app/chef/productEdit.html",{'key6':pdata})
    


h

# def UpdateProduct(request,pk):
#     udata = User.objects.get(id=pk)
#     if udata.Role=="Chef":
#         chef = Chef.objects.get(user_id=udata)
#         pdata = Product.objects.filter(chef_id=chef)
#         print("=========PDATA==========",pdata)
#         pdata.Productname = request.POST['Productname']
#         pdata.ProductDescription = request.POST['ProductDescription']
#         pdata.Price = request.POST['Price']
#         pdata.Expirydate = request.POST['Expirydate']
#         pdata.Mfgdate = request.POST['Mfgdate']
#         pdata.Detail = request.POST['Detail']
#         pdata.Status = request.POST['Status']
#         pdata.Keywords = request.POST['Keyword']
#         pdata.save()
#         url =f"/chefshowproductpage/{pk}"
#         return HttpResponseRedirect(reverse(url))