from num2words import num2words
a=float(input("birinchi mahsulot narxini kiriting:($)"))
b=float(input("ikkinchi mahsulot narxini kiriting:($)"))
c=float(input("uchunchi mahsulot narxini kiriting:($)"))
jami=a+b+c
a=f"{jami:.2f}"
print("umumiy summa:($)",jami,",",end="")
print(num2words(jami,lang="en"),",",(num2words(jami,lang="ru")))
print("yaxlitlangan narx:($)",f"{jami:.2f}",",",end="")
print(num2words(a,lang="en"),",",(num2words(a,lang="ru")))