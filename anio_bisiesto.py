#coding: utf8

anio=input("Introdueix un any: ")

if anio%400 == 0:

	print "es bisiesto"

else:

	if anio%100 == 0:

		print "no es bisiesto"
	else:

		if anio%4 == 0:

			print "es bisiesto"
