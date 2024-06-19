import asyncio
import logging


from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.base import BaseStorage
from aiogram.fsm.storage.redis import RedisStorage

from src.battle.main.config import get_settings
from src.battle.main.config import Settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_bot(settings: Settings) -> Bot:
    """
    Create the bot.
    """

    # Create the bot
    bot = Bot(
        token=settings.bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    return bot


def create_storage(settings: Settings) -> BaseStorage:
    """
    Create the storage.
    """

    # Create the storage
    storage = RedisStorage.from_url(settings.redis.dsn)

    return storage


def create_dispatcher(storage: BaseStorage | None = None) -> Dispatcher:
    """
    Create the dispatcher.
    """

    if storage and not isinstance(storage, BaseStorage):
        raise TypeError(
            f"FSM storage should be instance of 'BaseStorage' not {type(storage).__name__}"
        )

    # Create the dispatcher
    dispatcher = Dispatcher(storage=storage)

    return dispatcher


async def main():
    """
    The main function.
    """
    # Get the settings
    settings = get_settings()

    # Create the bot
    bot = create_bot(settings)

    # Create the storage
    storage = create_storage(settings)

    # Create the dispatcher
    dispatcher = create_dispatcher(storage)

    # Run the bot
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
