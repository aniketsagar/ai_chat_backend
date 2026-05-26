# service to create a prompt

import logging 
logger = logging.getLogger(__name__)
class PromptService():
  def build_prompt(self,message:str):
    instruction = "you are a life assistant."
    logger.info(":::PromptService:::")
    
    prompt ={
      "instruction": instruction,
      "input": message
    }

    return prompt



