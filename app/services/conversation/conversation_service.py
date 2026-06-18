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
  def __init__(self,debug:False):
    if(debug):
      self.model = "mock"
    else:
      self.model = "gpt"
    logger.info(":::ConversationService:::")
    logger.info(self.model)
    self.promptService = PromptService()
    self.providerService= ProviderService( self.model)
    self.conversation_cache = CachingService()
    self.conversation_repo = ConversationStorage()
  def generate(self,
                       message :str, conversation_id :str)-> ConversationServiceResponse:
    
    prompt = self.promptService.build_prompt(message,conversation_id)
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
          print("$$$$$$$$$$$$PROVIDER RESP $$$$$$$$$$$$$$$$$$$")
          print(providerResponse)
          chunk = {
            "data":providerResponse.result,
            "conversation_id":providerResponse.conversation_id,
            "timestamp":providerResponse.timestamp,
            "response_status":providerResponse.response_status
          }
          self.conversation_cache.write(conversation_id,chunk)
          print("::***************CACHE*************::::::::*************::::::::")
          print(self.conversation_cache.read(conversation_id))
          self.conversation_repo.write(conversation_id,self.conversation_cache.read(conversation_id))
          self.conversation_cache.delete(conversation_id)
          print("::***************CACHE*************::::::::*************::::::::")
          print(self.conversation_cache.read(conversation_id))
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
      logger.info(f"::ConversationService***::Exception::{e}")
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
    
    prompt = self.promptService.build_prompt(message,conversation_id)
    logger.info(log_preamble + self.model)
    logger.info(prompt)
    conversation_id = conversation_id
    try:

      for chunk in self.providerService.stream(prompt):
        print("*****WRITING TO CACHE************")
        print(chunk)
        self.conversation_cache.write(conversation_id,chunk)
        # print ("!@#!@#@#!@#!#!@#!@#(((((((())))))))))))))))*******************")
        # print(self.conversation_cache.read(conversation_id))
        # print("************&&&&&&&&&&&&&&&&CHUNK&&&&&&&&&&&&&&****************")
        # print(chunk)
        if(chunk["data"]):
          yield chunk["data"]
      print ("!@#!@#@#!@#!#!@#!@#(((((((())))))))))))))))*******************")
      print(self.conversation_cache.read(conversation_id))
      self.conversation_repo.write(conversation_id,self.conversation_cache.read(conversation_id))
      self.conversation_cache.delete(conversation_id)
      # print("::***************CACHE*************::::::::*************::::::::")
      # print(self.conversation_cache.read(conversation_id))
    except Exception as e:
      logger.info(f"::ConversationService*****&&&&&&::Exception::{e}")
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


