# This class owns the conversation responsibility
# so load conversation, store converstaion 

from ...prompts.promptService import PromptService
from ...providers.providerService import ProviderService
from ...models.conversationService import ConversationServiceResponse
from ..storage.cache.cachingService import CachingService
from ..storage.file.conversationStorage import ConversationStorage
import logging



logger = logging.getLogger(__name__)
log_preamble = ":::ConversationService:::"
class ConversationService: 
  def __init__(self):
    self.model = "gpt"
    logger.info(":::ConversationService:::")
    logger.info(self.model)
    self.promptService = PromptService()
    self.providerService= ProviderService( self.model)
    self.conversation_cache = CachingService()
    self.conversation_repo = ConversationStorage()
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
        if(providerResponse.result):
          self.conversation_cache.write(conversation_id,providerResponse.result)
          print("::***************CACHE*************::::::::*************::::::::")
          print(self.conversation_cache.read(conversation_id))
          self.conversation_repo.write(conversation_id,self.conversation_cache.read(conversation_id))
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

      for chunk in self.providerService.stream(prompt):
        self.conversation_cache.write(conversation_id,chunk)
        # print ("!@#!@#@#!@#!#!@#!@#(((((((())))))))))))))))*******************")
        # print(self.conversation_cache.read(conversation_id))
        yield chunk
      print ("!@#!@#@#!@#!#!@#!@#(((((((())))))))))))))))*******************")
      print(self.conversation_cache.read(conversation_id))
      self.conversation_repo.write(conversation_id,self.conversation_cache.read(conversation_id))

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


