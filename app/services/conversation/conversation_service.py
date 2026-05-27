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
    logger.info(":::ConversationService:::")
    logger.info(self.model)
    self.promptService = PromptService()
    self.providerService= ProviderService( self.model)
  def generate(self,
                       message :str)-> dict[str,Any]:
    
    prompt = self.promptService.build_prompt(message)
    logger.info(log_preamble + self.model)
    logger.info(prompt)

    try:
      providerResponse = self.providerService.generate(prompt)
    except Exception as e:
      logger.info(f"::ProviderService::Exception::{e}")
      providerResponse ={"error":e}
    # providerResponse ={'status': 'successful', 
    #                    'response': 'In the golden savannah, the lion roared fiercely, reclaiming his throne from shadows of doubt.'}

    response : dict[str,Any] = {
      "status": "successful",
      "response": providerResponse
    }
    logger.info(":::ConversationService:::")
    logger.info(response)
    return response



