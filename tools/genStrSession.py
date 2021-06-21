from os import environ, path
from asyncio import get_event_loop
from pyrogram import Client
from dotenv import load_dotenv


if path.isfile("config.env"):
    load_dotenv("config.env")


async def genStrSession() -> None:
    async with Client(
        "Alpha",
        api_id=int(environ.get("API_ID") or input("Enter Telegram APP ID: ")),
        api_hash=environ.get("API_HASH") or input("Enter Telegram API HASH: "),
    ) as app:
        print("\nprocessing...")
        await app.send_message(
            "me", f"#Alpha #HU_STRING_SESSION\n\n```{await app.export_session_string()}```"
        )
        print("Done !, session string has been sent to saved messages!")


if __name__ == "__main__":
