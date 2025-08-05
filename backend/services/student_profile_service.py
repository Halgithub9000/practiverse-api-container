import os
import json
from typing import Optional, Protocol

import anthropic
from dotenv import load_dotenv

from constants.prompt_templates import STUDENT_PROFILER_PROMPT, PROFILE_SUGGESTIONS_PROMPT


class LLMStudentProfiler(Protocol):
    def generate_student_profile(self, pdf: str) -> Optional[str]: ...

    def suggest_improvements(self, profile: str, interests: str) -> Optional[str]: ...


class AnthropicHaikuStudentProfiler(LLMStudentProfiler):
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        self.model = "claude-3-5-haiku-20241022"
        self.client = anthropic.Anthropic(api_key=self.api_key)

    def generate_student_profile(self, pdf: str) -> Optional[str]:
        if not pdf:
            print("Error: El texto del archivo está vacío. No se puede generar el perfil.")
            return None

        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=2000,
                system=STUDENT_PROFILER_PROMPT,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": "genera un perfil con el siguiente cv: " + pdf,
                            }
                        ],
                    }
                ],
            )
            json_string = message.content[0].text
            return json.loads(json_string)

        except Exception as e:
            print(f"Error al generar el perfil con Anthropic: {e}")
            return None

    def suggest_improvements(self, profile: str, interests: str) -> Optional[str]:
        if not profile or not interests:
            print("Error: El perfil o los intereses están vacíos. No se pueden generar sugerencias.")
            return None

        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=2000,
                system=PROFILE_SUGGESTIONS_PROMPT,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": f"Genera sugerencias de mejora para el perfil: {profile} con los intereses: {interests}",
                            }
                        ],
                    }
                ],
            )
            json_string = message.content[0].text
            return json.loads(json_string)
        except Exception as e:
            print(f"Error al generar sugerencias de mejora: {e}")
            return None
