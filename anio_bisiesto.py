#coding: utf8

anio=input("Introdueix un any: ")

def esBisiesto (anio):

	if (anio%4==0 and anio%100!=0) or anio%400==0:

		print "És bisiesto"

	else:

		print "No és bisiesto"

esBisiesto(anio)

anio2=input("Introdueix un any: ")

esBisiesto(anio2)

anio3=input("Introdueix un any: ")

esBisiesto(anio3)
