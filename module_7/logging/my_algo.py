import datetime
import logging
import utils


logger = logging.getLogger(__name__)


def run_algo():
    logger.info("Hola a las")
    logger.error("Hola a las")


def main():
    utils.config_logging()
    run_algo()         


if __name__ == "__main__":
    main()
                 
