from num2words import num2words
a=float(input("oy boshidagi ko'rsatkichni kiriting:($)"))
b=float(input("oy oxiridagi ko'rsatkichni kiriting:($)"))
tok_narxi_1kWh = 0.45
tolov_narxi=(b-a)*tok_narxi_1kWh
c=f"{tolov_narxi:.2f}"
print("to'lov :($)",c,",", end='')
print(num2words(c,lang="en",to="currency"),"  ",end="")
print(num2words(c,lang="ru",to="currency"))