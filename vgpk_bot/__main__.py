import asyncio
import logging
import sys

from vgpk_bot.client import bot, dp
from vgpk_bot.handlers import routers


async def main() -> None:
    for router in routers:
        dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
