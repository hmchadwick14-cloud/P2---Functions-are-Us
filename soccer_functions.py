# Haley Chadwick
# Git Hub Group Project\

# Function One
def welcome() :
    home_name = input("Please enter in your team name: ")
    print((f"Welcome {home_name} to your soccer season Predictions! \n") )
    return home_name
    print("You will enter in the number of games you will play and your opponants name")


import random

home_name = welcome()
numGames = int(input(f"Enter the number of games that {home_name} will play: "))

wins = 0
losses = 0
teamRecord = {"Won Against": [], "Lost Against": []}

for i in range(numGames):
    awayTeam = input(f"Enter the name of the away team for game {i+1}: ")

    homeTeamScore = random.randint(0,3)
    awayTeamScore = random.randint(0,3)

    while homeTeamScore == awayTeamScore:
        homeTeamScore = random.randint(0,3)
        awayTeamScore = random.randint(0,3)

#Keep track of the number of wins / losses of your home team however you want.

    if homeTeamScore > awayTeamScore:
        wins += 1
    elif homeTeamScore < awayTeamScore:
        losses += 1

#You also need to keep track of the names of teams that your team won against and lost against in a dictionary.

    if homeTeamScore > awayTeamScore:
        teamRecord["Won Against"].append(awayTeam)
    elif homeTeamScore < awayTeamScore:
        teamRecord["Lost Against"].append(awayTeam)


#Print out the name of the home team’s name and their score, as well as the away team’s name and their score like this:

    print(f"{home_name}'s score: {homeTeamScore} - {awayTeam}'s score: {awayTeamScore}")

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
