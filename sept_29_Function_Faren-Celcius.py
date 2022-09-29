def F_To_C(num):
    C = int(((num -32)*5/9))
    print(num,'Farenheight In Centirgrade is', C)
    return C

temps = [32,45,72,90, -40]

cel = []

for num in temps:
    cel.append(F_To_C(num))

print('Here is your list of tempratures in Celsius: ',cel)

