sisend_string = input("Sisesta string: ")

eemaldatud_stringid = sisend_string.strip()

if len(eemaldatud_stringid) >= 7 and len(eemaldatud_stringid) % 2 != 0:
    keskmised_sumbolid = eemaldatud_stringid[len(eemaldatud_stringid) // 2 - 1 : len(eemaldatud_stringid) // 2 + 2]
    print("Kolm keskmist sümbolit:", keskmised_sumbolid)
else:
    print("Sisestatud string ei vasta tingimustele.")
