# decorator for customer session (authentication)
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

#this decorator is to block user activites before login
def auth_customer(func):
    def wrapper(request, *args, **kwargs):
        if 'customer' in request.session: # 'customer' is the session key name of customer
            return func(request, *args, **kwargs)
        else:
            return redirect('common:customerlogin') 
    return wrapper # import this function in customer views
