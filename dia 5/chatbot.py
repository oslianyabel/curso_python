import json
import os

from dotenv import load_dotenv
from openai import OpenAI  # Documentacion: https://platform.openai.com/docs/overview

load_dotenv()

AVANGENIO_API_KEY = os.getenv(
    "AVANGENIO_API_KEY"
)  # recuerda porner esta variable dentro de .env


class Completions:
    def __init__(
        self,
        api_key,
        name="curso_python_bot",
        model="agent-md",  # ver en plataformia más modelos
        json_tools=[],
        functions={},
        tool_choice="auto",
    ):
        self.client = OpenAI(
            api_key=api_key, base_url="https://apigateway.avangenio.net"
        )
        self.name = name
        self.model = model
        self.json_tools = json_tools
        self.functions = functions
        self.tool_choice = tool_choice
        self.error_response = """Ha ocurrido un error ejecutando la herramienta {tool_name} con los argumentos {tool_args}"""

    def send_msg(self, messages):
        print(f"Running {self.name} with {len(self.functions)} tools")
        while True:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=self.json_tools,
                tool_choice=self.tool_choice,
            )
            if response.choices[0].message.tool_calls:
                self._run_tools(
                    messages, response
                )  # agrega a messages las respuestas de las herramientas
                continue

            break

        ans = response.choices[0].message.content.strip()
        print(f"{self.name}: {ans}")
        return ans

    def _run_tools(self, messages, response) -> None:
        tools = response.choices[0].message.tool_calls
        print(f"{len(tools)} tools need to be called!")
        messages.append(response.choices[0].message)  # Sin esto falla

        for tool in tools:
            function_name = tool.function.name
            function_args = json.loads(tool.function.arguments)
            function_to_call = self.functions[function_name]

            try:
                function_response = function_to_call(
                    **function_args,
                )
                print(f"{tool.function.name}: {function_response[:100]}")
                self.send_odoo_msg(
                    f"🛠️Herramienta {function_name} ejecutada con los argumentos {function_args}"
                )
            except Exception as exc:
                print(f"{tool.function.name}: {exc}")
                self.send_odoo_msg(
                    f"❌Falló la herramienta {function_name} con los argumentos {function_args}",
                )
                function_response = self.error_response.format(
                    tool_name=function_name, tool_args=function_args
                )

            messages.append(
                {
                    "tool_call_id": tool.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            )


ia = Completions(AVANGENIO_API_KEY)

if __name__ == "__main__":
    prompt = "Eres un profesor de Python. Ayuda a los usuarios con sus dudas. Refuerza las respuestas con ejemplos de código y las frases con emojis"
    msg_list = [
        {
            "role": "system",
            "content": prompt,
        }
    ]
    print("Hola, pregúntame algo sobre Python o escribe 'salir' para salir")
    while True:
        question = input()
        if question == "salir":
            break

        msg_list.append({"role": "user", "content": question})
        ans = ia.send_msg(msg_list)
        msg_list.append({"role": "assistant", "content": ans})
