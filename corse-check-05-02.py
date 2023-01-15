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

class Car:
    def __init__(self, make, model_name, top_speed, color):
       self.make = make
       self.model_name = model_name
       self.top_speed = top_speed
       self.color = color

       # Variables
       self.current_speed = 0

    def accelerate(self, step=10):
       self.current_speed += step

    def decelerate(self, step=10):
       self.current_speed -= step 
    def __repr__(self):
        return f"Car(make={self.make} model={self.model_name}, top_speed={self.top_speed}, color={self.color})"
    def __str__(self):
        return f'{self.color} {self.make} {self.model_name}'     
    def __eq__(self, other):
        return all(
            (
                self.make == other.make,
                self.model_name == other.model_name,
                self.top_speed == other.top_speed,
                self.color == other.color
            )
        )        
    def __gt__(self, other):
        return self.top_speed > other.top_speed  
         
    
    #def __eq__(self, other): # definiujemy funkcję następująco: dwie instancje danej klasy są równe gdy następujące warunki są spełnione: 
    #    return (
    #        self.make == other.make and
    #        self.model_name == other.model_name and
    #        self.top_speed == other.top_speed and
    #        self.color == other.color
    #    )         
    
  
#Mając tak zbudowany konstruktor, nie jest możliwe utworzenie nowych instancji klasy Car bez podania tych czterech parametrów: marki, modelu, prędkości maksymalnej i koloru.       

mustang = Car(make="Ford", model_name="Mustang", color="Yellow", top_speed=250)
print(mustang)
"""
print(mustang.make)
#print(mustang.model_name)
#print(mustang.color)
#print(mustang.top_speed)

#Do konkretnych pól klasy, możemy się dostać za pomocą notacji instancja.pole, tak samo będziemy się również odwoływać do metod zdefiniowanych w obrębie klasy.

#5.2. Metody w klasach
# Metody wbudowane

#print(dir(Car))

# __str__

# Pewnie zastanawiasz się, skąd w ogóle ten dziwny “numer” - 0x10792ff28? Oznacza on dokładny adres w pamięci, pod którym znajduje się obiekt. Jednak taka informacja niewiele mówi o tym, czym jest obiekt, który wydrukowaliśmy na konsoli.
# Spróbujmy to zmienić tak, aby nasz samochód przedstawiony jako string, zwracał kolor, markę oraz model. Nadpiszmy w tym celu metodę __str__ klasy Car w następujący sposób:


# __repr__ 
#Ta metoda odpowiada za to, jak obiekt jest przedstawiony w interpreterze. Z założenia, wynik __str__ powinien być czytelny i przeznaczony dla końcowego użytkownika programu lub skryptu. Natomiast wynik __repr__ jest adresowany głównie do programistów i wyszukiwania problemów w kodzie (debugowania).

#Przykład implementacji metody dla klasy Car:
#def __repr__(self):
#    return f"Car(make={self.make} model={self.model_name}, top_speed={self.top_speed}, color={self.color})"

print(mustang)
print(mustang.__str__)    
car = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
print(car) 
print(car.__repr__)


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

"""
def __eq__(self, other): # definiujemy funkcję następująco: dwie instancje danej klasy są równe gdy następujące warunki są spełnione: 
    return (
        self.make == other.make and
        self.model_name == other.model_name and
        self.top_speed == other.top_speed and
        self.color == other.color
    )

#print(__eq__(car_one,car_two))    
"""
print(car_one == car_two)

## Funkcja all()
## metoda all()

# Python ma wbudowaną funkcję all(), która zwraca True, jeśli wszystkie wartości do niej przekazane również są prawdziwe. W przeciwnym przypadku zwróci False.
"""
def __eq__(self, other):
    return all(
        (
            self.make == other.make,
            self.model_name == other.model_name,
            self.top_speed == other.top_speed,
            self.color == other.color
        )
    )

#print(car_one == car_two)
#print(__eq__(car_one,car_two))

"""
#Zwróć uwagę, że metoda all() przyjmuje zmienną, po której można iterować, czyli np. krotkę lub listę.
#Podobną funkcją jest any(). Ona z kolei zwróci True, jeśli którykolwiek z przekazanych argumentów będzie prawdą.
#Wspomniane funkcje są bardzo praktyczne w momentach, kiedy potrzebujesz sprawdzić jednocześnie wiele warunków logicznych.


car_one = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car_two = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
#print(car_one,'\n',car_two)

print(1, end = " ")
print(car_one == car_two)  #### DLACZEGO to nie działa? Nadpisanie overloading
#print(__eq__(car_one,car_two))

print(2, end = " ")
car_three = Car(make="Ford", model_name="Mustang", top_speed=250, color="Yellow")
print(car_two == car_three)
#print(__eq__(car_one,car_three))

#Samodzielne definiowanie zachowań takich jak dodawanie i porównywanie obiektów, nazywamy przeciążaniem operatorów.

#Uwaga! Przedstawione metody przeciążania operatorów sprawdzą się przy wykonywaniu operacji na obiektach tego samego typu. Jeśli potrzebujesz zaimplementować bardziej zaawansowane zachowania operatorów, jak np. dodawanie do siebie różnych typów obiektów, będziesz potrzebować więcej metod służących do przeciążania operatorów. Szczegółowy opis tych metod, znajdziesz w oficjalnej dokumentacji.

#def __gt__(self, other):
#    return self.top_speed > other.top_speed

car_one = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car_two = Car(make="Ford", model_name="Mustang", top_speed=350, color="Red")

#print(__gt__(car_two,car_one))    

print(car_two > car_one) 


car_one = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car_two = Car(make="Ford", model_name="Fiesta", top_speed=200, color="Blue")
car_three = Car(make="Porsche", model_name="911", top_speed=320, color="Black")
cars = [car_one, car_two, car_three]

by_speed = sorted(cars, key=lambda car: car.top_speed, reverse= True)
by_make = sorted(cars, key=lambda car: car.make)

print("by_speed, reverse = True:")
for car in by_speed:
    print(car)
print("by_make:")
for car in by_make:
    print(car)

def get_make(car):
    return car.make
lambda car: car.make
"""
## Własne metody


class Car:
    def __init__(self, make, model_name, top_speed, color):
       self.make = make
       self.model_name = model_name
       self.top_speed = top_speed
       self.color = color

       # Variables
       self._current_speed = 0

    def accelerate(self, step=10):
       self.current_speed += step

    def decelerate(self, step=10):
       self.current_speed -= step
       
    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, value):
        if value <= self.top_speed:
            self._current_speed = value
        else:
            raise ValueError(f"Value {value} exceeds top speed of {self.top_speed}")        

    def __repr__(self):
        return f"Car(make={self.make} model={self.model_name}, top_speed={self.top_speed}, color={self.color})"
    def __str__(self):
        return f'{self.color} {self.make} {self.model_name}'     
    def __eq__(self, other):
        return all(
            (
                self.make == other.make,
                self.model_name == other.model_name,
                self.top_speed == other.top_speed,
                self.color == other.color
            )
        )        
    def __gt__(self, other):
        return self.top_speed > other.top_speed  

# Definicja klasy Truck, która jest podklasą klasy Car

class Truck(Car):
   def __init__(self, max_load, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.max_load = max_load




"""
car = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car.current_speed: print(car.current_speed)
car.accelerate(); print(car.current_speed)
car.accelerate(50); print(car.current_speed)

## @property - dynamiczne atrybuty klas

car = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car.current_speed = 100; print(car.current_speed)

car = Car(make="Ford", model_name="Mustang", top_speed=250, color="red")
print(car.current_speed); print()

#car.current_speed() Metoda current_speed zachowuje się w tej chwili tak, jakby była zwykłym atrybutem klasy Car.

car = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car.current_speed = 100
print(car.current_speed)

#car.current_speed = 400 # W tym konkretnym przypadku zapewniamy, że wartość current_speed nigdy nie przekroczy prędkości maksymalnej samochodu:

print(car.current_speed)
"""
## Koniec Modułu 05.02


## Moduł 05.03 BEGIN 

"""
print("BEGIN 05.03")
truck = Truck(make="Mercedes", model_name="Actros", color="Black", top_speed=90, max_load=1200)
print();print(truck);print()

print(truck.current_speed)
truck.accelerate()
print(truck.current_speed)
truck.accelerate()
print(truck.current_speed)

print("Max load: ",truck.max_load)

## Funkcja super()
# Jak wspomnieliśmy powyżej, funkcja super() służy do odwołania się do klasy, po której odziedziczyliśmy. W naszym przykładzie będziemy odwoływać się z poziomu Truck do klasy Car, żeby móc usunąć trochę nadmiarowego kodu z konstruktora.

## Przydatne funkcje wbudowane
# W Pythonie dostępne są dwie funkcje wbudowane, które zostały zaprojektowane specjalnie po to, by wspomagać dziedziczenie obiektów: isinstance() oraz issubclass().

truck = Truck(make="Mercedes", model_name="Sprinter", color="Black", top_speed=90, max_load=1200)
car = Car(make="Ford", model_name="Mustang", top_speed=250, color="red")
print("isinstance(car, Truck)", end = " "); print(isinstance(car, Truck))
print("isinstance(car, Car)", end = "   "); print(isinstance(car, Car))
print("isinstance(truck, Car)", end = " "); print(isinstance(truck, Car));print()

#Funkcja issubclass() z kolei działa na klasach, a nie na konkretnych instancjach. Pozwala wykryć czy jedna klasa, dziedziczy z drugiej:

print("issubclass(Truck,Car)", end =" ");print(issubclass(Truck,Car))
print("issubclass(Car,Truck)", end =" ");print(issubclass(Car,Truck))

print();print()
print("END 05.03")
#print();print()

"""
## Moduł 05.03 END


## Moduł 05.04 Wielodziedziczenie BEGIN 

class DieselEngine:
   def tank(self, how_many=100):
       print(f"Adding {how_many} liters of Diesel")

class PetrolEngine:
   def tank(self, how_many=20):
       print(f"Adding {how_many} liters of Petrol")

class Truck(Car, DieselEngine):
   def __init__(self, max_load, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.max_load = max_load

class SportCar(Car, PetrolEngine):
   pass

#Zdefiniowaliśmy również klasę SportCar, która jest specjalnym przypadkiem klasy Car, z dodatkiem silnika benzynowego (nie definiuje żadnej dodatkowe logiki, więc zawiera jedynie instrukcję pass). W efekcie będzie dostarczała wszystko, co ma klasa Car oraz wszystko, co daje klasa PetrolEngine.

truck = Truck(make="Mercedes", model_name="Sprinter", color="Black", top_speed=90, max_load=1200)
porsche = SportCar(make="Porsche", model_name="911", color="Red", top_speed=250)
truck.tank()
porsche.tank()


# Zestaw wskazówek dla programistów:
# import this

# We wcześniejszej części tego modułu poznaliśmy @property, czyli zapis dekoratora w Pythonie.

#W Pythonie dekorator jest funkcją, która jako parametr przyjmuje inną funkcję (pamiętaj, że wszystko w Pythonie jest obiektem, więc bez problemu możemy przypisać funkcję do zmiennej, bez jej wywołania). Dzięki temu zachowaniu jesteśmy w stanie dynamicznie zmienić zachowanie dekorowanej funkcji. Dekoratory w Pythonie wywołujemy z użyciem @.

def say_hello():
   greeting = "Hello stranger!"
   return greeting

print(say_hello())   

def say_louder(func):
   def wrapper():
       result = func()
       return result.upper()
   return wrapper

@say_louder
def say_hello():
   greeting = "Hello stranger!"
   return greeting

print(say_hello())

#Powyższy zapis z użyciem @say_louder jest jednoznaczny z wywołaniem funkcji w ten sposób:

say_hello = say_louder(say_hello)
print(say_hello())

#Niemniej jednak, jeśli chcemy, aby funkcja pozostała udekorowana za każdym razem, kiedy jest wywoływana, najlepiej użyć składni z @.

#Ćwiczenie
#Napisz funkcję, która tworzy listę zawierającą 1000 wizytówek z losowymi danymi (użyj biblioteki faker, którą opisywaliśmy w tym module).

#Następnie stwórz dekorator, który zmierzy czas wykonywania tej operacji. Niech udekorowana funkcja wyświetla czas obliczeń (w sekundach) po ich zakończeniu.

#Wskazówka. W Pythonie do operacji na datach i czasie wykorzystuje się moduł datetime. Zapoznaj się z jego dokumentacją.

## Moduł 05.04 Wielodziedziczenie END

