import json
import base64
import logging
import requests
import numpy as np
from typing import Dict, List
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="/Users/meghnareddy/Desktop/LLM_Project/prompting/keys.env")  # Load environment variables from keys.env file

api_key = os.getenv("HUGGINGFACE_API_KEY")

from base_prompter import BasePrompter
from prompt import Prompt

class HuggingFaceVLM(BasePrompter):
    """ Prompter for HuggingFace's Vision-Language Models (VLMs).

    Requires the `HUGGINGFACE_API_KEY` environment variable to be set.

    Args:
        model (str): Model to use. Defaults to a vision-capable model.
    """

    def __init__(self, model: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.api_key = api_key  # Add your Hugging Face API key here
        if self.api_key is None:
            raise ValueError("HUGGINGFACE_API_KEY environment variable not set.")
        self.model = model

    def _make_header(self) -> Dict:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def _encode_image(self, image_path: str) -> str:
        """ Convert image to base64 for API request. """
        with open(image_path, "rb") as img_file:
            encoded_str = base64.b64encode(img_file.read()).decode("utf-8")
        
    #     # Debugging: Check length and first 100 characters
    #     print(f"Encoded image length: {len(encoded_str)}")
    #     print(f"Encoded image sample: {encoded_str[:100]}")  # Print first 100 chars

        return encoded_str
    

    def _make_payload(self, prompt: Prompt, image_path : str) -> str:
        """ Construct payload with text prompt and encoded image. """
        payload = {
            "inputs": {
                "image": self._encode_image(image_path), # Encode the stacked image
                "text": prompt.build()
                
            },
            "parameters": {
                "temperature": self.temperature,
                "top_p": self.top_p,
                "repetition_penalty": self.repetition_penalty,
                "num_return_sequences": 1,
                "max_new_tokens": self.max_tokens,
            },
            "options": {
                "use_cache": False,
                "wait_for_model": True,
            }
        }
        
        # # Include image if available
        # if prompt.image_url:
        #     payload["inputs"]["image"] = prompt.image_url  # Base64 or URL

        # print("Payload being sent:", json.dumps(payload, indent=2))  # Debugging step
        return json.dumps(payload)

    def _ask(self, prompt: Prompt, image_path : str) -> List[str]:
        """ Send a request to the Hugging Face API with an image and text prompt. """
        api_url = f"https://api-inference.huggingface.co/models/{self.model}"
        
        try:
            response = requests.post(
                api_url,
                headers=self._make_header(),
                data=self._make_payload(prompt, image_path)
            )

            print(f"Response Status Code: {response.status_code}")

            # Parse the response
            response_data = response.json()

            # Handle errors
            if "error" in response_data:
                logging.error(f"Hugging Face API Error: {response_data['error']}")
                return []

            # Return the first response
            responses = [r["generated_text"] for r in response_data]
            return responses[0] if responses else []

            
        except requests.exceptions.RequestException as e:
            logging.error(f"[HuggingFaceVLM] Request failed: {e}")
            return []
