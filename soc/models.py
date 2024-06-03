from django.db import models
# dorobit class Meta

class Ucitel(models.Model):
    meno = models.CharField(max_length=30)
    priezvisko = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    heslo = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.meno} {self.priezvisko}'


class Student(models.Model):
    meno = models.CharField(max_length=30)
    priezvisko = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    heslo = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.meno} {self.priezvisko}'

class Odbor(models.Model):
    nazov = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nazov}'


class Dostupnost(models.Model):
    nazov = models.CharField(max_length=70)

    def __str__(self):
        return f'{self.nazov}'

class Tema(models.Model):
    nazov = models.CharField(max_length=100)
    popis = models.TextField()
    konzultant = models.ForeignKey(Ucitel, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    odbor = models.ForeignKey(Odbor, on_delete=models.CASCADE)
    dostupnost = models.ForeignKey(Dostupnost, on_delete=models.CASCADE)
    pocet_kontrol = models.IntegerField()

    def __str__(self):
        return f'{self.nazov}, {self.popis}, {self.konzultant}, {self.student}, {self.odbor}, {self.dostupnost}, {self.pocet_kontrol}'