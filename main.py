import asyncio
from telegram.ext import Application
from config import TOKEN
from database import create_tables
from handlers import get_handlers

async def main():
    create_tables()
    app = Application.builder().token(TOKEN).build()
    app.add_handler(get_handlers())
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
