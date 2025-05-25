from num2words import num2words
a_1=float(input("birinchi kun harajatni kiriting: $)"))
a_2=float(input("ikkinchi kun harajatini kiriting: $"))
a_3=float(input("uchunchi kun harajatini kiriting: $"))
a_4=float(input("to'rtinchi kun harajatini kiriting: $"))
a_5=float(input("beshinchi kun harajatini kiriting: $"))
a_6=float(input("oltinchi kun harajatini kiriting: $"))
a_7=float(input("yettinchi kun harajatini kiriting: $"))
ortachasi=(a_1+a_2+a_3+a_4+a_5+a_6+a_7)/7
a=f"{ortachasi:.2f}"
print("o'rtacha harajat:($)",a,",",end="")
print(num2words(a,lang="en",to="currency"),"  ",end="")
print(num2words(a,lang="ru",to="currency"))
