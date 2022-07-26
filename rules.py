import tweepy
import logging


logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",
                    datefmt="%H:%M:%S")
logger = logging.getLogger()

def check_rules(stream):

    """checking on existing rules and deleting it if required"""

    #getting access to twitter api.v2
    old_rules = stream.get_rules()
    logger.debug(f"Old rules: {old_rules}")

    #checking for exicting rules
    rules_to_del = []

    if old_rules.data and len(old_rules.data) > 0:
        for old_rule in old_rules.data:
            logger.debug(f"Add old rule {old_rules} for deletion")
            print("You monitoring:", old_rule.value)
            rules_to_del.append(old_rule.id)
    
    
    
    if len(rules_to_del) > 0:
  
        your_choice = input("Do you want to delete rules from monitoring? Y or N ")
        if your_choice in ("Yes, yes, Y, y"):
            logger.debug(f"Deleteing rules: {rules_to_del}")
            stream.delete_rules(rules_to_del)
            

            
       
        elif your_choice in ("No, N, no, n"):
            logger.debug("Choose NO in rules delete choice")
            print("Ok, next step")
            
        
    else:
        logger.debug("No rules for delete")
    return old_rules

def add_rule(stream) -> None:
    """"Add rule to stream"""


    rule_input = input("Put user ID here example - BarackObama ")
    rule_to_add = tweepy.StreamRule(f"from:{rule_input}")

    rule_response = stream.add_rules(add=rule_to_add)
    logger.debug(f"Add new rule{rule_response}")
    user = stream.get_rules()
    for one_user in user.data:
        print('you monitoring', one_user.value)
    one_more_rule = input('Maybe do u want to add one more rule? Y or N ')
    if one_more_rule in ("Yes, yes, Y, y"):
        add_rule(stream)
