# this class holds the provider rigging 

#from pydantic import BaseModel
from .openai.openaiProvider import OpenAIProvider
from ..models.providerService import ProviderServiceResponse
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
        providerResult = self.provider.generate(prompt)
        response = ProviderServiceResponse(
          success = True,
          result = providerResult.result,
          provider_name = providerResult.provider 
        )

      except Exception as e:
        logger.info(f"::Exception::{e}")
        response = ProviderServiceResponse(
          success = False,
          error_code = "internal_server_error",
          error = f"::Exception::{e}"
        )
      
      logger.info(":::ProviderService:::")
      logger.info(response) 
    else:
      logger.info(":::ProviderService::: Error:: No provider found")
      logger.info(response) 
      response =   ProviderServiceResponse(
        success = False,
        error_code = "internal_server_error",
        error = f"::Exception::No Provider found"
      )
    return response
