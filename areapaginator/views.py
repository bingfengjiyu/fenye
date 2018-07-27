from django.http import HttpResponse
from django.shortcuts import render
from areapaginator.models import BooktestAreainfo
from django.core.paginator import Paginator
# Create your views here.


def area(request,pindex):
    areas = BooktestAreainfo.objects.filter(aparent__isnull=True)
    pageinfo=Paginator(areas,10)
    if pindex=="":
        pindex=1
    else:
        pindex=int(pindex)
    print (pindex)
    page=pageinfo.page(pindex)
    return render(request, "areapaginator/area.html", {"page":page,"pageinfo":pageinfo})




def session_set(request):
    request.session['name'] = 'itheima'
    return HttpResponse('ok')


def session_get(request):
    name = request.session['name']
    return HttpResponse(name)


