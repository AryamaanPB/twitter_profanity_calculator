import pandas as pd

def get_tweets():

    """
    Function to load all tweets as a dataframe.

    Args:
        None
    Returns:
            list_tweets (list) : A list of all tweets
    """

    df = pd.read_csv(".\data\labeled_data.csv")
    list_tweets = df['tweet'].tolist()

    return list_tweets