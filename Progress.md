# Project description 

For the online media and entertainment industry, recommendation engines are crucial for client engagement and retention.
Recommendation Engines are programs that compute the similarities between two items and then provide us with the desired results.
This movie recommendation system evaluates a data set to make movie recommendations to a user or client.

## Problem Statement

Create a movie recommendation system based on user feedback.
System of general recommendations:
In terms of recommendations, we always propose movies with the highest average rating and more than a specified amount of ratings using this method.
Recommendation system based on user input:
Similarities between user ratings were used to forecast the user's recommendations.

## Data Source

https://www.kaggle.com/netflix-inc/netflix-prize-data

## Real world/Business Objectives and constraints

Objectives: 
* Predict a user's rating for a movie he hasn't seen yet;
* Recommend top 10 movies appropriate for the user;
* Minimize the discrepancy between expected and actual rating (RMSE)

Constraints:

* Some level of interpretability is required.

  ## Proposed Solution

Exploratory Data Analysis on the Netflix data set can be done by loading the Netflix data set into Spark.

* Train, validate, and split your tests.
* Finding the appropriate hyperparameter for a
machine learning model.
* Predicting user ratings for movies they haven't seen yet.
* Visualization in action.

We could use tools in Spark's scalable machine learning library.
* Basic optimization primitives such as classification, regression, clustering, collaborative filtering, dimensionality reduction, and classification are all covered.
* Model training and production are also compatible with Spark ML, allowing trained models to be swiftly deployed to production.
