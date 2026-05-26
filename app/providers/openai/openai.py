# this class contains the rigging of openai
from pydantic import BaseModel
from typing import Any

class OpenAI(BaseModel):
  def processRequest(self,prompt:dict[str,str]):
    request = {
      "key":"12345asdadas",
      "prompt": prompt["prompt"]
    }

    response : Any =  {
      "message":"successful",
      "request": request  }
    return response