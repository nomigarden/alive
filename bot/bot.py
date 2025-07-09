import discord
import json
from datetime import timezone, datetime, timedelta
import asyncio
import json

with open("config.json", "r") as f:
    config = json.load(f)

BOT_TOKEN = config["bot_token"]
MY_USER_ID = config["my_user_id"]
ALERT_USER_ID = config["alert_user_id"]
CHECKIN_PATH = config["checkin_path"]
username = config["username"]

intents = discord.Intents.default()
client = discord.Client(intents=intents)


async def check_loop():
    await client.wait_until_ready()
    channel = None

    while not client.is_closed():
        try:
            with open(CHECKIN_PATH, "r") as f:
                data = json.load(f)

            last_check_str = data.get("last_checkin")
            if not last_check_str:
                print("no check-in yet.")
                await asyncio.sleep(3600)
                continue

            last_check = datetime.fromisoformat(last_check_str)
            now = datetime.now(timezone.utc)
            diff = now - last_check

            print(f"Time since last check-in: {diff}")

            if diff > timedelta(hours=48):
                user = await client.fetch_user(ALERT_USER_ID)
                await user.send(f"Alert: no response from {username} in over 48 hours. This is an automatic message from the 'dead man's switch' system created by Nomi.")
                
            elif diff > timedelta(hours=36):
                user = await client.fetch_user(MY_USER_ID)
                await user.send("Reminder: it has been over 36 hours since your last check-in.")
            else:
                print("All clear.")

        except Exception as e:
            print(f"Error during check-in validation: {e}")

        await asyncio.sleep(3600)  # wait 1h

@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")
    client.loop.create_task(check_loop())

client.run(BOT_TOKEN)