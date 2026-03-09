# Haley Chadwick, Monica Arias, Ashlyn Crop, Zofia Lacka
# Git Hub Group Project

# Function One (Menu)
# Displays the program menu and returns the user's choice
def menu():
    print("\nMenu")
    print("1. Play Soccer Season")
    print("2. Exit Program")

    choice = input("Enter your choice: ")
    return choice


# Function Two (Welcome Message)
# Asks the user for the home team name and prints a welcome message
def welcome():
    home_name = input("Please enter in your team name: ")
    print((f"Welcome {home_name} to your soccer season Predictions! \n"))
    print("You will enter in the number of games you will play and your opponents name")
    return home_name


# Function Three (Playing the game)
# Simulates a game between the home team and away team
# Generates random scores and ensures there are no ties
# Returns "W" if the home team wins and "L" if they lose
def play_game(home_name, awayTeam):

    # Generate random scores between 0 and 3
    homeTeamScore = random.randint(0,3)
    awayTeamScore = random.randint(0,3)

    # Repeat score generation if there is a tie
    while homeTeamScore == awayTeamScore:
        homeTeamScore = random.randint(0,3)
        awayTeamScore = random.randint(0,3)

    # Display the score of the game
    print(f"{home_name}'s score: {homeTeamScore} - {awayTeam}'s score: {awayTeamScore}")

    # Determine win or loss
    if homeTeamScore > awayTeamScore:
        return "W"
    else:
        return "L"


# Function Four (Final Record)
# Displays the final season results including wins, losses,
# teams beaten, teams lost to, and a season summary message
def display_final_record(home_name, wins, losses, teamRecord, numGames):

    # Print the teams the home team won against
    print("Teams won against:")
    for team in teamRecord["Won Against"]:
        print(f"  {team}")

    # Print the teams the home team lost against
    print("Teams lost against:")
    for team in teamRecord["Lost Against"]:
        print(f"  {team}")

    # Print the final record
    print(f"Final season record: {wins} - {losses}")

    # Calculate win percentage
    winPercentage = wins / numGames

    # Display a message based on season performance
    if winPercentage >= 0.75:
        print("Qualified for the NCAA Soccer Tournament!")
    elif winPercentage >= 0.50:
        print("You had a good season.")
    else:
        print("Your team needs to practice!")


# -------------------------
# Main Program
# -------------------------

import random

# Loop keeps program running until user chooses to exit
while True:

    # Display menu and get user choice
    choice = menu()

    # Option 1: Play a soccer season
    if choice == "1":

        # Get the home team name
        home_name = welcome()

        # Ask how many games will be played
        numGames = int(input(f"Enter the number of games that {home_name} will play: "))

        # Initialize win/loss counters
        wins = 0
        losses = 0

        # Dictionary to track teams won against and lost against
        teamRecord = {"Won Against": [], "Lost Against": []}

        # Loop through each game in the season
        for i in range(numGames):

            # Ask for the opponent team
            awayTeam = input(f"Enter the name of the away team for game {i+1}: ")

            # Play the game and store result
            result = play_game(home_name, awayTeam)

            # Update win/loss counters and dictionary
            if result == "W":
                wins += 1
                teamRecord["Won Against"].append(awayTeam)
            else:
                losses += 1
                teamRecord["Lost Against"].append(awayTeam)

        # After all games, display the final season results
        display_final_record(home_name, wins, losses, teamRecord, numGames)

    # Option 2: Exit the program
    elif choice == "2":
        print("Goodbye!")
        break

    # Handle invalid menu choices
    else:
        print("Invalid choice. Please try again.")