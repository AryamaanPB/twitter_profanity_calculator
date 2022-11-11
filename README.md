# Degree of Profanity in a Tweet
#### Aryamaan Singh

Through this code I have tried to calculate the percentage of profanity used in tweets. This percentage is calculated against a list of pre-defined profane words.
This is a great way to not only try to filter out messages (tweets) on your application (Twitter) to be further processed (deleted, banned or blacklisted).

## Pre-requisites
```sh
pip install pandas
```

## How it works

- First loads up the tweets that I got from [this](https://www.kaggle.com/datasets/mrmorj/hate-speech-and-offensive-language-dataset) labelled dataset I got from Kaggle.
- Loads up a list of pre defined profane tokens.
- Iterates over the list of tweets and calculates the degree of profanity for each.
- Saves the result as a csv.
- Performs rudimentary analysis about the result.

Here is what your sample output should look like:
![Alt text](/img/sample_output.jpg?raw=true "Sample Output")


