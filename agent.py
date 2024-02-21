import uuid

from google.cloud import dialogflowcx_v3


async def sample_create_agent():
    # Create a client
    client = dialogflowcx_v3.AgentsAsyncClient()

    # Initialize request argument(s)
    agent = dialogflowcx_v3.Agent()
    agent.display_name = "display_name_value"
    agent.default_language_code = "default_language_code_value"
    agent.time_zone = "time_zone_value"

    request = dialogflowcx_v3.CreateAgentRequest(
        parent="parent_value",
        agent=agent,
    )

    # Make the request
    response = await client.create_agent(request=request)

    # Handle the response
    print(response)

def run_sample():
    # TODO(developer): Replace these values when running the function
    project_id = "hack-21feb"
    # For more information about regionalization see https://cloud.google.com/dialogflow/cx/docs/how/region
    location_id = "global"
    # For more info on agents see https://cloud.google.com/dialogflow/cx/docs/concept/agent
    agent_id = "14e5ef4c-9da6-4311-b7cd-942f69ec655f"
    agent = f"projects/{project_id}/locations/{location_id}/agents/{agent_id}"
    # For more information on sessions see https://cloud.google.com/dialogflow/cx/docs/concept/session
    session_id = uuid.uuid4()
    texts = ["Hello"]
    # For more supported languages see https://cloud.google.com/dialogflow/es/docs/reference/language
    language_code = "en-us"

    detect_intent_texts(agent, session_id, texts, language_code)


def detect_intent_texts(agent, session_id, texts, language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""
    session_path = f"{agent}/sessions/{session_id}"
    print(f"Session path: {session_path}\n")
    client_options = None
    agent_components = dialogflowcx_v3.AgentsClient.parse_agent_path(agent)
    location_id = agent_components["location"]
    if location_id != "global":
        api_endpoint = f"{location_id}-dialogflow.googleapis.com:443"
        print(f"API Endpoint: {api_endpoint}\n")
        client_options = {"api_endpoint": api_endpoint}
    session_client = dialogflowcx_v3.SessionsClient(client_options=client_options)

    for text in texts:
        text_input = session.TextInput(text=text)
        query_input = session.QueryInput(text=text_input, language_code=language_code)
        request = session.DetectIntentRequest(
            session=session_path, query_input=query_input
        )
        response = session_client.detect_intent(request=request)

        print("=" * 20)
        print(f"Query text: {response.query_result.text}")
        response_messages = [
            " ".join(msg.text.text) for msg in response.query_result.response_messages
        ]
        print(f"Response text: {' '.join(response_messages)}\n")


run_sample()