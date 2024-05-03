from django.shortcuts import redirect
from functools import wraps
from .models import Freelancer
from django.contrib import messages

def freelancer_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return redirect("/auth/login/")
        
        # Check if the Freelancer object exists for the user
        try:
            freelancer = Freelancer.objects.get(email=request.user.email)
        except Freelancer.DoesNotExist:
            messages.warning(request, "You do not have access to client opportunities. Register Now!")
            return redirect("freelancing")  
        
        # If Freelancer object exists, execute the original view function
        return view_func(request, *args, **kwargs)
    
    return _wrapped_view
