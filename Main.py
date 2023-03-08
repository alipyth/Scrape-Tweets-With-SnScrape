
#pip install Snscrape

import snscrape.modules.twitter as sntwitter
# یوزر نیم توییتر مد نظر و تعداد توییتی که میخواهید استخراج کنید
username = "elonmusk"
num_tweets = 1000

# ایجاد یک لیست برای نگهداری از توییت ها
tweets = []

# حلقه برای پیدا کردن توییت ها و درج آن در لیست بالا
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f"from:{username}").get_items()):
    if i >= num_tweets:
        break
    tweets.append(tweet)

# چاپ توییت های استخراج شده 
for tweet in tweets:
    print(tweet.content)
    
