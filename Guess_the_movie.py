import random

movies = [
    # english                # hindi                # telugu
    "shawshank redemption", "pyaasa",              "maya bazaar",
    "godfather",             "sholay",             "c/o kancharapalem",
    "dark knight",                                   "aha naa pellanta",
    "12 angry men",          "lagaan",             "sita ramam",
    "lord of rings",         "3 idiots",           "jersey",
    "schindler's list",      "gangs of wasseypur", "nuvvu naaku nachchav",
    "pulp fiction",          "anand",              "nuvvostanante nenoddantana",
    "forrest gump",          "guide",              "magadheera",
    "fight club",            "dangal",             "eega",
    "inception",             "taare zameen par",   "baahubali",
                                                  "devadas"
]

def currentqn(picked_movie):
    temp = []
    for c in picked_movie:
        if c == " ":
            temp.append(" ")
        else:
            temp.append("*")
    return "".join(temp)

def unlock(picked_movie, current_qn, letter):
    revealed = list(current_qn)
    for i in range(len(picked_movie)):
        if picked_movie[i].lower() == letter.lower():
            revealed[i] = picked_movie[i]
    return "".join(revealed)

def play_turn(player_name):
    picked_movie = random.choice(movies)
    qn = currentqn(picked_movie)
    chances = 0
    print(f"\n{player_name}, your movie is: {qn}")

    while True:
        try:
            ch = int(input("Enter 1 to Guess the movie name or 2 to Reveal a letter: "))
        except ValueError:
            print("Please enter 1 or 2 only.")
            continue

        if ch == 1:
            guess = input("Enter your guess: ")
            chances += 1
            if guess.lower() == picked_movie.lower():
                print(f"Correct! The movie was '{picked_movie}'.")
                return chances
            else:
                print("Wrong guess. Try again.")
                print("Current movie:", qn)

        elif ch == 2:
            while True:
                letter = input("Enter a letter: ")
                chances += 1
                if letter.lower() in picked_movie.lower():
                    qn = unlock(picked_movie, qn, letter)
                    print("Updated movie:", qn)
                    if qn.lower() == picked_movie.lower():
                        print(f"{player_name} revealed the full movie!")
                        return chances
                    break  # exit inner loop once a correct letter is found
                else:
                    print("Letter not found.")
                    print("Updated movie:", qn)  # still show current progress
                    # no break → player immediately tries another letter
        else:
            print("Please enter only 1 or 2.")

def play():
    p1name = input("Enter Player 1 name: ")
    p2name = input("Enter Player 2 name: ")

    print(f"\n--- {p1name}'s Turn ---")
    p1_chances = play_turn(p1name)

    print(f"\n--- {p2name}'s Turn ---")
    p2_chances = play_turn(p2name)

    print("\n--- Results ---")
    print(f"{p1name} took {p1_chances} chances.")
    print(f"{p2name} took {p2_chances} chances.")

    if p1_chances < p2_chances:
        print(f"{p1name} wins!")
    elif p2_chances < p1_chances:
        print(f"{p2name} wins!")
    else:
        print("It's a tie!")

play()
