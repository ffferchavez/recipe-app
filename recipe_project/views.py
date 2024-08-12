from django.shortcuts import render, redirect  
# Django authentication libraries           
from django.contrib.auth import authenticate, login, logout  # Added logout import
# Django Form for authentication
from django.contrib.auth.forms import AuthenticationForm    

#define a function view called login_view that takes a request from user
def login_view(request):
    # Initialize error_message to None                                 
    error_message = None   
    # Form object with username and password fields                             
    form = AuthenticationForm()

    # When user hits "login" button, then POST request is generated
    if request.method == 'POST':       
        # Read the data sent by the form via POST request                   
        form = AuthenticationForm(data=request.POST)

        # Check if form is valid
        if form.is_valid():                                
            username = form.cleaned_data.get('username')  # Read username
            password = form.cleaned_data.get('password')  # Read password

            # Use Django authenticate function to validate the user
            user = authenticate(username=username, password=password)
            if user is not None:  # If user is authenticated
                # Use pre-defined Django function to login
                login(request, user)                
                return redirect('/')  # Redirect to desired page
        else:  # In case of error
            error_message = 'ooops.. something went wrong'  # Print error message

    # Prepare data to send from view to template
    context = {                                             
        'form': form,  # Send the form data
        'error_message': error_message  # And the error_message
    }
    # Load the login page using "context" information
    return render(request, 'auth/login.html', context)

# Define a function view called logout_view that takes a request from user
def logout_view(request):
    logout(request)
    return render(request, 'auth/success.html')
