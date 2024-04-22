import openai

from models.message_model import MessageRole


class PromptMessage:
    def __init__(self, role: MessageRole, content: str):
        self.role = role
        self.content = content
        pass


class ChatService:
    def __init__(self, sys_prompt, model, temperature):
        self.sys_prompt = PromptMessage(MessageRole.system, sys_prompt)
        self._model = model
        self._temperature = temperature

    def answer(self, messages: list[PromptMessage]):
        prompt = [vars(el) for el in messages]
        prompt.insert(0, vars(self.sys_prompt))

        # completion = openai.ChatCompletion.create(
        #     model=self.__model, messages=prompt, temperature=self._temperature
        # )

        # completion_answer = completion.choices[0].message.content
        completion_answer = "Temporary system generated message."

        return completion_answer
