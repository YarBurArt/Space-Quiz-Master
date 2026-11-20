# Space Quiz Master
![sdf](https://images.unsplash.com/photo-1610296669228-602fa827fc1f?q=80&w=1975&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)

## Welcome to the SpaceBot README!
Dive into the cosmos with SpaceBot, powered by cutting-edge tech (MongoDB, aiogram 3, asyncio, aiohttp).

### Setup

Requires Python 3.15 and [uv](https://docs.astral.sh/uv/). Set `TOKEN` in a `.env` file to use your own bot.

```sh
uv sync
uv run python bot.py
```

### Available Commands:

`/help`: This command will display a list of all available commands, just like you're seeing right now!

`/start`: Use this command to receive a welcome message and get started with SpaceBot.

`/next`: Feeling curious about the cosmos? This command will provide you with a random, fascinating fact about space.

`/cancel`: Did you start a quiz or just want to exit SpaceBot? This command will stop any ongoing interactions and let you start fresh.

`/rndimg`: Get stunning visuals of the universe with this command! It will fetch a random image from NASA's API and share it with you.
