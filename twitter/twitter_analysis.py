import GetOldTweets3 as got

def get_tweets():
    tweetCriteria = got.manager.TweetCriteria().setUsername("barackobama")
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
    print(tweet.text)

get_tweets()