import asyncio
import locale
import logging
import sys

from bot.client import bot, dp
from bot.handlers import routers

locale.setlocale(locale.LC_TIME, "ru_RU.UTF-8")


async def main() -> None:
    for router in routers:
        dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
