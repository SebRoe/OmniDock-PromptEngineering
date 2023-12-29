import requests
import openai
import json 
import logging 

import dotenv 
import os

dotenv.load_dotenv()

logger = logging.getLogger("tasks_executor")

class OpenAIAPIWrapper:
    
    def __init__(self):
        
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)
        if not OPENAI_API_KEY:
            raise Exception("OPENAI_API_KEY not found in environment variables.")

        self.api_key = OPENAI_API_KEY
        self.client = openai.OpenAI(api_key=self.api_key)
        
    def send_completion_request(self, prompt, model, response_format, **params):
        try:
            response = self.client.Completion.create(
                model=model,
                response_format=response_format,
                prompt=prompt,
                **params
            )
            return response.choices[0].message.content

        except openai.APIError as e:
            logger.error(f"OpenAI API Error: {str(e)}")
            return {"error": str(e), "status": "failure", "type": 1}

        except requests.exceptions.RequestException as e:
            logger.error(f"OpenAI API Error: {str(e)}")
            return {"error": str(e), "status": "failure", "type": 2}

        except Exception as e:
            logger.error(f"OpenAI API Error: {str(e)}")
            return {"error": str(e), "status": "failure", "type": 3}
        
        
        
    def send_chat_completion_request(self, messages, model, response_format, **params):
        try:
            response = self.client.chat.completions.create(
                model=model,
                response_format=response_format,
                messages=messages,
                **params
            )
            return response.choices[0].message.content

        except openai.APIError as e:
            return {"error": str(e), "status": "failure", "type": 1}

        except requests.exceptions.RequestException as e:
            return {"error": str(e), "status": "failure", "type": 2}

        except Exception as e:
            return {"error": str(e), "status": "failure", "type": 3}
        
