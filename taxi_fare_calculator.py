from num2words import num2words
boshlangich_tolov=3.00
har_km_uchun=1.20
masofa=float(input("masofani kiriting:(km)"))
jami=boshlangich_tolov+(masofa*har_km_uchun)
a=f"{jami:.2f}"
print("taxi narxi:($)",a,",",end="")
print(num2words(a,lang="en",to="currency"),"  ",end="")
print(num2words(a,lang="ru",to="currency"))
