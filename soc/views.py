from django.shortcuts import render
from . models import *

def vypis_tem(request):
    temy = Tema.objects.all().order_by('dostupnost', 'id')
    ucitelia = Ucitel.objects.all()
    odbory = Odbor.objects.all()
    dostupnosti = Dostupnost.objects.all()
    return render(request, 'soc/index.html', {'temy': temy, "ucitelia":ucitelia, "odbory":odbory, "dostupnosti":dostupnosti})

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
    return render(request, 'soc/temy.html', {'temy': temy})

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
    # 3. ci uz ziak nema ine prace/temy
    if (request.method == "GET"):
        return render(request, 'soc/add_tema.html', {"studenti":studenti, "ucitelia":ucitelia, "odbory":odbory, "dostupnosti":dostupnosti})
    else:
        konzultant = request.POST['konzultant']
        odbor = request.POST['odbor']
        dostupnost = request.POST['dostupnost']
        student = request.POST['student']

        if konzultant == "----------------------" or odbor == "----------------------" or dostupnost == "----------------------" or student == "----------------------":
            return render(request, 'soc/add_tema.html', {"studenti": studenti, "ucitelia": ucitelia, "odbory": odbory, "dostupnosti": dostupnosti, "message": "Prosím vyplňte všetky polia!"})
        
        if student == "-":
            dostupnost = Dostupnost.objects.get(nazov='voľné')
            pocet_kontrol = 0
            student = None
            tema = Tema(
                nazov = request.POST['nazov'],
                popis = request.POST['popis'],
                konzultant = Ucitel.objects.get(id=konzultant),
                student = None,
                odbor = Odbor.objects.get(id=odbor),
                dostupnost = Dostupnost.objects.get(id=dostupnost.id),
                pocet_kontrol = request.POST['pocet_kontrol']
            )
        else:
            existing_tema = Tema.objects.filter(student=student).exists()
            if existing_tema:
                return render(request, 'soc/add_tema.html', {"studenti": studenti, "ucitelia": ucitelia, "odbory": odbory, "dostupnosti": dostupnosti, "message": "Študent už má zadanú tému!"})
            else:
                tema = Tema(
                    nazov = request.POST['nazov'],
                    popis = request.POST['popis'],
                    konzultant = Ucitel.objects.get(id=konzultant),
                    student = Student.objects.get(id=student),
                    odbor = Odbor.objects.get(id=odbor),
                    dostupnost = Dostupnost.objects.get(id=dostupnost),
                    pocet_kontrol = request.POST['pocet_kontrol']
                )
        
        tema.save()
        return render(request, 'soc/add_tema.html', {"studenti": studenti, "ucitelia": ucitelia, "odbory": odbory, "dostupnosti": dostupnosti, "message": "Téma bola úspešne pridaná!"})