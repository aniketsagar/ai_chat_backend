# service to create a prompt


class PromptService():
  def generatePrompt(self,message:str):
    role = " you are a life assistent with expertise" \
    "in everything"
    prompt = role + " " +"query" + " "  + message
    result = {"prompt": prompt}
    return result
  