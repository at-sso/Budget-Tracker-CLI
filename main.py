from src import main, logger

if __name__ == "__main__":
    try:
        logger.returned(main)
    except Exception:
        logger.exc(c=main, default=True)
        raise
