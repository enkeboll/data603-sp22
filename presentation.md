# Movie Recommendation System 

## Project Description

•Recommendation engines play a critical role in customer engagement and retention for online media and entertainment     industry.
 
• Recommendation system is a system that seeks to predict or filter preferences according to the user’s choices.It       helps to personalize user experience to find something they like.

• RecommendationEnginesaretheprogramswhichbasicallycomputethesimilaritiesbetweentwo entities and on that basis, they     give us the targeted output.

• This movie recommendation system recommends movies to a user or a client by evaluating dataset.

## Problem Statement

• Build a movie recommendation system based on the user ratings.

• General recommendation system :As for recommendation , for this method ,we always recommend those movies with the     highest average rating and more than certain number of ratings.

• User based recommendation system :Used similarities between the user ratings and predicted recommendations for the     user.

## Objectives :

Implement a collaborative- filtering approach to recommend movies to user.

Predict the rating that a user would give to a movie that he has not yet rated.

Recommend top 10 movies suitable to the user.

Minimize the difference between predicted and actual rating (RMSE).

## Dataset Description : 

The data set we used for this project is from this source : https://www.kaggle.com/netflix-inc/netflix-prize-data/data  
For this project, I have utilized four datasets :

• The first dataset is TRAINING DATASET FILE where it provides a directory containing 17770 files, one per movie. The first line of each file contains the movie id followed by a colon. Each subsequent line in the file corresponds to a rating from a customer and its date in the following format: Customer-ID, Rating, Date.

• The second dataset is MOVIES FILE where there is Movie information in "movie_titles.txt" is in the following format: Movie ID, Year Of Release, Title.

• The Third dataset is QUALIFYING AND PREDICTION DATASET FILE where it consists of lines indicating a movie id, followed by a colon, and then customer ids and rating dates, one per line for that movie id. The movie and customer ids are contained in the training set. Of course the ratings are withheld. There are no empty lines in the file.

• The fourth dataset is the PROBE DATASET FILE where it allows you to test your system before you submit a prediction set based on the qualifying dataset, we have provided a probe dataset in the file "probe.txt". This text file contains lines indicating a movie id, followed by a colon, and then customer ids, one per line for that movie id.
