tekst = input("Sisestage tekst: ")
täishäälikud = "a, e, i, o, u, õ, ä, ö, ü"

täishäälikute_arv = 0

for word in tekst:
    if word.lower() in täishäälikud:
        täishäälikute_arv += 1

print(f"Täishäälikuid tektsis on {täishäälikute_arv}") 
