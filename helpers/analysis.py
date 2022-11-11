import pandas as pd

def analysis():

    """
    Function to perform rudimentary analysis of our results.

    Args:
        None.
    Returns:
        None.
    """

    df = pd.read_csv('.\data\profanity_result.csv')

    print("A sample of the result")
    print(df.head(),"\n")
    print("There were a total of {} tweets in total".format(df.shape[0]))
    print("On average each tweet was {}% profane".format(round(df['degree_of_profanity'].mean(), 3)))
    print("{}% of the tweets had some sort of profanity in them".format(round((df.loc[df['degree_of_profanity']>0].shape[0])/df.shape[0] *100, 3)))