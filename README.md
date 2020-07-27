# videoGameRecommendation
A content-based filtering recommendation system for Video Games:
- Using the data download from Games-Data-Scraping-Download project (dataForRecommendation.csv) to create an application that the users could pick a game that they have played and find out top 10 other games that are the most similar to it using Machine Learning (scikit-learn library).
- build_recommendation_model.py: Build the recommendation model from the csv file. Firstly, load the necessary data as matrix from the csv file using pandas library and numpy library. Only use the suitable column for the model: name, genres, tags, description, developers. Convert necessary data into appropriate data(genres, tags, developers to list of string (each string is a genre, tag, developer), remove unnecessary characters in the description game's name, extract key words in the description column using Rake, v.v...). Afterwards, combine all those columns into a bags of word column as a single feature. Map each of those game with that feature column onto a vector space models using Count Vectorizer transformation from the sckit-learn library. Finally, calculate each game similarity with each other using cosine similarity. Once the model has been built, save it to the recommend_cosine.npy and recommend_indices.csv for later use.  
- recommendation.py: using tkinter library to build GUI for the application. User could pick a game from the provided list that they want to recommend based upon, the pre-built model will be loaded and put out top 10 games that are the most similar to the game the user has picked.
- recommendation.exe: using pyinstaller to convert the application into an executable file.

# IMPORTANT!!! :
- Because of Github limited file size (<100mb), the recommend_cosine.npy file could not be uploaded. Therefore, user will have to run the build_recommendation_model.py to generate recommend_indices.csv and recommend_cosine.npy first before running the recommendation.exe file

# How to run:
- run build_recommendation_model.py after user has install all packages in the requirements.txt to generate the model for recommendation in two file (recommend_indices.csv and recommend_cosine.npy)
- run recommendation.exe

# Tool use:
- Python
- tkinter to create the GUI for the user.
- pandas library to load the csv file
- numpy library to convert the data from csv file to matrix.
- scikit-learn to use the Count Vectorizer transformation and cosine similarity
- rake-nltk to take out key words from the game's description
- re library to use regex to remove special character from data.
- pyinstaller convert it into an .exe file
