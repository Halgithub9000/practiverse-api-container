import anthropic
from dotenv import load_dotenv
import os
from typing import Protocol, Optional
from backend.constants.prompt_templates import STUDENT_PROFILER_PROMPT


class LLMStudentProfiler(Protocol):
    def generate_student_profile(self, pdf: str) -> Optional[str]:
        ...


class AnthropicHaikuStudentProfiler(LLMStudentProfiler):
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        self.model = "claude-3-5-haiku-20241022"
        self.client = anthropic.Anthropic(api_key=self.api_key)

    def generate_student_profile(self, pdf: str) -> Optional[str]:
        if not pdf:
            print(
                "Error: El texto del archivo está vacío. No se puede generar el perfil.")
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
                ]
            )
            return message.content[0].text
        except Exception as e:
            print(f"Error al generar el perfil con Anthropic: {e}")
            return None