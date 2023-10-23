a = float(input("Sisesta esimese külje pikkus: "))
b = float(input("Sisesta teise külje pikkus: "))
c = float(input("Sisesta kolmanda külje pikkus: "))
if a < b > c and c < b and c < a > b:
    if a == b and b == c and c == a:

        print("Kolmnurk on võrdliige")
    elif a == b or b == c or c == a:
        print("Kolmnurk on võrdhaarne")
    else:
        print("Kolmnurk on eriliigne")
else:
    print("Ei eksisteeri")
