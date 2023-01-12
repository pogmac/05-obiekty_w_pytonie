"""
Ćwiczenie – książka adresowa
Wyobraź sobie, że właśnie wracasz z obchodów Dni Sapera (niezwykle hucznych), Święta Bigosu, albo Konwencji Wielbicieli Pizzy Hawajskiej. Jedno jest pewne – masz całą kolekcję wizytówek od ludzi, z którymi chcesz utrzymać kontakt i przydałaby się książka adresowa, żeby ich wszystkich nie pogubić.

Stwórz klasę, która będzie przechowywać informacje z jednej wizytówki. Przyjmij, że każda wizytówka zawiera dane takie jak: imię, nazwisko, nazwa firmy, stanowisko, adres e-mail.

Zdefiniuj listę, która będzie zawierała 5 wizytówek ludzi o losowych danych (dane możesz skopiować ze strony takiej jak Fake Name Generator.

Skonstruuj pętlę, która wyświetli całą zawartość listy wizytówek tak, aby w jednej linii widoczne było imię, nazwisko i adres e-mail właściciela wizytówki.


Z pomocą przychodzi jedna z wielu bibliotek, dostępnych na PyPi, czyli Faker. W telegraficznym skrócie: Faker dostarcza klasę, która potrafi tworzyć losowe dane, ale w sposób, który ma sens dla ludzi.

Ćwiczenie
Napisz funkcję, która tworzy instancje Twojej klasy reprezentującej wizytówkę. Używając biblioteki faker, którą opisaliśmy powyżej. Zapewnij losowość danych w każdej wizytówce, którą zwróci Twoja funkcja.
"""

class BusinessCard:
    def __init__(self, imie, nazwisko, nazwa_firmy, stanowisko, adres_email):
       self.imie = imie
       self.nazwisko = nazwisko
       self.nazwa_firmy = nazwa_firmy
       self.stanowisko = stanowisko
       self.adres_email = adres_email

       #variables 
       self._len_imin = len(imie)+ len(nazwisko)+1

    def __str__(self):
        return f'{self.imie} {self.nazwisko} {self.adres_email}'
    def contact(self):    
        return f'Kontaktuję się z {self.imie} {self.nazwisko} {self.stanowisko} {self.adres_email}'
    
    @property
    def len_imin(self):
        return self._len_imin

    #@len_imin.setter
    #def len_imin(self,imie,nazwisko):
    #    self._len_imin = len(imie) + len(nazwisko)
        

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
print("by_last_name:")
for bc in by_last_name:
    print(bc)    

print("by_email:")
for bc in by_email:
    print(bc)        
"""

#Ćwiczenie
#Rozwiń program przechowujący wizytówki. Do klasy opisującej wizytówkę dodaj metodę contact(), która wypisze na konsoli napis “Kontaktuję się z …”, a na końcu wyświetli imię, nazwisko, stanowisko i adres e-mail osoby, z którą chcemy się skontaktować.

#W klasie przechowującej wizytówkę zdefiniuj dynamiczny atrybut (używając @property), który będzie zwracał sumę długości imienia i nazwiska oddzielonych spacją. Tę informację można wykorzystać przykładowo przy adresowaniu kopert lub zaproszeń, gdzie często miejsce na imię i nazwisko jest dosyć ograniczone.

