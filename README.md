# State Trivia!
State Trivia! Is a flashcard style quiz game that is intended to help students or anybody memorize state capitals and mottos. 
Based on Material Design and minimalist gameplay, this app sets out to be easy to play, intuitive, and help users memorize state capitals and mottos quicker. 
The goal of the app is also to be a quick experience that a user can play anytime they have a couple of free minutes, making it a great companion on commutes, waiting in line, or when nature calls.

# Technologies

* Django
* Postgres
* Materialize CSS
* HTML/ Javascript/ CSS
* Python
* Heroku (For deployment and server hosting)

# Install 
Fork and clone repo to your local computer.

Open the root folder of the project in your terminal and run the following commands:

```python3 -m venv .env```

```source .env/bin/activate``` 

```pip3 install -r requirements.txt```

```createdb statetrivia```

```python3 manage.py migrate```

```python3 manage.py loaddata state_data.json```

You should now be able to run the project locally by using the command ```python3 manage.py runserver``` and opening localhost:8000 on your browser.

# User Stories:

# MVP. As a user:
* I want to play a simple game that helps me learn state capitals.
* I want this game to give me multiple choice options when playing.
* I want this game to keep track of how many times I’ve answered correctly and incorrectly.
* I want to be able to create an account to keep track of my progress.
* I want to be able to see my global scores after I finish a game.
* I want the app to be primarily a mobile experience.

# Silver. As a user:
* I want the app to have a game mode that helps me learn state mottos.
* I want to be able to edit my username and password.
* I want the app to be a clean minimalist experience that won’t distract me too much.

# Gold. As a user:
* I want the app to have a hard mode difficulty.
* I want this difficulty to only show me a state silhouette with no multiple choice options. It should ask me to input the state name, state motto, and state capital. A correct answer in this mode only counts if you get all 3 answers correctly.
* I want to compete with other users, and have a high score section, or leaderboard.
* I want a desktop version of the app.


# Stretch Goals. As a user:
* I want a game mode that helps me learn the state flags.
* I want a game mode that helps me memorize state GDPs.

# Mock Up / Wireframes

[Click This Link to View the Interactive Adobe XD mock up on your browser](https://xd.adobe.com/view/8433e3eb-0b53-4677-b733-88eca7fca1e5-d160/?fullscreen "Title").
