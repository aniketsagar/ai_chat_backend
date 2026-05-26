# this class holds the provider rigging 

#from pydantic import BaseModel
from .openai.openai import OpenAI

import logging 
logger = logging.getLogger(__name__)
class  ProviderService():
  def __init__(self, model:str):
    self.model = model

  def sendRequest(self, prompt:dict[str,str]):
    response = None
    logger.info(":::ProviderService:::",vars(self))
    if (self.model.lower() == "gpt"):
      response = OpenAI().processRequest(prompt)

    return response
