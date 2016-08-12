import csv
import os
import tweepy

class TwitterScraper:
  'Scrapes twitter feeds using tweepy API'

  # API key information (use your own!)
  CUSTOMER_KEY = ''
  CUSTOMER_SECRET = ''
  ACCESS_KEY = ''
  ACCESS_SECRET = ''

  # tweepy API authorization
  auth = tweepy.OAuthHandler(CUSTOMER_KEY, CUSTOMER_SECRET)
  auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
  api = tweepy.API(auth)

  # Twitter Bot screen_name
  screen_name = ''

  # Cache most recent twitter feed
  mostRecentFeed = {
    'screen_name' : '',
    'tweets' : [],
  }

  def __init__(self):
    pass

  # Helper for caching tweets
  def __add_tweets(self, screen_name, tweets):
    # Empty cache
    self.mostRecentFeed['tweets'] = []
    # Fill cache
    self.mostRecentFeed['screen_name'] = screen_name
    for tweet in tweets:
      self.mostRecentFeed['tweets'].append(tweet)

  # Get cached screen_name
  def get_cached_screen_name(self):
    return self.mostRecentFeed['screen_name']

  # Get current cached tweets (reverse chronological)
  def get_cached_tweets(self):
    tweets = []
    for tweet in self.mostRecentFeed['tweets']:
      tweets.append(getattr(tweet, 'text').encode('ascii', 'ignore'))
    return tweets
    # Chronological order (if it really matters)
    # return tweets[::-1]

  # Get twitter feed associated with API key (up to 20 most recent)
  def get_home_feed(self):
    public_tweets = self.api.home_timeline()
    self.__add_tweets(self.screen_name, public_tweets)
    return self.get_cached_tweets()
    # Raw tweet data (array of Status objects)
    # return self.mostRecentFeed['tweets']

  # Get tweets from a given @user (up to 3240 from most recent tweet)
  def get_usr_feed(self, screen_name):
    # Hold tweets to be cached
    tweets = []

    # Grab and store most recent tweets (200 is max allowed)
    new_tweets = self.api.user_timeline(screen_name = screen_name, count = 200)
    tweets.extend(new_tweets)

    # Hold id of oldest tweet
    oldest = tweets[-1].id - 1

    # Get tweets until none are left
    while len(new_tweets) > 0:
      # Save the newest tweets again
      new_tweets = self.api.user_timeline(screen_name = screen_name,
        count = 200, max_id = oldest)
      tweets.extend(new_tweets)

      # Update id of oldest tweet
      oldest = tweets[-1].id

    # Update cache
    self.__add_tweets(screen_name, tweets)

    return tweets

  # Return CSV of screen_name (if exists)
  def get_csv(self, screen_name):
    fileName = './%s_tweets.csv' % screen_name
    if os.path.isfile(fileName):
      return fileName
    else:
      print 'No CSV on file. Run gen_usr_csv(\'%s\') to resolve this' % screen_name
      return None

  # Generate CSV of tweets from screen_name, return CSV name
  # Updates cache!
  def gen_usr_csv(self, screen_name):
    self.get_usr_feed(screen_name)

    # Hold tweets for adding to CSV
    tweets = self.mostRecentFeed['tweets']

    # Transform tweets into 2D array for CSV
    csvtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in tweets]

    # Write to CSV
    with open('%s_tweets.csv' % screen_name, 'wb') as f:
      writer = csv.writer(f)
      writer.writerow(['id', 'created_at', 'text'])
      writer.writerows(csvtweets)

    return '%s_tweets.csv' % screen_name


  # def test_tweet():
  #   # Generic tweet test
  #   api.update_status('tweet tweet am burb bot plz feed me quack')

  #   print 'Done'