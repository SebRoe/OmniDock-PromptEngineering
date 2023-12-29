import enum 


class OpenAIModelsChatCompletion(enum.Enum):
    GPT_4_1106_PREVIEW = "gpt-4-1106-preview"
    GPT_3_5_TURBO_1106 = "gpt-3.5-turbo-1106"
    
    
    @classmethod
    def has_model(cls, model):
        return any(model == item.name for item in cls)
    
    @classmethod 
    def get_value(cls, model):
        return cls[model].value