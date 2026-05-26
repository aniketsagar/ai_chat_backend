

from fastapi import FastAPI
from .api.routes import chat
from .backendLogging.loggingConfig import *
#import logging

logger = logging.getLogger(__name__)



logger.info("::::::::::::::APPLICATION STARTING")
print("PRINT TEST")


app = FastAPI()

app.include_router(chat.router)

logger.info(":::::::::::::::server started ....")
@app.get("/")
async def home():
  return {"status":"ok"}

