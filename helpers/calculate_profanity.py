import re
import json
import pandas as pd

def _get_profane_tokens():

    """
    Function to load all the pre determined profane words.

    Args:
        None
    Returns:
        profane_tokens (list) : A list of all pre determined profane words.
    """

    config_file = open('.\config\config.json')
    config_dict = json.load(config_file)

    profane_tokens = config_dict['profane_tokens']

    return profane_tokens

def _get_degree_of_profanity(profane_tokens,tweet):  

    """
    Function to calculate the degree of profanity for each tweet.

    Args:
        profane_tokens (list) : A list of all pre determined profane words.
        tweet (str) : A string containing a single tweet.

    Returns:
        degree_of_profanity (float) : A percentage of profanity in a single tweet.
    """

    match_profane_tokens = []
    span_profane_tokens = []

    for pt in profane_tokens:
        match = re.search(pt, tweet)
        if(match!=None):
            match_profane_tokens.append(match[0])
            span_profane_tokens.append(match.span()[0])
            span_profane_tokens.append(match.span()[1])

    sum_profanity = len(match_profane_tokens) - abs(len(span_profane_tokens) - len(set(span_profane_tokens)))

    degree_of_profanity = (sum_profanity / len(tweet.split()))*100

    return degree_of_profanity

def _save_dataframe(result_pd):

    """
    Saving the result dataframe as a csv.

    Args:
        result_pd (pandas.dataframe) : A dataframe containing the tweets and their degree of profanity
    Returns:
        None.
    """

    result_pd.to_csv('.\data\profanity_result.csv', index = False)

def calculate_profanity(list_tweets):

    """
    Main function to calculate profanity for all tweets.

    Args:
        list_tweets (list) : A list of all tweets.
    Returns:
        None.
    """

    list_degree_of_profanity = []

    profane_tokens = _get_profane_tokens()

    for tweet in list_tweets:
       list_degree_of_profanity.append(_get_degree_of_profanity(profane_tokens,tweet))

    result_pd = pd.DataFrame(
        {
            'tweet': list_tweets,
            'degree_of_profanity': list_degree_of_profanity,
        }
    )

    _save_dataframe(result_pd)