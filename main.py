from helpers.analysis import analysis
from helpers.calculate_profanity import calculate_profanity
from helpers.get_tweets import get_tweets

def main():

    """
    Main file to run the entire workflow:
        1. Loading the tweets
        2. Calculating the degree of profanity
        3. Analysing the result

    Args:
        None
    Returns:
        None
    """
    print("Loading the tweets")
    list_tweets = get_tweets()

    print("Calculating degree of profanity for each tweet")
    calculate_profanity(list_tweets)

    print("Analysing the result")
    analysis()

if __name__ == "__main__":
    main()