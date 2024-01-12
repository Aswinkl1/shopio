from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from item.models import item
# Create your views here.

@login_required
def dashboard(request):
    my_items = item.objects.filter(created_by = request.user)
    print(my_items)
    return render(request,'dashboard/index.html',{'items':my_items})




