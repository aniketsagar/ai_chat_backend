import logging
from pydantic import BaseModel
from typing import Any
class BackendLogger(BaseModel):
  def __init__(self,name:str):
    # Configure basic logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    self.logger = logging.getLogger(name)
