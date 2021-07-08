from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Sermon


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
    sermons = Sermon.objects.order_by('-date_made')[1:4]
    sermon2 = Sermon.objects.order_by('-date_made')[4:5]
    sermon3 = Sermon.objects.order_by('-date_made')[5:6]
    sermon5 = Sermon.objects.order_by('-date_made')[6:10]
    sermon6 = Sermon.objects.order_by('-date_made')[10:14]

    context = {'sermon': sermon, 'sermons': sermons, 'sermon2': sermon2, 'sermon3': sermon3, 'sermon5':sermon5,'sermon6':sermon6}
    return render(request, 'index.html', context)


def aboutUs(request):
    return render(request, 'aboutus.html')


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


@user_passes_test(lambda user: user.is_staff)
def staff_place(request):
    return HttpResponse("Employees must wash hands", content_type="text/plain")
