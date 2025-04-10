from django.db import models

class Vehicle(models.Model):
    spz = models.CharField(max_length=10, unique=True, verbose_name="SPZ")
    znacka = models.CharField(max_length=50, verbose_name="Značka")
    model = models.CharField(max_length=50, verbose_name="Model")
    rok_vyroby = models.IntegerField(verbose_name="Rok výroby")
    stk = models.DateField(verbose_name="Platnost STK")
    dalnicni_znamka = models.DateField(verbose_name="Platnost dálniční známky", blank=True, null=True)
    pojistka = models.DateField(verbose_name="Platnost povinného ručení", blank=True, null=True)

    def __str__(self):
        return f"{self.znacka} {self.model} ({self.spz})"

    def posledni_vymena_oleje(self):
        """
        Vrátí poslední výměnu oleje pro toto vozidlo.
        """
        return self.servisni_ukony.filter(typ='vymena_oleje').order_by('-datum').first()

class ServisniUkon(models.Model):
    TYPY_UKONU = [
        ('vymena_oleje', 'Výměna oleje'),
        ('oprava', 'Oprava'),
        ('vymena', 'Výměna dílu'),
        ('jine', 'Jiný servisní úkon'),
    ]

    vozidlo = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="servisni_ukony")
    datum = models.DateField(verbose_name="Datum servisu")
    km = models.IntegerField(verbose_name="Kilometry při servisu")
    typ = models.CharField(max_length=20, choices=TYPY_UKONU, verbose_name="Typ úkonu", default='jine')
    popis = models.TextField(verbose_name="Popis servisního úkonu", blank=True, null=True)

    def __str__(self):
        return f"{self.vozidlo} - {self.popis} ({self.datum})"

