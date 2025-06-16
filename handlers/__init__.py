from aiogram import Router

from . import handlers, support, queries
from . import message_texts as MT

router = Router()
router.include_routers(handlers.router, support.router, queries.router)