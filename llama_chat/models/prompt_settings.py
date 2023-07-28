from pydantic import BaseModel


class PromptSettings(BaseModel):
    context: str
    user_prefix: str
    user_suffix: str
    bot_prefix: str
    bot_suffix: str
    stop_words: list[str]
