from num2words import num2words

pul = int(input("Pul miqdorini kiriting ($): "))

a_50=pul//50
pul=pul%50
print("$50 kupyuradan:", a_50, "ta")

a_10=pul//10
pul=pul%10
print("$10 kupyuradan:", a_10, "ta")

a_5=pul//5
pul=pul%5
print("$5 kupyuradan:", a_5, "ta")

a_1=pul//1
pul=pul%1
print("$1 kupyuradan:", a_1, "ta")
a=a_50*50+a_10*10+a_5*5+a_1*1
print("umumiy summa:($)",a,end=" ")
print(num2words(a,lang='en'),end=",")
print(num2words(a,lang='ru'))
