from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import NgoTable

def index(request):
    ngo_table_list = NgoTable.objects.order_by('id')[:5]
    context = {'ngo_table_list': ngo_table_list}
    return render(request, 'ngoTable/index.html', context)