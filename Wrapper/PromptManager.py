from abc import ABC, abstractmethod
import json 
import datetime 

class PromptManager:

    @abstractmethod
    def create_completion_prompt(self, *args, **kwargs) -> str:
        pass 
    
    @abstractmethod
    def create_chat_completion_prompt(self, *args, **kwargs):
        pass 
    
    def save_to_file(self, response, file_path):
        """ Save the response to a file. Use timestamp as the file name. File should be a json file using indent = 4"""
        file_path = file_path + str(datetime.datetime.now().timestamp()) + ".json"
        with open(file_path, "w") as f:
            json.dump(response, f, indent=4)
    
    def serialize_chat_completion_response(self, response):
        
        # Test Format 1 
        try:
            response_dict = json.loads(response)
            return response_dict
        except Exception as e:
            pass 
        
        # Test Format 2
        if isinstance(response, dict):
            return response
                
        # Test Format 3
        try:
            json_string = response.replace("```json", "").replace("```", "").strip()
            response_dict = json.loads(json_string)
            return response_dict
        except json.JSONDecodeError as e:
            return {"error": str(e), "status": "failure"}


        
        