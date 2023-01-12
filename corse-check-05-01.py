#5.1. Klasy i obiekty
# Definiowanie klasy

# Przykład definicji klasy:
"""
class Car:
    pass

# Mając tak zdefiniowaną klasę, możemy już tworzyć jej instancje:

my_car = Car()
print(type(my_car))
"""
# W powyższym przykładzie do zmiennej my_car przypisaliśmy wynik wywołania klasy Car. Taki zapis oznaczał wywołanie wbudowanej funkcji, konstruktora klasy Car. Konstruktor to specjalna funkcja, której zadaniem jest tworzenie nowych instancji klasy.

#Metoda – funkcja, która jest zdefiniowana w obrębie klasy. Konstruktor – funkcja, która służy do tworzenia nowych instancji klasy. Atrybut – zmienna, która jest zdefiniowana na poziomie klasy.

# Zmienna self

"""
class Car:
   def __init__(self):
       pass
"""
class Car:
   def __init__(self, make, model_name, top_speed, color):
       self.make = make
       self.model_name = model_name
       self.top_speed = top_speed
       self.color = color

#Mając tak zbudowany konstruktor, nie jest możliwe utworzenie nowych instancji klasy Car bez podania tych czterech parametrów: marki, modelu, prędkości maksymalnej i koloru.       

mustang = Car(make="Ford", model_name="Mustang", color="Yellow", top_speed=250)
print(mustang)

print(mustang.make)
print(mustang.model_name)
print(mustang.color)
print(mustang.top_speed)

#Do konkretnych pól klasy, możemy się dostać za pomocą notacji instancja.pole, tak samo będziemy się również odwoływać do metod zdefiniowanych w obrębie klasy.
"""
class BusinessCard:
   def __init__(self, imie, nazwisko, nazwa_firmy, stanowisko, adres_email):
       self.imie = imie
       self.nazwisko = nazwisko
       self.nazwa_firmy = nazwa_firmy
       self.stanowisko = stanowisko
       self.adres_email = adres_email

maciejewski = BusinessCard(imie = "Maciej", nazwisko="Maciejewski", nazwa_firmy="Carl Durfees", stanowisko ="Water and liquid waste treatment plant and system operator", adres_email="SzczesnyMaciejewski@jourrapide.com")

lewandowski= BusinessCard(imie = "Robert", nazwisko ="Lewandowski", nazwa_firmy="Barcelona", stanowisko ="striker", adres_email="robertlewandowski@barcelona.es")

musk= BusinessCard(imie = "Elon", nazwisko ="Musk", nazwa_firmy="Tesla", stanowisko ="CEO", adres_email="elonmusk@tesla.com")
from faker import Faker
fake = Faker()
faker = BusinessCard(imie = fake.name(), nazwisko =fake.name(), nazwa_firmy=fake.company(), stanowisko =fake.job(), adres_email= fake.email())

name_list = []
name_list.append(maciejewski)
name_list.append(lewandowski)
name_list.append(musk)
name_list.append(faker)

#print(f"{name_list[0].imie}, {name_list[0].nazwisko}, {name_list[0].nazwa_firmy} , {name_list[0].stanowisko}, {name_list[0].adres_email} ")
for i in range(len(name_list)):
    print(f"{name_list[i].imie}, {name_list[i].nazwisko}, {name_list[i].nazwa_firmy}, {name_list[i].stanowisko}, {name_list[i].adres_email}")

"""

"""
from faker import Faker
fake = Faker()

print(fake.name())
print(fake.address())
print(fake.text())
"""
"""
faker = BusinessCard(imie = fake.name(), nazwisko =fake.name(), nazwa_firmy=fake.company(), stanowisko =fake.job(), adres_email= fake.email())

print(faker.imie)
print(faker.nazwisko)
print(faker.nazwa_firmy)
print(faker.stanowisko)
print(faker.adres_email)
"""

#5.2. Metody w klasach
# Metody wbudowane

print(dir(Car))

# __str__

print(mustang)

# Pewnie zastanawiasz się, skąd w ogóle ten dziwny “numer” - 0x10792ff28? Oznacza on dokładny adres w pamięci, pod którym znajduje się obiekt. Jednak taka informacja niewiele mówi o tym, czym jest obiekt, który wydrukowaliśmy na konsoli.
# Spróbujmy to zmienić tak, aby nasz samochód przedstawiony jako string, zwracał kolor, markę oraz model. Nadpiszmy w tym celu metodę __str__ klasy Car w następujący sposób:

def __str__(self):
    return f'{self.color} {self.make} {self.model_name}'

print(__str__(mustang))

# __repr__ 
#Ta metoda odpowiada za to, jak obiekt jest przedstawiony w interpreterze. Z założenia, wynik __str__ powinien być czytelny i przeznaczony dla końcowego użytkownika programu lub skryptu. Natomiast wynik __repr__ jest adresowany głównie do programistów i wyszukiwania problemów w kodzie (debugowania).

#Przykład implementacji metody dla klasy Car:
def __repr__(self):
    return f"Car(make={self.make} model={self.model_name}, top_speed={self.top_speed}, color={self.color})"

print(__str__(mustang))
print(__repr__(mustang))    


# Warto wspomnieć, że jeśli zdefiniujesz tylko metodę __repr__, a nie zdefiniujesz __str__, to Twoja klasa po przedstawieniu jako string, zwróci to, co zwraca metoda __repr__.

## __eq__, __gt__, __ge__, __lt__, __le__
# Grupa tych metod odpowiada za porównania obiektów. Dlaczego są przydatne? Czasami możesz potrzebować zestawić ze sobą dwie instancje tej samej klasy, żeby na przykład usunąć duplikaty z listy czy posortować listę obiektów.

car_one = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car_two = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
print(car_one,'\n',car_two)
print(car_one == car_two)

#Domyślnie dwie instancje, nawet o tych samych atrybutach, to zupełnie dwa różne obiekty. Możesz jednak kontrolować to zachowanie obiektów, przez nadpisanie metody __eq__ (od ang. equals).

#Metoda __eq__ przyjmuje dwa parametry: self (jak każda metoda klasy, będzie tutaj przekazany automatycznie obiekt, na którym została wywołana metoda) oraz other, czyli drugi obiekt tej samej klasy, z którym porównujemy.

#Rezultatem tej metody musi być wartość logiczna True lub False.

def __eq__(self, other): # definiujemy funkcję następująco: dwie instancje danej klasy są równe gdy następujące warunki są spełnione: 
    return (
        self.make == other.make and
        self.model_name == other.model_name and
        self.top_speed == other.top_speed and
        self.color == other.color
    )

print(__eq__(car_one,car_two))    

## Funkcja all()
## metoda all()

# Python ma wbudowaną funkcję all(), która zwraca True, jeśli wszystkie wartości do niej przekazane również są prawdziwe. W przeciwnym przypadku zwróci False.

def __eq__(self, other):
    return all(
        (
            self.make == other.make,
            self.model_name == other.model_name,
            self.top_speed == other.top_speed,
            self.color == other.color
        )
    )

print(__eq__(car_one,car_two))

#Zwróć uwagę, że metoda all() przyjmuje zmienną, po której można iterować, czyli np. krotkę lub listę.
#Podobną funkcją jest any(). Ona z kolei zwróci True, jeśli którykolwiek z przekazanych argumentów będzie prawdą.
#Wspomniane funkcje są bardzo praktyczne w momentach, kiedy potrzebujesz sprawdzić jednocześnie wiele warunków logicznych.


car_one = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car_two = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
#print(car_one,'\n',car_two)

print(1)
print(car_one == car_two)  #### DLACZEGO to nie działa? Nadpisanie overloading
print(__eq__(car_one,car_two))


car_three = Car(make="Ford", model_name="Mustang", top_speed=250, color="Yellow")
print(__eq__(car_one,car_three))

#Samodzielne definiowanie zachowań takich jak dodawanie i porównywanie obiektów, nazywamy przeciążaniem operatorów.

#Uwaga! Przedstawione metody przeciążania operatorów sprawdzą się przy wykonywaniu operacji na obiektach tego samego typu. Jeśli potrzebujesz zaimplementować bardziej zaawansowane zachowania operatorów, jak np. dodawanie do siebie różnych typów obiektów, będziesz potrzebować więcej metod służących do przeciążania operatorów. Szczegółowy opis tych metod, znajdziesz w oficjalnej dokumentacji.

def __gt__(self, other):
    return self.top_speed > other.top_speed

car_one = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car_two = Car(make="Ford", model_name="Mustang", top_speed=350, color="Red")

print(__gt__(car_two,car_one))    
#print(car_one > car_two) ## DLACZEGO to nie działa?

car_one = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car_two = Car(make="Ford", model_name="Fiesta", top_speed=200, color="Blue")
car_three = Car(make="Porsche", model_name="911", top_speed=320, color="Black")
cars = [car_one, car_two, car_three]

by_speed = sorted(cars, key=lambda car: car.top_speed, reverse= True)
by_make = sorted(cars, key=lambda car: car.make)

print("by_speed:")
for car in by_speed:
    print(__repr__(car))
print("by_make:")
for car in by_make:
    print(__repr__(car))

def get_make(car):
    return car.make
lambda car: car.make