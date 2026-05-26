# This class owns the conversation responsibility
# so load conversation, store converstaion 

from ...prompts.promptService import PromptService
from ...providers.providerService import ProviderService
from typing import Any
import logging


logger = logging.getLogger(__name__)
class ConversationService: 
  def __init__(self):
    self.model = "gpt"
    logger.info(":::::#################:::::::::::::::::::::")
    logger.info(self.model)
  def generate_response(self,
                       message :str)-> str:
    
    prompt = PromptService().generatePrompt(message)
    print("***********",self.model)
    print("******",prompt)
    provider= ProviderService("gpt")
    print(">>>>>>>>>>>>>>>>>>>>>>>",vars(provider))
    providerResponse = provider.sendRequest(prompt)
    
    response :Any = {
      "status": "successful",
      "response": providerResponse
    }
    print("*****************",response)
    return response




