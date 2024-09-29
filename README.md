<p align='center'>
    <img height='400' src='https://user-images.githubusercontent.com/31500911/143410521-b2653b16-0ee9-46e7-9c5c-7a8b2262a3d1.png'>
</p>

# Model Deployment using Streamlit

In this project, I have built a content-based movie recommender system. The algorithm recommends movies that are similar to those a user has liked in the past. This similarity (typically cosine similarity) is computed from the data we have about the items and the user’s past preferences.

## What it does

<p align='center'>
    <img height='400' src='https://user-images.githubusercontent.com/31500911/145380710-1813c6e7-7635-47a6-b764-c4bd3315c9c1.png'>
</p>

## Live Demo

<p align='center'>
    <img height='400' src='https://user-images.githubusercontent.com/31500911/143416246-4bc98d07-12fa-404a-a98c-228eaaa6ef5c.gif'>
</p>

## How it works

Content-Based Filtering - This recommender system suggests similar items based on a particular item. It uses item metadata, such as genre, director, description, actors, etc., for movies, to make these recommendations. The core idea behind content-based recommender systems is that if a person liked a particular item, they are likely to enjoy other items that are similar.

## How to get the API key for images?

To obtain an API key for accessing movie data, follow these steps:

1. Create an account at [The Movie Database (TMDB)](https://www.themoviedb.org/).
2. Navigate to your account settings and click on the API link from the left-hand sidebar.
3. Fill in the required details to apply for an API key. If asked for a website URL, enter "NA" if you don't have one.
4. Once your request is approved, you will find the API key in the API section of your account settings.

<p align='center'>
    <img src='https://user-images.githubusercontent.com/31500911/143419982-2d726687-84d6-4616-8d09-833f732c92b2.png'>
</p>

## How to run the program

Run the following command to set up and start the application:

```
bash
sh setup.sh && streamlit run app.py
```
## Similarity Score
How does the system decide which movie is most similar to the one the user likes? It uses similarity scores.

A similarity score is a numerical value between 0 and 1 that helps determine how similar two movies are. This score is obtained by measuring the similarity between the text details of both movies using cosine similarity.

<p align='center'> <img src='https://user-images.githubusercontent.com/31500911/143418326-9ed3e46a-5ddd-46dc-86fc-8b145101af52.png'> </p>
How Cosine Similarity works
Cosine similarity is a metric used to measure how similar two documents are, regardless of their size. It measures the cosine of the angle between two vectors projected in a multi-dimensional space. Cosine similarity is advantageous because even if two documents are far apart by Euclidean distance, they may still be oriented closely in terms of their cosine similarity. The smaller the angle, the higher the similarity.

<p align='center'> <img src='https://user-images.githubusercontent.com/31500911/143417796-8602832b-aac9-4f4f-b930-b753dc050981.png'> </p>

## Dataset
I used the TMDB 5000 movies dataset to build the model.

You can download the dataset from Kaggle.
https://www.kaggle.com/tmdb/tmdb-movie-metadata
