from discord_webhook import DiscordWebhook, DiscordEmbed
import config


url_discord = config.url

def send_emben_webhook(url, text: str,user_name: str):

    webhook = DiscordWebhook(url_discord)

    embed = DiscordEmbed(title=f'Tweet author {user_name}', description=f'{url}', color='03b2f8')
    embed.add_embed_field(name="tweet text", value=f"{text}", inline=False)
    embed.set_timestamp()
# add embed object to webhook
    webhook.add_embed(embed)

    response = webhook.execute()

def send_normal_webhook():
    webhook = DiscordWebhook(url_discord, content="monitoring started")

    response = webhook.execute()