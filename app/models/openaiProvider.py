from pydantic import BaseModel
from typing import Optional, Any
class OpenAIProviderResult(BaseModel):
  success: bool
  result: Optional[str] = None 
  error : Optional[str] = None 
  error_type: Optional[str] = None 
  provider : str
  error_code:Optional[str] = None
  response_status:Optional[str] = None
  timestamp : float
  conversation_id: str