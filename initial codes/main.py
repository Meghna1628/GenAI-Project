from prompt import Prompt
from hf_vlm_prompter import HuggingFaceVLM
from vertical_image_stacking import video_to_stacked_image
# import requests

def main():

    video_path = "/Users/meghnareddy/Downloads/AwkwardWillFerrellGIFbySaturdayNightLive-ezgif.com-gif-to-mp4-converter.mp4"
    output_image_path = "stacked_image.jpg"

    # Convert video to stacked image
    image_path = video_to_stacked_image(video_path, output_image_path)

    if not image_path:
        print("Error: Image generation failed.")
        exit()

    # # Check model's availability
    # model = "meta-llama/Llama-3.2-11B-Vision-Instruct"
    # url = f"https://huggingface.co/api/models/{model}"
    # headers = {"Authorization": "Bearer YOUR_API_KEY"}

    # response = requests.get(url, headers=headers)
    # print(response.json())

    # Your video event understanding prompt
    custom_prompt = "Describe the image."
    my_prompt = Prompt(custom_prompt)

    # print(f'my_prompt: {my_prompt}')

    # Initialize HuggingFacePrompter with the model of choice
    hf_prompter = HuggingFaceVLM(model="meta-llama/Llama-3.2-11B-Vision-Instruct")

    # Get response from HuggingFace API
    response = hf_prompter.prompt(my_prompt, image_path)

    # Print the response from the API
    if response:
        print("Model Response:", response)
    else:
        print("Error: No response received from Hugging Face API.")


if __name__ == "__main__":
    main()
