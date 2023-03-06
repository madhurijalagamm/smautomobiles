from django.shortcuts import render
from dashboard.models import INVESTIGATOR


sno=''
name=''
regid=''
branch=''
email=''
mobile=''

def dashboardaction(request):
    if request.method == 'POST':
         regid=request.POST['regid']
         print(regid)
         user = INVESTIGATOR(sno=request.POST['sno'], name=request.POST['name'],regid=request.POST['regid'],branch=request.POST['branch'],email=request.POST['email'],mobile=request.POST['mobile'])
         user.save()
    data = INVESTIGATOR.objects.all()
    print(data[0].sno)
    return render(request, 'dashboard.html', {'data': data})


# def create_record(request):
#     if request.method == 'POST':
#         user = INVESTIGATOR(sno=request.POST['sno'],name=request.POST['name'],regid=request.POST['regid'],branch=request.POST['branch'],email=request.POST['email'],mobile=request.POST['mobile'])
#         user.save()
#         print(user)
#     return render(request, 'dashbaord.html')
    