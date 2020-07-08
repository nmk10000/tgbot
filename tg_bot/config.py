from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 1181258174  # my telegram ID
    OWNER_USERNAME = "Naeemkk"  # my telegram username
    API_KEY = "1296488130:AAEkKKXG65eD2vINqCcW8EywugsW1nebB4I"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgres://yosnsoix:XRa9--gWDTL8Pc1NDiI7Vj3dw8N0Sszt@ruby.db.elephantsql.com:5432/yosnsoix'  # sample db credentials
    MESSAGE_DUMP = '-1234567890' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [752438017, 1181258174]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
