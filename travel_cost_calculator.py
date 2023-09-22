
# Dilexsan H.A.L EG/2020/3896

from csv import *

a = {}
currency_array = {}
c = {}

def hotel_rates(file):  
    with open(file) as h:
        r = reader(h)
        for row in r:
            a[row[0]] = float(row[1])

def exchange_rates(file): 
    with open(file) as e:
        r = reader(e)
        for row in r:
            currency_array[row[0].upper()] = float(row[1]) * 1 

def flight_costs(file):
    with open(file) as f:
        r = reader(f)
        for row in r:
            c[row[0]] = float(row[1])

def main():
    
    hotel_rates('data/hotel_rates.csv')
    exchange_rates('data/exchange_rates.csv')
    flight_costs('data/flight_costs.csv')

    destination = input("Enter your destination: ").upper()

    f = c.get(destination, 0.0)
    hours = a.get(destination, 0.0)

    days = int(input("Enter your stay duration in days: "))
    hours *= days
    total = f + hours

    print(f"Flight cost: USD {f:.2f}")
    print(f"Hotel cost for {days} days: USD {hours:.2f}")
    print(f"Total: USD {total:.2f}")

    currency = input(f"Select your currency for final price estimation ({', '.join(currency_array.keys())}): ")

    price = total * currency_array[currency]
    print(f"Total in {currency}: {price:.2f}")

if __name__ == "__main__":
    main()
