# This class owns the conversation responsibility
# so load conversation, store converstaion 

from ...prompts.promptService import PromptService
from ...providers.providerService import ProviderService
from typing import Any
import logging


logger = logging.getLogger(__name__)
log_preamble = ":::ConversationService:::"
class ConversationService: 
  def __init__(self):
    self.model = "gpt"
    logger.info(":::::#################:::::::::::::::::::::")
    logger.info(self.model)
  def generate_response(self,
                       message :str)-> dict[str,Any]:
    
    prompt = PromptService().generatePrompt(message)
    logger.info(log_preamble + self.model)
    logger.info(prompt)
    provider= ProviderService("gpt")
    providerResponse = provider.sendRequest(prompt)
    
    response : dict[str,Any] = {
      "status": "successful",
      "response": providerResponse
    }
    logger.info(":::ConversationService:::")
    logger.info(response)
    return response




