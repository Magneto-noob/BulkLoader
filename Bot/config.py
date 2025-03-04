from distutils.util import strtobool
import os
from dotenv import load_dotenv
from pyrogram.types import BotCommand


# Load environment variables from .env file
load_dotenv()


class Config(object):

    # Your API HASH
    API_HASH = '33a37e968712427c2e7971cb03f341b3'

    # Your API ID
    APP_ID = '15523035'

    # Your Bot Token
    BOT_TOKEN = '2049170894:AAExN_SOtMIEf2SD7tUmpvelNAokokQSwG8'

    # Your Telegram ID (optional)
    OWNER_ID = '910674886'

    # Upload method (default to False)
    AS_ZIP = bool(strtobool(os.environ.get('AS_ZIP', 'False')))

    # Channel/Group ID where you dump all the downloaded files.
    DUMP_ID = int(os.environ.get('DUMP_ID')
                  ) if os.environ.get('DUMP_ID') else None

    PLUGINS = {'root': 'Bot.plugins'}

    DOWNLOAD_DIR = "./downloads/"

    BOT_COMMANDS = [
        BotCommand('start', 'start bot'),
        BotCommand('help', 'help messages'),
        BotCommand('thumbnail', 'custom thumbnail'),
        BotCommand('caption', 'custom caption')
    ]
