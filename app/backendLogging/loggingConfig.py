import logging 
logging.basicConfig(
        level=logging.INFO,
        force=True,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

print("LOGGING CONFIG LOADED")