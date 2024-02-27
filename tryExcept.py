import time

while True:
    num = input("Bir rəqəm daxil edin! ")
    try:
        num = float(num)
        time.sleep(1)
        
    except:
        print("Daxil edilən dəyər düzgün formatda deyil!")
        time.sleep(2)
    print(num**2)