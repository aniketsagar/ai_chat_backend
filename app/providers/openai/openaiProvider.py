# this class contains the rigging of openai
from openai import OpenAI
import logging
logger = logging.getLogger(__name__)
class OpenAIProvider():
  def __init__(self):
    self.client = OpenAI(
    )
  def processRequest(self,prompt):
    logger.info(prompt)
    response = self.client.responses.create(
      model = "gpt-4.1-nano",# this is cheapest
      input =  prompt["input"],
      instructions = prompt["instruction"]
    )
   
    return response