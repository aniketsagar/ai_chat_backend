import json
from pathlib import Path

# `cwd`: current directory is straightforward
cwd = Path.cwd()

# `mod_path`: According to the accepted answer and combine with future power
# if we are in the `helper_script.py`
mod_path = Path(__file__).parent
class ConversationStorage():
  def __init__(self):
    relative_path = "../../../repositories/conversations.json"
    self.filePath = (mod_path / relative_path).resolve()
    
  
  def read(self):
    data = None 
    with open(self.filePath, mode="r", encoding="utf-8") as read_file:
      data = json.load(read_file)
    return data 
  def write(self,conversation_id,data):
    conversation_data = self.read()
    if(conversation_data):
      try:
        conversation_data[conversation_id] = data
      except: 
        conversation_data[conversation_id] = data
    else:
      conversation_data = {}
      conversation_data[conversation_id] = data

    with open(self.filePath, mode="w",encoding="utf-8") as write_file:
      json.dump(conversation_data, write_file)
