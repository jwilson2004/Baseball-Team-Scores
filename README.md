# Baseball-Team-Scores
A simple Python program which calls an API to retrieve today's baseball scores for your favorite team(s).

Go to `https://api-sports.io/documentation/baseball/v1` to attain a free API key.

Create an .env file and paste in `API_KEY=\<your_api_key\>`

To run the program, open the terminal and navigate to the Baseball-Team-Scores folder using `cd Baseball-Team-Scores`.

To install the necessary packages, run `pip install -r requirements.txt`

In the main function of `get_games.py`, type in your favorite baseball teams into the list `FAVORITE_TEAMS` with the format `/<city/> /<team name/>`

For example, you could put `FAVORITE_TEAMS = ["New York Mets", "Boston Red Sox"]`

To the program, enter `python3 get_games.py`  into the terminal.

You should see your output printed in the terminal and the output saved to a file called `baseball_update.txt`.



