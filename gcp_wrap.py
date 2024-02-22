from consts import HTML_TEMPLATE
from vertexai.preview.generative_models import GenerativeModel


def try_gemi(prompt):
    gemini_pro_model = GenerativeModel("gemini-pro")

    system_prompt = f"""
        You know everything about BJSS Enterprise Agile.
        Keep it really short. You will be given questions, just give quick short answer, no headings. Two sentences max
    """
    print(system_prompt)
    model_response = gemini_pro_model.generate_content(system_prompt + prompt, generation_config={"temperature": 0})
    print("model_response\n",model_response)
    return model_response.text
