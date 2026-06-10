from typing import Optional
from pydantic import BaseModel

class ProviderServiceResponse(BaseModel):
  success : bool
  provider_name : str
  result : Optional[str] = None
  error_code : Optional[str] = None
  error : Optional[str] = None
  timestamp : float
  conversation_id: str
  response_status: Optional[str] = None