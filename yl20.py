number = int(input ("Sisesta number 1-12: "))

for i in range(0,13):
    answer = i * number
    print(f"{number} x {i} = {answer}")
