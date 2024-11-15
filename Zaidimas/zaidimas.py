import random

choices = ["akmuo", "popierius", 'zirkles']

player_choice = input("Pasirinkite: akmuo, popierius ar zirkles: ").lower()

computer_choice = random.choice(choices)
print(f"Jus pasirinkote: {player_choice}")
print(f"Kompiuteris pasirinko: {computer_choice}")

if player_choice == computer_choice:
    print("Lygiosios!")
elif (player_choice == "akmuo" and computer_choice == "zirkles") or \
            (player_choice == "popierius" and computer_choice =="akmuo") or \
            (player_choice == "zirkles" and computer_choice == "popierius"):
        print ("Jus laimejote")
else:
    print("Kompiuteris laimejo")