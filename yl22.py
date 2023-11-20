import random

options = ["Kivi", "Paber", "Käärid"]

user_choice = input("Vali Kivi, Paber või Käärid: ")

computer_choice = random.choice(options)

print("Sa valisid: ", user_choice)

print("Arvuti valis: ", computer_choice)

if user_choice == computer_choice:

    print("Jääb viiki!")

elif user_choice == "Kivi" and computer_choice == "Käärid":

    print("Sa võitsid!")

elif user_choice == "Paber" and computer_choice == "Kivi":

    print("Sa võitsid!")

elif user_choice == "Käärid" and computer_choice == "Paber":

    print("Sa võitsid!")

else:

    print("Arvuti võitis!")
