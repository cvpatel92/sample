from django.shortcuts import render
from models import Info
import datetime as dt
# Create your views here.
import pdb
import json
from .models import Info
import datetime

def get_time_intrevals(request):    
     
#     for i in range(1,15):
#         info = Info(
#                     Process_ID = 2,
#                     start_time = str(datetime.timedelta(seconds=3600)),
#                     end_time = str(datetime.timedelta(seconds=72000))
#                     )
#         info.save()
       
    info=Info.objects.all()
    chart_type = 'pie'
    if request.method == "POST":
        chart_type = request.POST.get('select_chart','')
    print chart_type
    res=[]
    print chart_type
    data1 = []
    data  = []
    for i in info:
        d = []
#         print str(i.start_time).strip()
        start_time=str(i.start_time).strip()
        end_time=str(i.end_time).strip()
        start_dt = dt.datetime.strptime(start_time, '%H:%M:%S')
        end_dt = dt.datetime.strptime(end_time, '%H:%M:%S')
        diff = (end_dt - start_dt)
        total= diff.seconds/60
        data.append(total)
        data1.append(i.id)
        d.append(i.id)
        d.append(total)
        res.append(d)
    return render(request,'show.html',locals())
        
