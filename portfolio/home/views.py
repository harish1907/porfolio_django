from django.shortcuts import render
from datetime import date, datetime
from django.contrib import messages
from home.models import Company, Viewer
import smtplib

# Create your views here.
MY_EMAIL = "harishchaudhary0129@gmail.com"
PASSWORD = "fqccdufsdzdcqemv"

# send email using smtplib..
def send_email(msg, subject="Someone is in your website contact page."):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:{subject}\n\n {msg}"
                            )


context = {
    'year': datetime.now().year
}
date = datetime.today().date()


def home(request):
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html', context)


def skills(request):
    return render(request, 'skills.html', context)


def hire(request):
    try:
        if request.method == "POST":
            name = request.POST.get("c-name")
            email = request.POST.get("c-email")
            ctc = request.POST.get("c-ctc")
            message = request.POST.get("c-message")

            if name and email and message and ctc:
                current_company = f"Company name: {name}\nCompany email: {email}\nCompany CTC: {ctc}\nCompany message: {message}"
                send_email(current_company, "Company want to hire you.")
                messages.success(request, "Your detail send successfully.")
                Company(name=name, email=email, ctc=ctc, message=message, date=date).save()
                
            else:
                messages.error(request, "Don't leave any boxes blank.")
    except:
        return render(request, 'hire.html', context)

    return render(request, "hire.html", context)


def contact(request):
    try:
        
        # fetch all emails
        viwer_email = [view.email for view in Viewer.objects.all()]
        
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")
            
            if email in viwer_email:
                messages.error(request, "This email already exist.")

            elif name and email and message:
                messages.success(request, "Your details send successfully.")
                message_email = f"name: {name}\nemail: {email}\nmessage: {message}"
                send_email(message_email)
                Viewer(name=name, email=email, message=message, date=date).save()

            else:
                messages.error(request, "don't leave any boxes empty.")
    except:
        return render(request, 'contact.html', context)

    return render(request, 'contact.html', context)