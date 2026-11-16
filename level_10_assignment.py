import pandas as pd     #importing the pandas functions

#filtering the data by whatever year the user decides to enter
football_data = pd.read_csv("/Users/zacharychichoni/Downloads/cfb.csv")

target_season = int(input("Enter a season to analyze: "))

season_football_data = football_data[football_data["Season"] == target_season]

#Making sure the year entered is valid and found in the spreadsheet
while season_football_data.empty:
    print(f"Sorry, {target_season} season is not registered ")
    target_season = int(input("Enter a season to analyze: "))
    season_football_data = football_data[football_data["Season"] == target_season]

#Creating the option dictionary to add the teams to later
else:
    win_categories = {
        "10 or more wins": [],
        "8 - 9 wins": [],
        "6 - 7 wins": [],
        "Fewer than 6 wins": []

    }

#Filtering the teams by the amount of wins they have and adding them to their appropriate categories
    for index, row in season_football_data.iterrows(): 
        team_name = row["Team"]
        wins = row["Win"]


        if wins >= 10:
            win_categories["10 or more wins"].append(team_name)
        elif wins >= 8:
            win_categories["8 - 9 wins"].append(team_name)
        elif wins >= 6: 
            win_categories["6 - 7 wins"].append(team_name)
        elif wins < 6:
            win_categories["Fewer than 6 wins"].append(team_name)


#Displayinfg the filtered data for the user to see
    print(f"College football results for the {target_season} ")

    for category, teams in win_categories.items():
     print(f"\n{category}:")      
    
     for team in teams:
        print(f"  {team}")        
