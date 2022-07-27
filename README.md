## It's real time twitter monitoring bot with discrod webhook 

🔗 https://www.python.org/downloads/

⚠️ It is important to check the option to add python to PATH

You need to take a registration in twitter developer account

[https://developer.twitter.com/](https://developer.twitter.com/)

Then do all steps from this video [https://youtu.be/0EekpQBEP_8?t=229](https://youtu.be/0EekpQBEP_8?t=229) to setup twitter API and get bearer_token

Edit config.py file and put your bearer_token

How to get webhook url - https://www.youtube.com/watch?v=K8vgRWZnSZw
***

## Commands

Install the dependencies by running the command below into the project folder:

`pip install -r requirements.txt`


Ready! Now just start the bot with the command, inside the project folder

`python main.py`

## When started bot asked you:

### Do you want to delete rules from monitoring? Y or N

Description: In first running you need write "yes". If you have account which you monitored before and you want to delete it, then you need to write "yes" 
### Do you want to add new rule? Y or N

Description: In first running you need write "yes". If you want to add new user for monitoring, write "yes" then bot ask you again (maybe you want to monitoring several users)
