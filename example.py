from functools import reduce

# a=int(input())
# b=int(input())
# c= int(input())
# print(c==a+b)

# age1 = int(input())
# age2 = int(input())

# if (age1>age2):
#     print(age1,"is greater than", age2)
# elif age1<age2:
#     print(age2, "is greater than", age1)
# else:
#     print(age1,"and", age2, "are equal")

# if age2>age1 or age1>age2:
#     print(age1, " and ", age2, " are different")
# else:
#     print(age1, " is equal to ", age2)


# while (age1<10):
#     print(age1)
#     age1=age1+1

# while (True):
#     age1 = input('say: ')
#     print('yazilan say: ', age1)


# myBabyAge = 26

# while (True):
#     age = int(input("tahmin et bakalım: "))
#     if  myBabyAge == 0:
#         print ("Çok küçükmüş")
#     elif myBabyAge > age:
#         print("Biraz artır")
#     elif myBabyAge < age:
#         print("Yox o qədər də deyil azalt")
#     else:
#         print("Doğruuuu!!!!")
#         break



az = "əğöüşçİı"
isim = input( 'Adinizi yazin: ')
print('adinizin herfleri: ')
for letter in isim:
    letter
    
# ad = input( 'Adınızı təkrar yazın: ')

for char in isim:
    if char in az:
        print("Müəyyən edilmiş hərflərin istifadəsi qadağandır!")
    else:
        print(char)
        





# num1=int(input())
# num2=int(input())
# while (True):
#     if (num1*num2==1000 or num1*num2<1000):
#         print(num1*num2)
#         break
#     else:
#         print(num1+num2)
#         break

# num =  range(0,int(input("Enter a number: ")))

# for i in num:
#         result = i+(i-1)
#         print(i,"+",i-1,"=",result)



# def fakt(n):
#     if (n>=0):
#         if (n==1 or n==0):
#             return 1
#         else:
#             return n*fakt(n-1)
#     else:
#         print("The num must be bigger than 0")

# num = int(input())
# print(fakt(num))



# def square(num):
#     return num*num

# nums = range(int(input()))

# calc = list(map(square, nums))
# print(calc)


# def evennums(num):
#     return num%2

# nums = range(int(input()))
# print(list(filter(evennums, nums)))


# def isTitle(word):
#     return word.istitle()

# words = [input(), input(), input()]
# print(list(filter(isTitle, words)))

