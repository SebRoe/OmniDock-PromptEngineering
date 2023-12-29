from .OpenAIAPIWrapper import OpenAIAPIWrapper
from .enums import OpenAIModelsChatCompletion

import logging 

logger = logging.getLogger("tasks_executor")
class OpenAIManager:

    def __init__(self, model, response_format):
        self.api_wrapper = OpenAIAPIWrapper() 

        if OpenAIModelsChatCompletion.has_model(model):
            self.execute_task = self.execute_task_chat_completion
            self.model = OpenAIModelsChatCompletion[model].value
        
        self._set_response_format(response_format)
                
    def _set_response_format(self, response_format):
        
        if self.model in [
            OpenAIModelsChatCompletion.GPT_4_1106_PREVIEW.value, 
            OpenAIModelsChatCompletion.GPT_3_5_TURBO_1106.value]:
            if response_format == "json":
                self.response_format = {"type": "json_object"}
                return 
            
        self.response_format = None 
            
    def execute_task_chat_completion(self, messages, **params):        
        return self.api_wrapper.send_chat_completion_request(messages, self.model, self.response_format, **params)

    def execute_task_completion(self, prompt, **params):
        return self.api_wrapper.send_completion_request(prompt, self.model, self.response_format, **params)