name = input("Sisestage oma nimi: ")
print("Tere!", name)

area = input("Sisestage oma elukoht: ")
if "saaremaa" in area.lower():
        print("Tervist saarlane!")
else:
     print("Kao seenele kusipää")

age = int(input("Sisestage oma vanus: "))
if age < 18:
    print("Sa oled liiga noor, et autot juhtida")
elif age == 18:
    print("Palju õnne täisealiseks saamise eest!")
else:
     print("Sa võid autot juhtida big boy :)")
