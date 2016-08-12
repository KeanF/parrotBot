from twitter_scraper import TwitterScraper

if __name__ == '__main__':
  # Test scraping personal feed
  scraper = TwitterScraper()
  myFeed = scraper.get_home_feed()
  print scraper.get_cached_screen_name(), scraper.get_cached_tweets()

  # Test methods with 'example' feed
  feedName = ''

  parrotBotFeed = scraper.get_usr_feed(feedName)
  print scraper.get_cached_screen_name(), scraper.get_cached_tweets()
  
  # feedName = 'realDonaldTrump'
  # trumpFeed = scraper.get_user_tweets(feedName)
  
  # Check if CSV for feed exists
  csvName = scraper.get_csv(feedName)
  if csvName:
    print 'CSV: %s exists' % csvName
  else:
    scraper.gen_usr_csv(feedName)
    print('CSV for %s ' + 
      'now exists' if scraper.get_csv() else 'doesn\'t exist')