# Python Recommender

## What is it?

Python Recommender is a project I completed while studying computer science at Duke University. Taken from the instructions:

"Collaborative filtering and content-based filtering are two kinds of recommender systems that provide users with information to help them find and choose anything from books, to movies, to restaurants, to courses based on their own preferences compared to the preferences of others.

In this assignment, you'll develop a program that implements three different algorithms for recommending items based on the responses made by others.

The assignment comes in two conceptual parts:

* Reading data stored in files and converting the data into a common format
* Using the data (stored in the common format) to make recommendations for either every students/rater or for a particular student.

We're providing three sources of data. Sometimes ratings are stored in a single file, sometimes in more than one file. You'll need to write a separate Python module to deal with each data source, then use what these modules return to develop ratings." 

In this project, I have written a recommender system for food, a recommender system for books, and a recommender system for movies. Although this project contains many files, the main programs which deliver the recommendations are:
* Module RecommenderFood.py:
	* This is the main program for food recomendations. It uses Recommender.py and ReadFood.py.
* Module RecommenderBooks.py:
	* This is the main program for book recommendations. It uses Recommender.py and ReadBooks.py.
* Module RecommenderMovies.py:
	* This is the main program for movie recommendations. It uses Recommender.py and ReadMovies.py.

## Technologies Used
* Python

## Grade Received 
100%