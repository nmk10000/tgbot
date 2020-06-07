from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 1181258174  # my telegram ID
    OWNER_USERNAME = "Naeemkk"  # my telegram username
    API_KEY = "1296488130:AAH_Qi3WpsvlHy8Q9A-CEqib1TLjSxIw0kI"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgres://nuypghmooiebtg:6c0656a9a38b30b5b9a65a1ba17aaa639ad85054d2ab6460777bf9ae561735a2@ec2-52-70-15-120.compute-1.amazonaws.com:5432/d60q8uja4blcp6'  # sample db credentials
    MESSAGE_DUMP = '-1234567890' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [752438017, 1181258174]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
