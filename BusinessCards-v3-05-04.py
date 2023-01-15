class BaseContact: # Definicja klasy podstawowej BaseContact 
    def __init__(self, imie, nazwisko, telefon_prywatny, adres_email):
       self.imie = imie
       self.nazwisko = nazwisko
       self.telefon_prywatny = telefon_prywatny
       self.adres_email = adres_email
       
       #variables 
       self._len_imin = len(imie)+ len(nazwisko)+1

    def __str__(self):
        return f'{self.imie} {self.nazwisko} {self.telefon_prywatny} {self.adres_email}'
    def contact(self):    
        return f'Wybieram number {self.telefon_prywatny} i dzwonię do {self.imie} {self.nazwisko}'
    
    @property
    def len_imin(self):
        return self._len_imin

class BusinessContact(BaseContact): # Definicja klasy rozszeżającej klasę podstawową BaseContact o atrybuty służbowe
    def __init__(self,nazwa_firmy, stanowisko,telefon_sluzbowy, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nazwa_firmy = nazwa_firmy
        self.stanowisko = stanowisko
        self.telefon_sluzbowy = telefon_sluzbowy
    def __str__(self):
        return f'{self.imie} {self.nazwisko} {self.adres_email} {self.nazwa_firmy} {self.stanowisko} {self.telefon_sluzbowy}'
    def contact(self):    
        return f'Wybieram number {self.telefon_sluzbowy} i dzwonię do {self.imie} {self.nazwisko}'    

### Tworzę funkcje create BaseContact i BusinessContact


import datetime
import time
from faker import Faker
fake = Faker()
#def createBaseContact():
#    faker_p = BaseContact(imie = fake.first_name(), nazwisko =fake.last_name(), telefon_prywatny=fake.phone_number(), adres_email= fake.email())
#    return faker_p

#def createBusinessContact():
#    faker_p = BusinessContact(imie = fake.first_name(), nazwisko =fake.last_name(), telefon_prywatny=fake.phone_number(), adres_email= fake.email(), nazwa_firmy = fake.company(), stanowisko = fake.job(), telefon_sluzbowy = fake.phone_number())
#    return faker_p

name_list =[]
def create_contacts(conType,number):
    """
    Creates a certain number of business cards of a passed type "conType" and assigns them to a list name_list[]
    Arguments:
    conType = [BaseContact,BusinessContact]
    number = integer
    """
    
    print();print("Wybrałeś typ = ", conType);print("Liczba wizytówek stworzona =", number); print()
    if conType == BaseContact:    
        for i in range(number):
            faker_p = BaseContact(imie = fake.first_name(), nazwisko =fake.last_name(), telefon_prywatny=fake.phone_number(), adres_email= fake.email())
            name_list.append(faker_p) #print("Typ =", conType, i)
            #print(name_list[i])
        print()
    elif conType == BusinessContact:    
        for i in range(number):
            faker_p = BusinessContact(imie = fake.first_name(), nazwisko =fake.last_name(), telefon_prywatny=fake.phone_number(), adres_email= fake.email(), nazwa_firmy = fake.company(), stanowisko = fake.job(), telefon_sluzbowy = fake.phone_number())
            name_list.append(faker_p) #print("Typ =", conType, i)
            #print(name_list[i])
        print()
    else:
        print("Wybierz właściwy typ kontaktu (BaseContact lub BusinessContact")
t1 = time.time()

create_contacts(BaseContact,5000)
#create_contacts(BusinessContact,3)
"""
for i in range(len(name_list)):
    print(f"{name_list[i].imie}, {name_list[i].nazwisko}, {name_list[i].telefon_prywatny}, {name_list[i].adres_email}")
    print()
"""

#print(help(create_contacts))
t2 = time.time()

print(f"zadanie zajęło: {t2-t1} sekund")



### testowanie czy działa na prostych kontaktach Base i Business

messi = BaseContact(imie = "leo", nazwisko="Messi", telefon_prywatny ="+48123456789", adres_email="maciejmaciejewski@jourrapide.com") 
lewybiz = BusinessContact(imie = "Robert", nazwisko="Lewandowski", telefon_prywatny ="+48123456789", adres_email="maciejmaciejewski@jourrapide.com", nazwa_firmy="Orlen", stanowisko = "CEO", telefon_sluzbowy = "+49987654321")
print();#print(maciejewski)
print(BaseContact.contact(messi))
print("messi.len_imin = ", end = " ");print(messi.len_imin)

print();#print(maciejewski_biznes)
print(BusinessContact.contact(lewybiz))
print("lewybis.len_imin = ", end = " ");print(lewybiz.len_imin)
print()


### Sprawdzam funkcje create BaseContact i BusinessContact
#johnBase = createBaseContact();print(johnBase)
#johnBus = createBusinessContact();print(johnBus)
# obie działają poprawnie


"""
maciejewski = BusinessCard(imie = "Maciej", nazwisko="Maciejewski", nazwa_firmy="Carl Durfees", stanowisko ="Water and liquid waste treatment plant operator", adres_email="szczesnyMaciejewski@jourrapide.com")
lewandowski= BusinessCard(imie = "Robert", nazwisko ="Lewandowski", nazwa_firmy="Barcelona", stanowisko ="striker", adres_email="robertlewandowski@barcelona.es")
musk= BusinessCard(imie = "Elon", nazwisko ="Musk", nazwa_firmy="Tesla", stanowisko ="CEO", adres_email="elonmusk@tesla.com")



name_list = []
name_list.append(maciejewski)
name_list.append(lewandowski)
name_list.append(musk)

#print(BusinessCard._len_imie_i_nazwisko)
#musk.len_imin = 10
print(musk.len_imin)

#print(BusinessCard.len_imin(musk))


from faker import Faker
fake = Faker()
#print(dir(fake))

def faker_func():
    #from faker import Faker
    #fake = Faker()
    faker_p = BusinessCard(imie = fake.first_name(), nazwisko =fake.last_name(), nazwa_firmy=fake.company(), stanowisko =fake.job(), adres_email= fake.email())
    return faker_p

for i in range(10):
    name_list.append(faker_func())

for i in range(len(name_list)):
    print(f"{name_list[i].imie}, {name_list[i].nazwisko}, {name_list[i].nazwa_firmy}, {name_list[i].stanowisko}, {name_list[i].adres_email}")
    


# Ćwiczenie
#1 Zmodyfikuj kod z poprzedniego ćwiczenia na temat książki adresowej tak, aby obiekt wizytówki przedstawiony jako string zawierał imię, nazwisko i adres e-mail osoby, do której należy wizytówka.

print();print("Oto i lista za pomocą nadpisanej funkcji __str__")

for businessCard in name_list:
    print(businessCard)

#2 Stwórz listę wizytówek, a następnie używając funkcji sorted(), ułóż ją na trzy sposoby – według imienia, nazwiska oraz adresu e-mail.


by_first_name = sorted(name_list, key=lambda BusinessCard: BusinessCard.imie)
by_last_name = sorted(name_list, key = lambda BusinessCard: BusinessCard.nazwisko)
by_email = sorted(name_list, key = lambda BusinessCard: BusinessCard.adres_email)

print();print("by_first_name:");print()
for bc in by_first_name:
    print(BusinessCard.contact(bc))
    print(bc.len_imin)
    #print(bc)

"""

"""
print("by_last_name:")
for bc in by_last_name:
    print(bc)    

print("by_email:")
for bc in by_email:
    print(bc)        
"""
