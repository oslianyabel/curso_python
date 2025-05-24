json_tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current temperature for a given location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "Nombre de la ciudad. Solo la ciudad, sin el pais",
                    }
                },
                "required": ["location"],
                "additionalProperties": False,
            },
        },
    }
]