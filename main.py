import random
from bicycles import Bicycle, BikeShop, Customer

bikes = [
    Bicycle("Off-Road XC", 75, 100), Bicycle("Off-Road GRAVITY", 70, 150),
    Bicycle("Off-Road TRAIL", 50, 250), Bicycle("Off-Road SPRORT XC", 90, 350),
    Bicycle("Off-Road ENDURO", 65, 100), Bicycle("Off-Road RECREATION", 75, 550)
    ]

shop = BikeShop("GiantShop Surplus Cycles", 20, bikes)

customers = [Customer("Hue", 200), Customer("Saigon", 500), Customer("Hanoi", 1000)]

print ("--------------------------Giant bikes Recommendation for Customer---------------------------------")
for customer in customers:

    bikes = ", ".join( bike.model for bike in shop.filter(customer.fund) )

    print ("Customer:", customer.name, "|", bikes)

print ('\n\n', "--------------------------Surplus Before Sales---------------------------------")
print (shop)

print ("--------------------------Detail Sales---------------------------------")
template = "{0} bought the {1} at ${2}, and they have ${3} left over."

for customer in customers:
    
    affordables = shop.filter(customer.fund)
    shop.sell(random.choice(affordables), customer)
    
    print (template.format(
        customer.name, customer.bike.model,
        customer.bike.price, customer.fund
        ))

print ('\n\n', "--------------------------GiantShop Surplus---------------------------------")
print (shop)
print ("--------------------------------Final---------------------------------------")
