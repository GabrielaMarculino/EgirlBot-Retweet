import tweepy
import time

auth = tweepy.OAuthHandler('1tJcqHPwW1Y4CUB3MEbvL4DlP','BReKYbxXrAQJQXQyTzDlmEGsNUscU5xuzPXcYwClK2NFFU8pDK')
auth.set_access_token('1268342000958537728-Y7WbbQPU6fO32mj9SPUKwaaSlbevvw','yEbfHsk7VdTcOHDcL5rMCxGpiy0EI3wOe1xyNdyd8ef9g')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'egirl'
nrTweets = 200

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Retweeted')
        tweet.retweet()
        time.sleep(300)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
