from django.shortcuts import render, redirect
from .models import Customer,Seller
import random
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse

# Create your views here.
def project_home(request):
    return render(request, 'common/project_home.html')

def customer_login(request):
    msg = ''
    if request.method == 'POST':
        customer_email = request.POST['customer_email']
        customer_password = request.POST['customer_password']
        
        try:
            customer = Customer.objects.get(customer_email = customer_email, customer_password = customer_password)
            request.session['customer'] = customer.id
            return redirect('customer:customerhome') 
        except:
            msg = 'Incorrect email-id or password'
    return render(request, 'common/customer_login.html',{'msg':msg})

def seller_login(request):
    msg = ''
    if request.method == 'POST':
        seller_username = request.POST['username']
        seller_password = request.POST['password']

        # select * from seller sellerusername = sellerusername and password = password
        try:
            seller = Seller.objects.get(seller_username = seller_username, seller_password = seller_password)


            # if username and password is correct, we set a session variable with key 'seller'
            # session variable can be accessed throughout the application

            # working of django session:
            # when username and password is correct, we set a session variable with key (here key is 'seller') and
            # unique value for each seller (here value is the primary key of the logged seller)
            # if a seller with primary key 2 logs in,  session key will be 'selle' and value will be 2

            # when we set a session, key and value will be stored in django_session table inside database in encrypted format.
            # and the encrypted key will be send with http response to the client(browser)

            # in the client side(browser), the key received from the server will be stored in the browser storage(cookies)
            # when the user request any page (eg: cart page) from the same browser, the same key stored inside cookies will be
            # sending to the server through http request

            #when the request reaches the server, it wil look for the key stored in cookie to match with django_session thable inside
            # the database to find the corresponding user.


            request.session['seller'] = seller.id 
            return redirect('seller:sellerhome')
        except:
            msg = 'Incorrect username or password' # it calls in the html
    return render(request, 'common/seller_login.html',{'msg':msg})

def customer_registration(request):

    if request.method == 'POST': # works when button clicks
        cst_name = request.POST['cust_name'] #here we get data input in textbox, cust_name is the name of inputbox
        cst_email = request.POST['cust_email']
        cst_phone = request.POST['cust_phone']
        cst_address = request.POST['cust_address']
        cst_gender = request.POST['cust_gender']
        cst_password = request.POST['cust_password']
        cst_image = request.FILES['customer_image']
        # to  insert data into table
        #1. create object of model class, eg: Customer

        new_customer = Customer(customer_name = cst_name, 
         customer_email = cst_email,
         customer_phone = cst_phone,
         customer_address = cst_address,
         customer_gender = cst_gender, 
         customer_password = cst_password,
         customer_image = cst_image)

        # call save() method, here save() method is equivalent to insert into sql query
        new_customer.save()
    return render(request, 'common/customer_reg.html')

def seller_registration(request):
    if request.method == 'POST':
        seller_name = request.POST['seller_name']
        seller_email = request.POST['seller_email']
        seller_phone = request.POST['seller_phone']
        seller_address = request.POST['seller_address']
        company_name = request.POST['company_name']
        seller_acc_holdername = request.POST['acc_holde_name']
        seller_ifsc = request.POST['ifsc']
        seller_branch = request.POST['branch']
        seller_acc_number = request.POST['acc_number']
        seller_image = request.FILES['seller_image']
        seller_username = random.randint(1111,9999)
        seller_password = 'sel-' + seller_name.lower() + str(seller_username)
        message = 'hi, your user name is ' + str(seller_username) + 'and temporary password is ' + seller_password

        send_mail(
            'username and temporary password',
            message,
            settings.EMAIL_HOST_USER,
            [seller_email,],
            fail_silently=False
        )
        new_seller = Seller(seller_name=seller_name,seller_email=seller_email,
            seller_phone=seller_phone,seller_address=seller_address,
            company_name=company_name,acc_holdername=seller_acc_holdername,
            ifsc=seller_ifsc,branch=seller_branch,acc_number=seller_acc_number,
            seller_username=seller_username,seller_password=seller_password,
            seller_pic=seller_image)

        new_seller.save()
    return render(request, 'common/seller_reg.html')

def email_exist(request):
    email = request.POST['email'] # here 'email' is the key inside Json

    status = Customer.objects.filter(customer_email = email).exists()

    return JsonResponse({'status':status}) # the rquest and response both are in Json format.