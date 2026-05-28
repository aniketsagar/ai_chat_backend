# this class holds the provider rigging 

#from pydantic import BaseModel
from .openai.openaiProvider import OpenAIProvider

import logging 
logger = logging.getLogger(__name__)
class  ProviderService():
  def __init__(self, model:str):
    self.model = model
    if (self.model == "gpt"):
      self.provider = OpenAIProvider()
    else: 
        self.provider = None

  def generate(self, prompt:dict[str,str]):
    response = None
    logger.info(":::ProviderService:::",vars(self))
    
    if(self.provider):
      try:
        result = self.provider.generate(prompt)
        response = result.output_text
      except Exception as e:
        logger.info(f"::Exception::{e}")
        response = result
      
      logger.info(":::ProviderService:::")
      logger.info(response) 
    else:
      logger.info(":::ProviderService::: Error:: No provider found")
      logger.info(response) 
    return response
