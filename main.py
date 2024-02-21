import chainlit as cl
from dataclasses import asdict
from gcp_wrap import try_gemi

@cl.on_chat_start
async def main():
    elements = [
        cl.Audio(name="example.mp3", path="./example.mp3", display="inline"),
    ]
    await cl.Message(
        content="Here is an audio file",
        elements=elements,
    ).send()


@cl.on_message
async def main(message: cl.Message):
    response = try_gemi(message.content)
    response_dict = asdict(response)
    await cl.Message(
        content='TRANSLATION:\n\n' + response.translation + '\n\n'
                + 'SCORE: ' + str(response.score) + '\n\n'
                + response.reason + '\n\n'
    ).send()
