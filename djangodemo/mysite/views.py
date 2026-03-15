from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


from django.shortcuts import render,redirect
from .forms import ContactForm 
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("messages")
        form_full_name = form.cleaned_data.get("full_name")
        subject = "Site contact form"
        from_email = settings.EMAIL_HOST_USER
        to_email = [form_email]

        contact_messages = "%s: %s via %s" % (
            form_full_name,
            form_message,
            form_email
        )
        try:
            send_mail(subject,contact_messages,from_email,to_email)
        except BadHeaderError:
            return HttpResponse("Invalid header found..")
        return redirect("success")

    context = {
        "form" : form,
    }
    return render(request,"forms.html", context)

def success(request):
    return render(request,'success.html')