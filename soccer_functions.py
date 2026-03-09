# Haley Chadwick, Monica Arias, Ashlyn Crop, Zofia Lacka
# Git Hub Group Project

# Function One (Welcome Message)
def welcome() :
    home_name = input("Please enter in your team name: ")
    print((f"Welcome {home_name} to your soccer season Predictions! \n") )
    print("You will enter in the number of games you will play and your opponants name")
    return home_name


#Function Two (Playing the game)
def play_game(home_name, awayTeam):
    homeTeamScore = random.randint(0,3)
    awayTeamScore = random.randint(0,3)

    while homeTeamScore == awayTeamScore:
        homeTeamScore = random.randint(0,3)
        awayTeamScore = random.randint(0,3)

    print(f"{home_name}'s score: {homeTeamScore} - {awayTeam}'s score: {awayTeamScore}")

    if homeTeamScore > awayTeamScore:
        return "W"
    else:
        return "L"

# Function Three (Final Record)
def display_final_record(home_name, wins, losses, teamRecord, numGames):
    #Print out: Teams won against:
    #Then print out the name of each team your home team won against.
    print("Teams won against:")
    for team in teamRecord["Won Against"]:
        print(f"  {team}")

    #Print out: Teams lost against:
    print("Teams lost against:")
    for team in teamRecord["Lost Against"]:
        print(f"  {team}")

    #Print out Final season record followed by their record
    print(f"Final season record: {wins} - {losses}")

    #After all of this, print out a final message based on the record of the home team.
    winPercentage = wins / numGames
    if winPercentage >= 0.75:
        print("Qualified for the NCAA Soccer Tournament!")
    elif winPercentage >= 0.50:
        print("You had a good season.")
    else:
        print("Your team needs to practice!")


#Main Program
import random

home_name = welcome()
numGames = int(input(f"Enter the number of games that {home_name} will play: "))

wins = 0
losses = 0
teamRecord = {"Won Against": [], "Lost Against": []}

for i in range(numGames):
    awayTeam = input(f"Enter the name of the away team for game {i+1}: ")

    result = play_game(home_name, awayTeam)

    if result == "W":
        wins += 1
        teamRecord["Won Against"].append(awayTeam)
    else:
        losses += 1
        teamRecord["Lost Against"].append(awayTeam)


display_final_record(home_name, wins, losses, teamRecord, numGames)


