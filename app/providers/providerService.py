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
      result = OpenAIProvider().processRequest(prompt)
      response = result.output_text
      logger.info(":::ProviderService:::",response) 
    return response
