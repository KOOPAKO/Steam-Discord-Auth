# steamdiscordauth

Script to get mobile auth codes via Discord, rather than Steam mobile app.

Originally made to allow myself and some friends to easily share a steam account.

## Requirements
- Ensure you have python 3.6
- python -m pip install -U steam[client]
- python -m pip install -U steam
- python -m pip install -U discord.py

## Setup
1. Ensure all requirements are met
2. Add [Discord bot token](https://discord.com/developers/applications) to token.json
3. Generate token.json file with [these steps](https://pastebin.com/rFHRrT88). More info on this [here](https://steam.readthedocs.io/en/stable/api/steam.guard.html).
4. Run discordbot.py
