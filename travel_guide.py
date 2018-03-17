#Code takes input for your plan and give you approximate Costing

print ("Select city from 1.London\n2.Paris\n3.Tokiyo\n4.Los Angeles")
city=input("Enter city:")
days=int(input("Days you want to stay:"))
spending_money=int(input("Money you will Spend: "))


def hotel_cost(nights):                        #function definition
  return 140 * nights

def plane_ride_cost(city):
  if city == "London":
    return 183
  elif city == "Paris":
    return 220
  elif city == "Tokiyo":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost

def trip_cost(city,days,spending_money):
  sum=hotel_cost(days)+plane_ride_cost(city)+rental_car_cost(days)+spending_money
  return sum

print (trip_cost(city,days,spending_money))                           #function call inside print.