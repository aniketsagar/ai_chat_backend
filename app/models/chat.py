from pydantic import BaseModel
from typing import Optional
class ChatRequest(BaseModel):
  conversation_id : str
  message : str


class ChatResponse(BaseModel):
  conversation_id : str
  status : str
  success :bool
  provider_name : str
  result : Optional[str] = None
  error : Optional[str] = None 
  error_code : Optional[str] = None
  error : Optional[str] = None
