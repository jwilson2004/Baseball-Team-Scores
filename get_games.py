from requests import get
# from pprint import PrettyPrinter
from datetime import datetime, date
import pytz
from dotenv import load_dotenv
import os

def get_response():
    payload={}
    headers = {
    'x-rapidapi-key': API_KEY,
    'x-rapidapi-host': 'v1.baseball.api-sports.io'
    }

    params = {
        'date': date.today().strftime("%Y-%m-%d")
    }

    response = get(BASE_URL, headers=headers, params=params, data=payload).json()
    return response


def filter_games(response, favorite_teams): 
    games = response['response']

    favorite_games = filter(lambda x: x['teams']['home']['name'] in favorite_teams
                                    or x['teams']['away']['name'] in favorite_teams,
                                    games)

    print(type(favorite_games))
    return favorite_games
    
def get_email_body(favorite_games):
    games_report = ""
    for game in favorite_games:
        print(game)
        
        home_team = game['teams']['home']['name']
        away_team = game['teams']['away']['name']
        home_team_score = 0 if game['scores']['home']['total'] is None else game['scores']['home']['total']
        away_team_score = 0 if game['scores']['away']['total'] is None else game['scores']['away']['total']

        games_report += (
        f"--------------------------\n"
        f"{home_team} (Home) vs. {away_team} (Away)\n"
        f"{home_team_score} - {away_team_score}\n"
        f"{game['status']['long']}\n"
        f"Started at {utc_to_pst(game['time'])}\n"
        "--------------------------\n"
        )
    return "There were no games played by your favorite teams." if games_report == "" else games_report

def utc_to_pst(utc_time_str):
    # Combine with today's date to create a full datetime string
    today = date.today().strftime("%Y-%m-%d")
    full_utc_str = f"{today} {utc_time_str}"

    # Parse the full UTC datetime
    utc = pytz.utc
    utc_dt = utc.localize(datetime.strptime(full_utc_str, "%Y-%m-%d %H:%M"))

    # Convert to Pacific time (automatically handles daylight saving time)
    pacific = pytz.timezone("US/Pacific")
    pacific_dt = utc_dt.astimezone(pacific)

    # Return formatted time in 12-hour format with AM/PM
    return pacific_dt.strftime("%I:%M %p").lstrip("0")

def write_to_file(games_report):
    filename="baseball_update.txt"
    with open(filename, "w") as f:
        f.write(games_report)

if __name__ == '__main__':
    # Load .env file variables
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    BASE_URL = 'https://v1.baseball.api-sports.io/games'
    FAVORITE_TEAMS = ["New York Mets", "Boston Red Sox"]
    
    response = get_response()
    
    games = filter_games(response, FAVORITE_TEAMS)
    games_report = get_email_body(games)
    print(games_report)
    write_to_file(games_report)




