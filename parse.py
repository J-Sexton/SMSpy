import sys
import decimal

class Tenant(object):
       name = ""
       paidBool = False
       total = 0.00
       phone = "+1"

def _init_(self, name, paidBool, total, phone,rent, water, internet, power, gas):
       self.name = name
       self.paidBool = paidBool
       self.total = total
       self.phone += phone
       self.rent = rent
       self.water = water
       self.internet = internet
       self.power = power
       self.gas = gas

def make_tenant (name, paidBool, total, phone, rent, water, internet, power, gas):
       tenant = Tenant()
       tenant.name = name
       tenant.paidBool = paidBool
       tenant.total = total
       tenant.phone += phone
       tenant.rent = rent
       tenant.water = water
       tenant.internet = internet
       tenant.power = power
       tenant.gas = gas
       return tenant
      
def getAll():
   a = open("rent.txt", "r") #open file
   myData =[]
   for line in a:
       allRentData = line.split(",")
       x = make_tenant(allRentData[0], allRentData[1], allRentData[2], allRentData[3], allRentData[4], allRentData[5], allRentData[6], allRentData[7], allRentData[8])
       myData.append(x)
   return myData

def getName(var):

   allData = getAll()
   for item in allData:
      if item.name == var:
         return item
         break

