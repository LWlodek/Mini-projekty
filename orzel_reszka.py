import time, random

print("""
Witaj, zagrajmy w grę orzeł - reszka! Zgadnij co wypadnie w następnym rzucie.
Wygrywa ten, kto jako pierwszy zdobędzie 3 punkty.
""")

user_score = 0
computer_score = 0

while user_score < 3 and computer_score < 3:
    user_choice = input("Podaj swój wybór, możliwe opcje to o (orzeł), r (reszka), stop (wyjście)")
    if user_choice == "o":
        user_choice = "Orzeł"  
    elif user_choice == "r":
        user_choice = "Reszka"
    elif user_choice == "stop":
        break
    else:
        print("Wybrano niewłaściwą opcję, spróbuj ponownie)")
        continue

    print("Twój wybór to " + user_choice + " rzucam monetą!")
    czas = 3
    while czas > 0:
        time.sleep(1)
        print(czas)
        czas -=1
    draw = random.choice(["Orzeł","Reszka"])
    print()
    print("Wynik rzutu: " + draw)
    print()
    if user_choice == draw:
        user_score +=1
        print("Zdobywasz punkt! Obecny wynik gracz:komputer", user_score, ":", computer_score)
    else:
        computer_score +=1
        print("Punkt dla komputera. Obecny wynik gracz:komputer", user_score, ":", computer_score)
if user_score == 3:
    print("Zwycięstwo! wynik rozgrywki gracz - komputer to ", user_score, ":", computer_score)
elif computer_score == 3:
    print("Porażka! wynik rozgrywki gracz - komputer to ", user_score, ":", computer_score)
else:
    print("Gra przerwana przed zakończeniem.")