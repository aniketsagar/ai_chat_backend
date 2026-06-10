# service to create a prompt

import logging 
logger = logging.getLogger(__name__)
class PromptService():
  def build_prompt(self,message:str,conversation_id:str):
    instruction = "you are a life assistant."
    logger.info(":::PromptService:::")
    
    prompt ={
      "instruction": instruction,
      "input": message,
      "conversation_id":conversation_id
    }

    return prompt



