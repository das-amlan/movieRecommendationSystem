# Movie Recommendation System
End To End Machine Learning Implementation of a movie recommendation system


## Dataset Overview
The recommendation system utilizes the TMDB Movie Metadata dataset from Kaggle, a comprehensive collection of movie information including titles, genres, cast and crew details, release dates, ratings, and much more. This dataset offers a wide array of attributes that form the basis for our intelligent recommendation system. With information spanning over several decades, the dataset presents a wealth of cinematic content, allowing us to a recommendation system from broad selection of movies.

- Dataset: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## Libraries Used

The movie recommendation system is implemented using several libraries:

- **numpy**: `NumPy` is a library for the Python programming language that provides support for large, multi-dimensional arrays and matrices. It is used for numerical computations and data manipulation in this project.

- **pandas**: `Pandas` is a powerful data analysis and manipulation library. It provides data structures and functions for efficiently handling and analyzing structured data. In this project, Pandas is used for loading and preprocessing the movie dataset.

- **nltk.stem.porter**: `NLTK` (Natural Language Toolkit) is a library for natural language processing in Python. The `PorterStemmer` class from NLTK is used for stemming, which is the process of reducing words to their base or root form. It helps in improving the accuracy of text-based features in content-based filtering.

- **sklearn.feature_extraction.text**: `Scikit-learn` is a popular machine learning library in Python, and the `CountVectorizer` class from `sklearn.feature_extraction.text` is used to convert text data (such as movie plots) into numerical feature vectors. It tokenizes the text and builds a vocabulary of known words, assigning a numerical value to each word.

- **sklearn.metrics.pairwise**: This module from scikit-learn provides various distance metrics and pairwise similarity computations. In this project, the `cosine_similarity` function from this module is used to calculate the cosine similarity between feature vectors. It helps in measuring the similarity between movies based on their content features.

- **pickle**: The `pickle` module in Python is used for object serialization and deserialization. In this project, it is used to save and load trained models or intermediate data structures.

- **streamlit**: `Streamlit` is a Python library used for building interactive web applications for machine learning and data science. It simplifies the process of creating web interfaces for your projects. In this project, Streamlit is used to deploy the movie recommendation system as a web application.

- **requests**: The `requests` library is used for making HTTP requests in Python. It allows your code to interact with web APIs or retrieve data from remote servers. In this project, it is used for fetching movie data from an external API.



