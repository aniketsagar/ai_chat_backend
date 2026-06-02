# This class owns the conversation responsibility
# so load conversation, store converstaion 

from ...prompts.promptService import PromptService
from ...providers.providerService import ProviderService
from ...models.conversationService import ConversationServiceResponse

import logging
from contextlib import contextmanager

logger = logging.getLogger(__name__)
log_preamble = ":::ConversationService:::"
class ConversationService: 
  def __init__(self):
    self.model = "gpt"
    logger.info(":::ConversationService:::")
    logger.info(self.model)
    self.promptService = PromptService()
    self.providerService= ProviderService( self.model)
  def generate(self,
                       message :str, conversation_id :str)-> ConversationServiceResponse:
    
    prompt = self.promptService.build_prompt(message)
    logger.info(log_preamble + self.model)
    logger.info(prompt)
    conversation_id = conversation_id
    try:

      providerResponse = self.providerService.generate(prompt)
      if(providerResponse.success):
        response = ConversationServiceResponse(
          conversation_id = conversation_id,
          status = "successful",
          success=True,
          result= providerResponse.result,
          provider_name=providerResponse.provider_name
        )
      else:
        response = ConversationServiceResponse(
          conversation_id = conversation_id,
          status = "Failed",
          success=False,
          error=providerResponse.error,
          error_code=providerResponse.error_code,
          provider_name=providerResponse.provider_name
        )
    except Exception as e:
      logger.info(f"::ProviderService::Exception::{e}")
      providerResponse ={"error":e}
      response = ConversationServiceResponse(
        conversation_id = conversation_id,
        status = "Failed",
        success=False,
        error="Internal Server Error",
        error_code="500",
        provider_name="openai"
      )
    # providerResponse ={'status': 'successful', 
    #                    'response': 'In the golden savannah, the lion roared fiercely, reclaiming his throne from shadows of doubt.'}

    logger.info(":::ConversationService:::")
    logger.info(response)
    return response
  

  
  def stream(self, message :str, conversation_id :str):
    
    prompt = self.promptService.build_prompt(message)
    logger.info(log_preamble + self.model)
    logger.info(prompt)
    conversation_id = conversation_id
    try:

     with self.providerService.stream(prompt) as stream:
       for chunk in stream:
         print ("!@#!@#@#!@#!#!@#!@#(((((((())))))))))))))))*******************")
         print(chunk)
         yield chunk

    except Exception as e:
      logger.info(f"::ProviderService::Exception::{e}")
      response = ConversationServiceResponse(
        conversation_id = conversation_id,
        status = "Failed",
        success=False,
        error="Internal Server Error",
        error_code="500",
        provider_name="openai"
      )
    # providerResponse ={'status': 'successful', 
    #                    'response': 'In the golden savannah, the lion roared fiercely, reclaiming his throne from shadows of doubt.'}
   
      logger.info(":::ConversationService:::")
      logger.info(response)
      yield response


