from django.shortcuts import render
from medicine.models import MEDICINE


def medicineaction(request):
    if request.method == 'POST':
        #  regid=request.POST['regid']
        #  print(regid)
         user = MEDICINE(quantity=request.POST['quantity'], name=request.POST['name'],price=request.POST['price'],store=request.POST['store'],instock=request.POST['instock'])
         user.save()
    
    user = MEDICINE(quantity= 5, name='crocin', price=100, store = 'hyd', instock = True, incart = False)
    user.save()
    data = MEDICINE.objects.all()

    print(data[0].name)
    return render(request, 'medicine.html', {'data': data})