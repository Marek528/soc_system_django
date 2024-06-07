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

def vypis_tem_samostatne(request):
    temy = Tema.objects.all().order_by('dostupnost', 'id')
    return render(request, 'soc/temy_samostatne.html', {'temy': temy})

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

def pridat_temu(request):
    studenti = Student.objects.all()
    ucitelia = Ucitel.objects.all()
    odbory = Odbor.objects.all()
    dostupnosti = Dostupnost.objects.all()

    # kontroly, ktore treba osetrit:
    # 1. ci je konzultant + odbor + dostupnost vybrane
    # 2. ak je student zvoleny ako -, v tom pripade skontrolovat ci je dostupnost zadana ako volne a pocet kontrol je 0
    # 3. ci uz ziak nema ine prace/temy (da sa to osetrit rovno aj tu -> bude to asi lepsie)
    if (request.method == "GET"):
        return render(request, 'soc/add_tema.html', {"studenti":studenti, "ucitelia":ucitelia, "odbory":odbory, "dostupnosti":dostupnosti})
    else:
        return