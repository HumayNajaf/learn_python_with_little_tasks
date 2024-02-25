import random
import time
import math

point = 0
while True:
    rand = random.randint(1,4)

    print("Suallar hazırlanır, biraz səbrli olun...")
    time.sleep(2)
    if rand==1:
        print("Ədədləri topla!...")
        firstNum = random.randint(1,20)
        secNum = random.randint(1,20)
        print(f"{firstNum} ilə {secNum} cəmini tapın!")
        time.sleep(2)
        result = int(input("Cavab: "))
        if firstNum+secNum == result:
            print("Təbriklər! Növbəti suala keçə bilərsiniz")
            point = point + 1
            time.sleep(2)
            print(f"Your point: {point}")
        else:
            print(f"Maaf! Suala yanlış cavab verdiniz. Doğru cavab: {firstNum+secNum}")
            point = point - 2
            time.sleep(2)
            print(f"Your point: {point}")
            if point<0:
                print("Yolun sonu......")
                quit()
    elif rand==2:
        print("Çıxma əməlini yerinə yetir!...")
        time.sleep(2)
        firstNum = random.randint(1,20)
        secNum = random.randint(1,20)
        print(f"{firstNum} - {secNum} = ?")
        time.sleep(2)
        result = int(input("Cavab: "))
        if firstNum-secNum == result:
            print("Təbriklər! Növbəti suala keçə bilərsiniz")
            point = point + 1
            time.sleep(2)
            print(f"Your point: {point}")
        else:
            print(f"Maaf! Suala yanlış cavab verdiniz. Doğru cavab: {firstNum-secNum}")
            point = point - 2
            time.sleep(2)
            print(f"Your point: {point}")
            if point<0:
                print("Yolun sonu......")
                quit()
    elif rand==3:
        print("Vurma əməlini yerinə yetirin!")
        time.sleep(2)
        firstNum = random.randint(1,20)
        secNum = random.randint(1,20)
        print(f"{firstNum}*{secNum} = ?")
        time.sleep(2)
        result = int(input("Cavab: "))
        if firstNum*secNum == result:
            print("Təbriklər! Növbəti suala keçə bilərsiniz.")
            point = point + 1
            time.sleep(2)
            print(f"Your point: {point}")
        else:
            print(f"Bəxtinizi bir daha sınayın. Doğru cavab:  {firstNum * secNum}")
            point = point - 2
            time.sleep(2)
            print(f"Your point: {point}")
            if point<0:
                print("Yolun sonu......")
                quit()
    
    elif  rand==4:
        print("Ədədin faktorialını tapın")
        time.sleep(2)
        num = random.randint(1,12)
        print(f"{num}! = ?")
        time.sleep(2)
        result=int(input("Cavab: "))
        fact = math.factorial(num)
        if fact == result :
            print("Təbriklər! Növbəti suala keçə bilərsiniz.")
            point = point + 1
            time.sleep(2)
            print(f"Your point: {point}")
        else:
            print(f"Yanlış cavab verdiyiniz üçün təbriq edilmir. Doğru cavab: {fact}")
            point = point - 2
            time.sleep(2)
            print(f"Your point: {point}")
            if point<0:
                print("Yolun sonu......")
                quit()