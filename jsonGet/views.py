import json
from .models import StockM
#from django.forms.models import model_to_dict
from django.http import HttpResponse
#from django.shortcuts import get_object_or_404, redirect, direct_to_template

#from threading import Thread
#from time import sleep

'''counter = 1
def timedModelUpdate():
    global counter
    if(counter == 1):
        counter = 0
    i = 0
    while(1):
        pk = "adas"+i
        s = StockN(item=pk,price="1",volume="2",time="3:06")
        s.save()
        sleep(2)
        i = i+1
'''

# Create your views here.

'''def my_view(request, id):
    instance = get_object_or_404(StockN, id=id)
    form = MyForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('next_view')
    return direct_to_template(request, 'my_template.html', {'form': form})'''



def postJSON(request):
    if request.method=='POST':
            #received_json_data = json.loads(request.body)
            #s = StockM(received_json_data)
            s = StockM()
            s.setValues(json.loads(request.body))
            s.save()
            return HttpResponse("data saved", content_type="application/json")
    else:
        return HttpResponse("send via POst with json object as body", content_type="application/json")


flag = 1
def index(request):
    global flag
    if(flag == 1):
        d = {"item":"ramseed","price":"1111","volume":"453","time":"12:50"}
        d = json.dumps(d)
        ls = StockM()
        ls.setValues(d)
        ls.save()
        flag = 0
    ls = StockM.objects.all()
    results = [ob.as_json() for ob in ls]
    '''s = ""
    for l in ls:
        dict_obj = model_to_dict(l)
        s = s + str(dict_obj) + ","
    s = s[:len(s)-1]
    s = json.loads(s)'''
    if(ls):
        return HttpResponse(json.dumps(results), content_type="application/json")
    else:
        return HttpResponse(json.dumps("none"), content_type="application/json")