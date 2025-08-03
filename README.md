# Optimized-Spotify-Listening-Design

Helped create a more personalized listening experience while also addressing biases in music apps such as Spotify by creating a Python-fueled machine-learning algorithm that takes in a dataset of songs, sorts them based on user input, and outputs the songs that best fit the user's choice.

## Problem Statement <!--- do not change this line -->

Music is and always has been an integral part of our daily lives; however, we find that music listening may not always fit the liking of the user, which is an issue we hope to reveal and address.

## Key Results <!--- do not change this line -->

1. Within the dataset of Most Streamed Songs, the songs were skewed in danceability, energy, and acousticness, with songs mostly having high danceability and energy but low acousticness.
2. Cluster plot of danceability and acousticness displays a strong preference for electronic songs with high danceability.
3. Cluster plot of danceability and acousticness displays a strong preference for songs with high danceability and energy.
4. Displays a possible bias in popular Spotify songs, as they may favor specific artists or genres.

## Methodologies <!--- do not change this line -->

To accomplish this, I first cleaned a dataset of Spotify's most streamed songs and used Jupyter Notebook to create histograms as well as cluster plots to see the possible biases that may be present in this specific dataset. In order to tackle said bias, I designed a Python script which takes in specific user input and based on this input, the algorithm outputs the song based on their preference, NOT based on popularity. Successfully tackles bias by factoring out popularity and outputting songs solely based on the preference described by the user.

## Data Sources <!--- do not change this line -->

Kaggle Dataset: [Spotify Most Streamed Songs]([https://www.kaggle.com/datasets](https://www.kaggle.com/datasets/abdulszz/spotify-most-streamed-songs/data))*

## Technologies Used <!--- do not change this line -->

- *Python*
- *Jupyter Notebook*
- *CSV File*
- *pandas*
- *matplotlib*
- *scikit-learn*
- *seaborn*


## Authors <!--- do not change this line -->

(UPDATE IN README.md)

*This project was completed by:*
- *Giselle Muriel ([gisellemuriel123@gmail.com](mailto:gisellemuriel123@gmail.com))*
