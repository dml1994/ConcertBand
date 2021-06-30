from django.http import request
from django.test import TestCase
from accounting.models import Ledger, Period, Entry
from accounting.admin import LedgerAdmin, PeriodAdmin, EntryAdmin

# Create your tests here.

class AccountingTestCase(TestCase):

    def setUp(self):

        l = Ledger(name="Libro de Cuentas Test 1", initialBalance = 1000)

        p = Period(name="Ejercicio Test 1",ledger = l) 

        l.save()

        p.save()

        super().setUp()

    def tearDown(self):

        super().tearDown()

        self.l=None

        self.p=None


    @staticmethod
    def createEntry(concept,amount,spending,period):
        e = Entry(concept=concept,amount = amount, spending = spending, period = period)
        e.save()

    # Test de creacion de un Libro de Cuentas
    def test_create_ledger(self):
        led = Ledger.objects.get(name="Libro de Cuentas Test 1")
        self.assertEquals(led.name,"Libro de Cuentas Test 1")
        self.assertEquals(led.initialBalance,1000)
        self.assertEquals(led.currentBalance,1000)

    # Test de creacion de un Ejercicio
    def test_create_period(self):
        p = Period.objects.get(name="Ejercicio Test 1")
        self.assertEquals(p.name,"Ejercicio Test 1")
        self.assertEquals(p.initialBalance,1000)
        self.assertEquals(p.currentBalance,1000)
        self.assertEquals(p.ledger.name,"Libro de Cuentas Test 1")

    # Test de creacion de una Entrada de gasto
    def test_create_spending_entry(self):
        p = Period.objects.get(name="Ejercicio Test 1")
        self.createEntry("Concepto Test 1",500, True, p)
        e = Entry.objects.get(concept="Concepto Test 1")

        # Comprobaciones Entrada
        self.assertEquals(e.concept,"Concepto Test 1")
        self.assertEquals(e.initialBalance,1000)
        self.assertEquals(e.endBalance,500)
        self.assertEquals(e.period.name,"Ejercicio Test 1")
        self.assertEquals(e.amount,500)

        # Comprobaciones Ejercicio
        self.assertEquals(p.name,"Ejercicio Test 1")
        self.assertEquals(p.initialBalance,1000)
        self.assertEquals(p.currentBalance,500)
        self.assertEquals(p.ledger.name,"Libro de Cuentas Test 1")

        # Comprobaciones Libro de Cuentas
        led = Ledger.objects.get(name="Libro de Cuentas Test 1")
        self.assertEquals(led.name,"Libro de Cuentas Test 1")
        self.assertEquals(led.initialBalance,1000)
        self.assertEquals(led.currentBalance,500)

        # Comprobación Cadena de Texto
        self.assertEquals(str(e),str(e.date) + " (Ejercicio Test 1)")

        # Borrado de la Entrada
        e.delete()
        self.assertFalse(Entry.objects.filter(concept="Concepto Test 1").exists())

        # Comprobaciones Ejercicio después del borrado
        p = Period.objects.get(name="Ejercicio Test 1")
        self.assertEquals(p.name,"Ejercicio Test 1")
        self.assertEquals(p.initialBalance,1000)
        self.assertEquals(p.currentBalance,1000)
        self.assertEquals(p.ledger.name,"Libro de Cuentas Test 1")

        # Comprobaciones Libro de Cuentas después del borrado
        led = Ledger.objects.get(name="Libro de Cuentas Test 1")
        self.assertEquals(led.name,"Libro de Cuentas Test 1")
        self.assertEquals(led.initialBalance,1000)
        self.assertEquals(led.currentBalance,1000)

    # Test de creacion de una Entrada de gasto
    def test_create_no_spending_entry(self):
        p = Period.objects.get(name="Ejercicio Test 1")
        self.createEntry("Concepto Test 1",500, False, p)
        e = Entry.objects.get(concept="Concepto Test 1")

        # Comprobaciones Entrada
        self.assertEquals(e.concept,"Concepto Test 1")
        self.assertEquals(e.initialBalance,1000)
        self.assertEquals(e.endBalance,1500)
        self.assertEquals(e.period.name,"Ejercicio Test 1")
        self.assertEquals(e.amount,500)

        # Comprobaciones Ejercicio
        self.assertEquals(p.name,"Ejercicio Test 1")
        self.assertEquals(p.initialBalance,1000)
        self.assertEquals(p.currentBalance,1500)
        self.assertEquals(p.ledger.name,"Libro de Cuentas Test 1")

        # Comprobaciones Libro de Cuentas
        led = Ledger.objects.get(name="Libro de Cuentas Test 1")
        self.assertEquals(led.name,"Libro de Cuentas Test 1")
        self.assertEquals(led.initialBalance,1000)
        self.assertEquals(led.currentBalance,1500)

        # Comprobación Cadena de Texto
        self.assertEquals(str(e),str(e.date) + " (Ejercicio Test 1)")

        # Borrado de la Entrada
        e.delete()
        self.assertFalse(Entry.objects.filter(concept="Concepto Test 1").exists())

        # Comprobaciones Ejercicio después del borrado
        p = Period.objects.get(name="Ejercicio Test 1")
        self.assertEquals(p.name,"Ejercicio Test 1")
        self.assertEquals(p.initialBalance,1000)
        self.assertEquals(p.currentBalance,1000)
        self.assertEquals(p.ledger.name,"Libro de Cuentas Test 1")

        # Comprobaciones Libro de Cuentas después del borrado
        led = Ledger.objects.get(name="Libro de Cuentas Test 1")
        self.assertEquals(led.name,"Libro de Cuentas Test 1")
        self.assertEquals(led.initialBalance,1000)
        self.assertEquals(led.currentBalance,1000)

    # Test Cadena de Texto Libro de Cuentas
    def test_str_ledger(self):
        led = Ledger.objects.get(name="Libro de Cuentas Test 1")
        self.assertEquals(str(led),"Libro de Cuentas Test 1")
    
    # Test Cadena de Texto Ejercico
    def test_str_period(self):
        p = Period.objects.get(name="Ejercicio Test 1")
        self.assertEquals(str(p),"Ejercicio Test 1 (Libro de Cuentas Test 1)")
