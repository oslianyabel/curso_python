import json
import os

from dotenv import load_dotenv
from json_tools import json_tools
from openai import OpenAI

load_dotenv()

AVANGENIO_API_KEY = os.getenv(
    "AVANGENIO_API_KEY"
)  # recuerda porner esta variable dentro de .env

client = OpenAI(api_key=AVANGENIO_API_KEY, base_url="https://apigateway.avangenio.net")
prompt = "Eres un profesor de Python. Ayuda a los usuarios con sus dudas. Refuerza las respuestas con ejemplos de código y las frases con emojis"
msg_list = [
    {
        "role": "system",
        "content": prompt,
    }
]
MODEL = "agent-md"


def get_weather(location):
    return "30"


print(
    "Hola! Preguntame sobre la temperatura de una ciudad para probar las llamadas a funciones. También puedes crear tus propias funciones y agregarlas al bot. Escribe 'salir' para salir"
)
while True:
    question = input()
    if question == "salir":
        break

    msg_list.append({"role": "user", "content": question})
    response = client.chat.completions.create(
        model=MODEL,
        messages=msg_list,
        tools=json_tools,
    )

    tools = response.choices[0].message.tool_calls
    if tools:
        msg_list.append(
            response.choices[0].message
        )  # Agrega la llamada a la herramienta a los mensajes. Por esto me daba el error que no entendia

        print(f"{len(tools)} tools need to be called!")
        for tool in tools:
            print(tool.function.name)
            print(tool.function.arguments)

            if isinstance(tool.function.arguments, str):
                tool.function.arguments = json.loads(tool.function.arguments)

            if tool.function.name == "get_weather":
                function_response = get_weather(**tool.function.arguments)
                msg_list.append(
                    {
                        "tool_call_id": tool.id,
                        "name": tool.function.name,
                        "role": "tool",
                        "content": function_response,
                    }
                )
            else:
                print("Function not supported")

            response = client.chat.completions.create(
                model=MODEL,
                messages=msg_list,
            )

    ans = response.choices[0].message.content
    msg_list.append({"role": "assistant", "content": ans})
    print(ans)
