from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .forms import ContactForm
from .models import Sermon
from django.conf import settings


def see_request(request):
    text = f"""
        Some attributes of the HttpRequest object:

        scheme: {request.scheme}
        path:   {request.path}
        method: {request.method}
        GET:    {request.GET}
        user:   {request.user}
    """

    return HttpResponse(text, content_type="text/plain")


def user_info(request):
    text = f"""
        Selected HttpRequest.user attributes:

        username:     {request.user.username}
        is_anonymous: {request.user.is_anonymous}
        is_staff:     {request.user.is_staff}
        is_superuser: {request.user.is_superuser}
        is_active:    {request.user.is_active}
    """

    return HttpResponse(text, content_type="text/plain")


@login_required
def private_place(request):
    return HttpResponse("Shhh, members only!", content_type="text/plain")


def DashBoard(request):
    sermon = Sermon.objects.order_by('date_made').last()
    sermon2 = Sermon.objects.order_by('-date_made')[1:2]
    sermon3 = Sermon.objects.order_by('-date_made')[2:3]
    sermon4 = Sermon.objects.order_by('-date_made')[3:4]
    sermon5 = Sermon.objects.order_by('-date_made')[4:5]
    sermon6 = Sermon.objects.order_by('-date_made')[5:11]

    form = ContactForm(request.POST)
    if form.is_valid():
        subject = 'Berea Website subscription'
        message = 'Hey,  We have a new member' + form.instance.email + ''
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['agtumusiime@gmail.com', ]
        send_mail(subject, message, email_from, recipient_list)

        form.save()
    else:
        form = ContactForm()

    context = {'form': form, 'sermon': sermon, 'sermon2': sermon2, 'sermon3': sermon3, 'sermon4': sermon4,
               'sermon5': sermon5,
               'sermon6': sermon6}
    return render(request, 'index.html', context)


def aboutUs(request):
    return render(request, 'aboutus.html')


def fellowship(request):
    return render(request, 'fellowship.html')


def listing(request):
    data = {
        "sermons": Sermon.objects.all(),
    }

    return render(request, "listing.html", data)


def view_sermon(request, sermon_id):
    sermon = get_object_or_404(Sermon, id=sermon_id)
    data = {
        "sermons": sermon,
    }

    return render(request, "view_sermon.html", data)


def Sermon_detail(request, id):
    sermon = Sermon.objects.get(id=id)
    context = {'sermon': sermon}
    return render(request, 'sermon_detail.html', context)


def Subscribe(request):
    form = ContactForm(request.POST)
    print('We are here 1')
    if form.is_valid():
        form.save()
        print('We are here 2')
    else:
        print('We are here 3')
        form = ContactForm()

    context = {'form': form}

    return render(request, 'index.html', context)


@user_passes_test(lambda user: user.is_staff)
def staff_place(request):
    return HttpResponse("Employees must wash hands", content_type="text/plain")
