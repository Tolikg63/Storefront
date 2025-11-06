from django.shortcuts import render
from store.models import Customer


def index(request):
   customers = Customer.objects.all()[:30]
   return render(request, 'index.html', {'customers': list(customers)})