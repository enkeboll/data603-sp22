# Movie Recommendation System 

## Project Description

Recommendation engines play a critical role in customer engagement and retention for online media and entertainment     industry.
 
Recommendation system is a system that seeks to predict or filter preferences according to the user’s choices.It       helps to personalize user experience to find something they like.

RecommendationEnginesaretheprogramswhichbasicallycomputethesimilaritiesbetweentwo entities and on that basis, they     give us the targeted output.

This movie recommendation system recommends movies to a user or a client by evaluating dataset.

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

## Spark MLlib

• MLlib is Spark’s scalable machine learning library consisting of common learning algorithms and utilities.

• It includes classification, regression, clustering, collaborative filtering, dimensionality reduction, as well as underlying optimization primitives.

• SparkMLalsoworkswellwithmodeltrainingandproduction,sothosemodelstrainedcaneasilybe deployed to production.

## Collaborative Filtering Movie Recommendation Systems

Collaborative Filtering is commonly used for recommender systems. It tackles the similarities between the users and items to perform recommendations. The algorithm constantly finds the relationships between the users and does the recommendations.

• Apache Spark ML implements alternating least squares (ALS) for collaborative filtering, a very popular algorithm for   making recommendations.

• Implemented Alternating Least Square(ALS) with Spark. ALS is a matrix factorization technique to perform               collaborative filtering. The objective function of ALS uses L1 regularization and optimizes the loss functions
  using Gradient Descent.

• We train the ALS model by tuning the below hyper-parameters: Rank , Reg Parameters & Maximum iterations.

• To measure the errors for each value of rank and store the index of error values, best rank values and best iteration value.

## Implementation

Step 1 : Loading the Netflix data on Spark. Installing and Importing all the relevant libraries.

<p align="center">
 <img width="555" alt="Screen Shot 2022-05-12 at 2 21 42 PM" src="https://user-images.githubusercontent.com/89950200/168143753-1b000ba2-f1de-443e-9501-c304d4f3dd71.png">
 </p>

Step 2 : Collecting the data and mounting the data file to Google Collaboratory.

<p align="center">
  <img  height="300" width="590" alt="Screen Shot 2022-05-12 at 1 45 10 PM" src="https://user-images.githubusercontent.com/89950200/168140058-ab448409-9f74-474b-975b-3b1b2c5f4d69.png">
</p>

Step 3 : Starting the spark kernel :

<p align="center">
<img width="788" alt="Screen Shot 2022-05-12 at 2 22 40 PM" src="https://user-images.githubusercontent.com/89950200/168143223-1b0635be-b6eb-456c-83ac-71997d17884f.png">
 </p>

Step 4 : Merging all the data files into a single file and reading the data.


Step 5 : Creating RDDs (Resilient Distributed Dataset) is a low-level object and are highly efficient
in performing distributed tasks.

 Step 6 : Performing Exploratory Data analysis on the dataset to check the duplicate entries and unnecessary columns. The dataset has been cleaned.

## Plotting graphs based on ratings distribution:

<p align="center">
  <img height="300" width="489" alt="Screen Shot 2022-05-05 at 1 19 35 PM" src="https://user-images.githubusercontent.com/89950200/168140530-82b05f76-feaf-4b2d-9dcd-0f6d4b302b13.png">
">
</p>

<p align="center">
  <img width="549" alt="Screen Shot 2022-05-05 at 1 23 46 PM" src="https://user-images.githubusercontent.com/89950200/168140654-cf4533ee-3238-4813-aaf1-8dc164e67372.png">
</p>

Step 7 : To Validate and perform test splitting for training Machine Learning model and finding best hyper parameter   to find RMSE on test data.

                                       (We are using ALS Algorithm here.)
                               

Step 8 : Now , after finding the best hyper parameter. We are creating a new user to get movie recommendations, with a new user ID .

Step 9 : Training the model with the merged data to get a new model to predict ratings for movies not yet watched by the user.

Step 10 : Recommending top 10 movies to the new user.

# Visualization

Creating visualisation of recommended movies(x-axis) vs movie counts (y-axis).

<p align="center">
  <img height="300" width="694" alt="Screen Shot 2022-05-05 at 1 42 58 PM" src="https://user-images.githubusercontent.com/89950200/168142518-fcc55d50-4d9f-4c03-964f-57d2bfaa40e5.png">
</p>

<p align="center">
  <img height="300"  width="659" alt="Screen Shot 2022-05-05 at 1 43 25 PM" src="https://user-images.githubusercontent.com/89950200/168142619-2190e7ad-24f1-469b-afa4-7f874af46996.png">
</p>

## Conclusion and Learnings

• Learnt to develop a recommendation system using Spark with the help of Python.

• Recommended movies for the users based on the previous ratings provided by them.
