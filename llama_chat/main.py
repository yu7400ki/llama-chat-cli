import sys

from llama_cpp import Llama

from llama_chat.models.conversion import Conversion
from llama_chat.models.message import Message
from llama_chat.models.prompt_settings import PromptSettings


def main() -> None:
    args = sys.argv[1:]

    if len(args) != 1:
        print("Usage: python -m llama_chat <model_path>")
        sys.exit(1)

    model_path = args[0]
    llm = Llama(model_path=model_path)

    prompt_settings = PromptSettings(
        context="",
        user_prefix="User: ",
        user_suffix="\n",
        bot_prefix="Assistant: ",
        bot_suffix="\n",
        stop_words=["User:", "\nUser:"],
    )

    conversion = Conversion(
        prompt_settings=prompt_settings,
        messages=[
            Message(
                role="bot",
                text="Hello, I am the llama chatbot. I am here to help you with your problems.",
            ),
        ],
    )

    while True:
        user_text = input(conversion.prompt_settings.user_prefix)
        user_message = Message(
            role="user",
            text=user_text,
        )
        conversion.messages.append(user_message)
        prompt = conversion.to_prompt()
        prompt += conversion.prompt_settings.bot_prefix
        print(conversion.prompt_settings.bot_prefix, end="", flush=True)
        generator = llm(prompt, stop=conversion.prompt_settings.stop_words, echo=False, stream=True)
        response = ""
        for output in generator:
            print(output["choices"][0]["text"], end="", flush=True)
            response += output["choices"][0]["text"]
        print(conversion.prompt_settings.bot_suffix, end="", flush=True)
        bot_message = Message(
            role="bot",
            text=response,
        )
        conversion.messages.append(bot_message)


if __name__ == "__main__":
    main()
