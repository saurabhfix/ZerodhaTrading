from django.shortcuts import render, redirect
from .form import ContactForm, ArithmeticForm

from kiteconnect import KiteConnect

# Create your views here.

# This is the home page view function
def home_view(request):
    global kite
    kite= KiteConnect(api_key="3onztsky2v4h5t7q")
    print(kite.login_url())
    return render(request, 'home.html')

# Define the contact_view function to handle the contact form
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            global enteredtoken
            # enteredtoken = request.POST.get('auth_token', '')
            enteredtoken = form.cleaned_data.get('auth_token')
            # accesstoken ->
            return redirect('contact-success')
    else:
        form = ContactForm()
    context = {'form':form}
    return render(request, 'auth.html', context)

# Define the contact_success_view function to handle the success page
def contact_success_view(request):
    data = kite.generate_session(enteredtoken, api_secret="3zweqs83tkvbkblss7k9r7zj5j524ospdw")
    kite.set_access_token(data["access_token"])

    kite.orders()

    print( kite.orders()+"contact - suceess ")
    return render(request, 'contact_success.html' )

def calculate_view(request):
    result = None
    form = ArithmeticForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        number1 = form.cleaned_data.get('number1')
        number2 = form.cleaned_data.get('number2')
        operation = form.cleaned_data.get('operation')

        if operation == 'add':
            result = number1 + number2
        elif operation == 'subtract':
            result = number1 - number2
        elif operation == 'multiply':
            result = number1 * number2
        elif operation == 'divide':
            try:
                result = number1 / number2
            except ZeroDivisionError:
                result = "Error! Division by zero."

    context = {
        'form': form,
        'result': result,
    }
    return render(request, 'calculate.html', context)
