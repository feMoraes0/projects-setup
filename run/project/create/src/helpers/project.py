import os

class Project:
  def __init__(self, name, framework, message):
    self.name = self.__validate_name(name)
    self.framework = framework
    self.user_message =  message

  def __validate_name(self, name):
    restrictions = [" ", "-", "_"]
    
    if any(x in name for x in restrictions):
      name = self.__fix_name(name, x) # is not valid
    
    return name # is valid

  def __fix_name(self, name, separator):
    name_list = name.split(separator)
    correct_name = ""
    
    for name_item in name_list:
      correct_name += name_item.capitalize()
    
    return correct_name

  def create(self):
    try:
      if(self.framework == "ReactJS"):
        os.system(f"npx create-react-app {self.name}")
      elif(self.framework == "React Native"):
        os.system(f"npx react-native init {self.name}")
      elif (self.framework == "NodeJS"):
        os.system(f"mkdir {self.name} && cd {self.name} && npm init -y")
      self.message.success(f"Project {self.name} created with success!")
    except:
      self.message.error(f"Fail to create the project {self.name}")