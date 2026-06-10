# this class holds the provider rigging 

#from pydantic import BaseModel
from .openai.openaiProvider import OpenAIProvider
from ..models.providerService import ProviderServiceResponse
import logging 
from datetime import datetime
from contextlib import  contextmanager
logger = logging.getLogger(__name__)
class  ProviderService():

  def __init__(self, model:str):
    self.model = model
    if (self.model == "gpt"):
      self.provider = OpenAIProvider()
      self.provider_name = "openai"
    else: 
        self.provider = None

  def generate(self, prompt:dict[str,str])->ProviderServiceResponse:
    response = None
    logger.info(":::ProviderService:::",vars(self))
    conversation_id = prompt["conversation_id"]
    if(self.provider):
      try:
        providerResult = self.provider.generate(prompt)
        if(providerResult.success):
            
          response = ProviderServiceResponse(
            success = True,
            result = providerResult.result,
            provider_name = providerResult.provider,
            conversation_id=providerResult.conversation_id,
            timestamp=providerResult.timestamp,
            response_status=providerResult.response_status
          )
        else:
          response = ProviderServiceResponse(
            success = False,
            error_code = providerResult.error_code,
            error = providerResult.error_type,
            provider_name = self.provider_name,
            conversation_id=providerResult.conversation_id,
            timestamp=providerResult.timestamp,
            response_status=providerResult.response_status
          )

      except Exception as e:
        logger.info(f"::Exception::{e}")
        response = ProviderServiceResponse(
          success = False,
          error_code = "internal_server_error",
          error = f"::Exception::{e}",
          provider_name = self.provider_name,
          conversation_id=conversation_id,
          timestamp=datetime.now().timestamp(),
          response_status="failed"
        )
      
      logger.info(":::ProviderService:::")
      logger.info(response) 
    else:
      logger.info(":::ProviderService::: Error:: No provider found")
      logger.info(response) 
      response =   ProviderServiceResponse(
        success = False,
        error_code = "internal_server_error",
        error = f"::Exception::No Provider found",
        provider_name = self.provider_name ,
        conversation_id=conversation_id,
        timestamp=datetime.now().timestamp(),
        response_status="failed"
      )
    return response

  
  def stream(self, prompt:dict[str,str]):
    response = None
    logger.info(":::ProviderService:::",vars(self))
    conversation_id = prompt["conversation_id"]
    if(self.provider):
      try:
        for chunk in self.provider.stream(prompt):
          yield chunk
      except Exception as e:
        logger.info(f":: THIS Exception::{e}")
        response = ProviderServiceResponse(
          success = False,
          error_code = "internal_server_error",
          error = f"::Exception::{e}",
          provider_name = self.provider_name,
          conversation_id=conversation_id,
          timestamp=datetime.now().timestamp(),
          response_status="failed"
        )
      
      logger.info(":::ProviderService:::")
      logger.info(response) 
    else:
      logger.info(":::ProviderService::: Error:: No provider found")
      logger.info(response) 
      response =   ProviderServiceResponse(
        success = False,
        error_code = "internal_server_error",
        error = f"::Exception::No Provider found",
        provider_name = self.provider_name,
        conversation_id=conversation_id,
        timestamp=datetime.now().timestamp(),
        response_status="failed"
      )
    if(response):

      yield response
