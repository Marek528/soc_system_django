from django.shortcuts import render
from . models import *

def vypis_tem(request):
    temy = Tema.objects.all().order_by('dostupnost')
    return render(request, 'soc/temy.html', {'temy': temy})

def vypis_ucitela(request, id):
    ucitel = Ucitel.objects.get(id=id)
    temy = Tema.objects.filter(konzultant=ucitel)
    return render(request, 'soc/ucitel.html', {'temy': temy, 'ucitel': ucitel})

def vypis_studenta(request, id):
    student = Student.objects.get(id=id)
    temy = Tema.objects.filter(student=student)
    return render(request, 'soc/student.html', {'temy': temy, 'student': student})

def vypis_temy(request, id):
    tema = Tema.objects.get(id=id)
    return render(request, 'soc/tema.html', {'tema': tema})