import os
from markov_generator import MarkovGenerator
from twitter_scraper import TwitterScraper

def markov_generator_test(txtFile='tests/janeere.txt'):
  gen = MarkovGenerator()
  gen.input(txtFile)
  gen.generateCorpus(gen.input(txtFile))
  print(gen.output())

def twitter_scraper_test():
  # Test scraping personal feed
  scraper = TwitterScraper()
  myFeed = scraper.get_home_feed()
  print scraper.get_cached_screen_name(), scraper.get_cached_tweets()

  # Test methods with 'example' feed
  feedName = 'Parrot_Bots'

  parrotBotFeed = scraper.get_usr_feed(feedName)
  print scraper.get_cached_screen_name(), scraper.get_cached_tweets()
  
  # Check if CSV for feed exists
  csvName = scraper.get_csv(feedName)
  if csvName:
    print 'CSV: %s exists' % csvName
  else:
    scraper.gen_usr_csv(feedName)
    print('CSV for %s ' + 
      'now exists' if scraper.get_csv(feedName) else 'doesn\'t exist')

def twitter_markov_test(feedName='Parrot_Bots'):
  # Initialize APIs
  gen = MarkovGenerator()
  scraper = TwitterScraper()

  # Scrape given feed and generate CSV
  scraper.get_usr_feed(feedName, 1)

  # Hold and format our scraped feeds
  tweets = scraper.get_cached_tweets()
  outTxt = '\n'.join(tweets)

  # Output to file to work with MarkovGenerator
  for i in range(1, len(tweets)):
    f = open('out%s.txt' % s, 'w')
    f.write(outTxt)
    f.close()
    
    # Train our MarkovGenerator
    gen.generateCorpus(gen.input('out%s.txt' % i))

  # Print some example text
  print(gen.output())

if __name__ == '__main__':
  # markov_generator_test()
  # twitter_scraper_test()
  twitter_markov_test()