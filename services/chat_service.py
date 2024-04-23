import openai
from abc import ABC, abstractmethod
from models.message_model import MessageRole


class PromptMessage:
    def __init__(self, role: MessageRole, content: str):
        self.role = role
        self.content = content
        pass


class BaseChatService(ABC):
    @abstractmethod
    def answer(self, messages: list[PromptMessage]):
        pass


class ChatService(BaseChatService):
    def __init__(self, sys_prompt, model, temperature):
        self.sys_prompt = PromptMessage(MessageRole.system, sys_prompt)
        self._model = model
        self._temperature = temperature

    def answer(self, messages: list[PromptMessage]):
        prompt = [{"role": el.role.value, "content": el.content} for el in messages]
        prompt.insert(
            0, {"role": self.sys_prompt.role.value, "content": self.sys_prompt.content}
        )

        completion = openai.ChatCompletion.create(
            model=self._model, messages=prompt, temperature=self._temperature
        )

        completion_answer = completion.choices[0].message.content

        return completion_answer


class MockedChatService(BaseChatService):
    def __init__(self, sys_prompt, model, temperature):
        self.sys_prompt = PromptMessage(MessageRole.system, sys_prompt)
        self._model = model
        self._temperature = temperature

    def answer(self, messages: list[PromptMessage]):
        [*prompt, last_message] = messages

        completion_answer = (
            f"Temporary system generated message: You said: {last_message.content}."
        )

        return completion_answer
