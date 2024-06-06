from django.shortcuts import render
from . models import *

def vypis_tem(request):
    temy = Tema.objects.all().order_by('dostupnost', 'id')
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

def statistiky(request):
    pocet_ucitelov = Ucitel.objects.count()
    pocet_studentov = Student.objects.count()
    pocet_tem = Tema.objects.count()

    pocet_volnych = Tema.objects.filter(dostupnost__nazov='voľné').count()
    pocet_obsadenych = Tema.objects.filter(dostupnost__nazov='obsadené').count()
    pocet_cakajucich = Tema.objects.filter(dostupnost__nazov='čakajúce na schválenie').count()
    return render(request, 'soc/statistiky.html', {'pocet_ucitelov': pocet_ucitelov, 'pocet_studentov': pocet_studentov, 'pocet_tem': pocet_tem,
                                                  'pocet_volnych': pocet_volnych, 'pocet_obsadenych': pocet_obsadenych, 'pocet_cakajucich': pocet_cakajucich})