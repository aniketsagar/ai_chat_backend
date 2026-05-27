# this class holds the provider rigging 

#from pydantic import BaseModel
from .openai.openaiProvider import OpenAIProvider

import logging 
logger = logging.getLogger(__name__)
class  ProviderService():
  def __init__(self, model:str):
    self.model = model

  def generate(self, prompt:dict[str,str]):
    response = None
    logger.info(":::ProviderService:::",vars(self))
    if (self.model.lower() == "gpt"):
      try:
        result = OpenAIProvider().processRequest(prompt)
        response = result.output_text
      except Exception as e:
        logger.info(f"::Exception::{e}")
        response = result
      
      logger.info(":::ProviderService:::")
      logger.info(response) 
    return response
