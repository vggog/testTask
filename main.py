from src.handlers import *
from src.model import metadata
from src.repository import Repo


if __name__ == "__main__":
    repo = Repo()
    metadata.create_all(repo.engine)

    bot.run_forever()
