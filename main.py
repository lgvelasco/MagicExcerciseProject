print("Your are in the magic maze. Which way to go? (N, S, E, W")

solution = ["S", "S", "W", "N", "E", "S"]
index = 0
moves = 0
lives = 3

flag = True

while flag:

    command = input("Enter direction: ")

    if command == solution[index]:
        print("Correct!!")
        print("Moves: ", moves)
        print("Lives: ", lives)
        index += 1
        moves += 1
    else:
        print("Incorrect")
        moves += 1
        print("Moves: ", moves)
        print("Lives: ", lives)
        index = 0

    if index == len(solution):
        print("You escaped the maze in ", moves, "moves")
        flag = False

    if moves % 10 == 0:
        lives = lives - 1

    if lives == 0:
        print("You ran out of lives")
        flag = False