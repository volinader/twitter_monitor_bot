import tweepy
import config
from discord_sendmessage import send_emben_webhook, send_normal_webhook
from rules import add_rule, check_rules, logger

consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token 
access_token_secret = config.access_token_secret
bearer_token = config.bearer_token

#auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
#api = tweepy.API(auth)




class Listener(tweepy.StreamingClient):
    def on_connect(self):
        logger.info(" Bot Started")
    ''''add func streamresponse'''

    def on_response(self, response):
        users = [users.data for users in response.includes["users"]]
        user_name = users[0]['username']
        data = response.data.id
        url = f'https://twitter.com/{user_name}/status/{data}'
        print(url)
        print('account name', user_name)
        text = response.data.text
        print(text)
        
        send_emben_webhook(
            url = url,
            text = text,
            user_name = user_name
        )



def start():
    send_normal_webhook()
    stream = Listener(bearer_token)
    
    check_rules(stream)
    ask_about_add_rule = input("Do you want to add new rule? Y or N ")
    if ask_about_add_rule in ("YES, Y, yes, y"):
        add_rule(stream)
    
        

    stream.filter(
            expansions = "author_id"
    )
    

start()
