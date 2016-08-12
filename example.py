import tweepy
import csv

# API key information
CUSTOMER_KEY = ''
CUSTOMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

# tweepy API authorization
auth = tweepy.OAuthHandler(CUSTOMER_KEY, CUSTOMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def get_tweets(screen_name):
  # Hold tweepy tweets
  tweets = []

  # Grab and store most recent tweets (200 is max allowed)
  new_tweets = api.user_timeline(screen_name = screen_name, count = 200)
  tweets.extend(new_tweets)

  # Hold id of oldest tweet
  oldest = tweets[-1].id - 1

  # Get tweets until none are left
  while len(new_tweets) > 0:
    print 'getting tweets before %s' % (oldest)

    # Save the newest tweets again
    new_tweets = api.user_timeline(screen_name = screen_name,
      count = 200, max_id = oldest)
    tweets.extend(new_tweets)

    # Update id of oldest tweet
    oldest = tweets[-1].id

    print '...%s tweets downloaded so far' % (len(tweets))
    print '%s tweets left to parse...' % (len(new_tweets))

  # Transform tweets into 2D array for CSV
  csvtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in tweets]

  # Write to CSV
  with open('%s_tweets.csv' % screen_name, 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'created_at', 'text'])
    writer.writerows(csvtweets)

  pass

def test_tweet():
  # Generic tweet test
  api.update_status('tweet tweet am burb bot plz feed me quack')

  print 'Done'

def get_feed():
  public_tweets = api.home_timeline()
  for tweet in public_tweets:
    print tweet.text

if __name__ == '__main__':
  screen_name = raw_input('Enter a feed: ')
  get_tweets(screen_name)
  print 'Done!'