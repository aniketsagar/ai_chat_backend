# service to create a prompt

import logging 
logger = logging.getLogger(__name__)
class PromptService():
  def build_prompt(self,message:str):
    logger.info(":::PromptService:::")
    role = " you are a life assistent with expertise" \
    "in everything"
    prompt = role + " " +"query" + " "  + message
    result = {"prompt": prompt}
    logger.info(result)
    return result
  