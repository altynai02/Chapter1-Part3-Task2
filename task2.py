# 2. Напишите функцию который будет конвертировать
# Фаренгейт в Цельсии и наоборот.




def cel_to_fah():
    result = (temp * 9 // 5) + 32 
    return result

def fah_to_cel():
    result = (temp - 32) * 5//9 
    return result

print(" 1.Celsius to Fahrenheit")
print("2.Fahrenheit to Celsius")    
option = int(input("Hello young novice. Choose the option: "))


temp = int(input("Enter a temperature in degree: "))
if option == 1:
    print(cel_to_fah())
elif option == 2:
    print(fah_to_cel())
else:
    print("Error")
