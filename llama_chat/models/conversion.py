from pydantic import BaseModel

from llama_chat.models.message import Message
from llama_chat.models.prompt_settings import PromptSettings
from llama_chat.utils.never import never


class Conversion(BaseModel):
    prompt_settings: PromptSettings
    messages: list[Message]

    def to_prompt(self) -> str:
        prompt = self.prompt_settings.context
        for message in self.messages:
            match message.role:
                case "user":
                    prompt += self.prompt_settings.user_prefix + message.text + self.prompt_settings.user_suffix
                case "bot":
                    prompt += self.prompt_settings.bot_prefix + message.text + self.prompt_settings.bot_suffix
                case _:
                    never(message.role)
        return prompt
