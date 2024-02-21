from consts import HTML_TEMPLATE
from vertexai.preview.generative_models import GenerativeModel

def try_gemi(prompt):
    gemini_pro_model = GenerativeModel("gemini-pro")

    system_prompt = f"""
        You are overachieving tester.
        Take it slow.
        Use Gherkin declarative style. Use Given, When, Then.
        Generate all Test scenarios based on user story and acceptance criteria.
        Including happy path scenarios, negative scenarios and edge cases.
        Write at least the amount of test as number of acceptence criteria given.
        Format as a simple html snippet. Use template {HTML_TEMPLATE}
        User story:
    """
    print(system_prompt)
    model_response = gemini_pro_model.generate_content(system_prompt + prompt, generation_config={"temperature": 0})
    print("model_response\n",model_response)
    return model_response.text