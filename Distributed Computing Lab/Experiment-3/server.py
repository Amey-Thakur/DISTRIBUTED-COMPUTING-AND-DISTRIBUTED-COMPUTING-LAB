import Pyro4
import random
import os
import datetime
import subprocess
import math

now=datetime.datetime.now()
print('date: '+now.strftime('%d-%m-%y')+' Time:'+now.strftime('%H:%M:%S'))
@Pyro4.expose

class Server(object):
    def get_usid(self, name):
        return "Hello, {0}.\n" \
        "Your Current User Session is {1}:".format(name, random.randint(0,1000))

    def add(self, a, b):
        return "{0} + {1} = {2}".format(a, b, a+b)

    def subtract(self, a, b):
        return "{0} - {1} = {2}".format(a, b, a-b)

    def multiply(self, a, b):
        return "{0} * {1} = {2}".format(a, b, a*b)

    def division(self, a, b):
        return "{0} / {1} = {2}".format(a, b, a/b)

    def sqr(self, a):
        return "{0} ^ 2 = {1}".format(a, a**2)

    def sqrt(self, a):
        return "sqrt({0}) = {1}".format(a, math.sqrt(a))

    def mod(self, a, b):
        return "{0} % {1} = {2}".format(a, b, a%b)

    def per(self, a, b):
        return "( {0} / {1} ) * 100 = {2}".format(a, b, (a/b)*100)

    def exp(self, a, b):
        return "{0} ** {1} = {2}".format(a, b, a**b)

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
url = daemon.register(Server)
ns.register("RMI.calculator", url)

print("The Server is now active., please request your calculations or start file transfer")

daemon.requestLoop()
