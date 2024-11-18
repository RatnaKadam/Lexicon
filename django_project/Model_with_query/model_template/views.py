from django.shortcuts import render
from django.http import HttpResponse
from model_template.models import Topic,AccessRecord,Webpage

# Create your views here.
def hello_view(request):
    webpages_list = AccessRecord.objects.order_by("date")
    data_dict = {"access_records":webpages_list}
    return render(request, 'index.html',context=data_dict)
