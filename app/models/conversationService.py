from pydantic import BaseModel
from typing import Optional

class ConversationServiceResponse(BaseModel):
  conversation_id : str
  status : str
  success :bool
  provider_name : str
  result : Optional[str] = None
  error : Optional[str] = None 
  error_code : Optional[str] = None
  error : Optional[str] = None
