def add(*args):
    sum = 0
    for n in args:
        print(n)
        sum += n
    return sum

print(add(99,1))

# def calculate(**kwargs ):
#     print(kwargs)
#
#     # for key, value in kwargs.items():
#     #     print(key)
#     n += kwargs ["add"]
#     n *= kwargs ["multiply"]
#     print (n)
#     print(kwargs)

# calculate(start =2,sum=2, multiply=3)

class Car:
    def __init__(self,**kw):
        self.name = kw["name"]
        self.price = kw ["price"]
        self.model = kw ["model"]
        self.year = kw ["year"]

my_car = Car(name = "rider",year= 2009,model="Toyota Supra",price=10000000)
print(my_car.year)
