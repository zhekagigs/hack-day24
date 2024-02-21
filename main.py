import chainlit as cl
from dataclasses import asdict
from gcp_wrap import try_gemi
from voice import text_to_wav


# @cl.on_chat_start
# async def main():
#     example = "Hello hackhaton peoples"

#     filename = text_to_wav("en-GB-Neural2-C", example)
    
#     elements = [
#         cl.Audio(name=filename, path=f"./{filename}", display="inline"),
#     ]

#     await cl.Message(
#         content="Here is an audio file",
#         elements=elements,
#     ).send()

#     await cl.Message(
#         content="This message should have an avatar!", author="Tool 1"
#     ).send()

#     await cl.Avatar(
#         name="Tool 1",
#         url="https://avatars.githubusercontent.com/u/128686189?s=400&u=a1d1553023f8ea0921fba0debbe92a8c5f840dd9&v=4",
#     ).send()


@cl.on_message
async def main(message: cl.Message):
    response = try_gemi(message.content)
    filename = text_to_wav("en-GB-Neural2-C", response)
    elements = [
        cl.Audio(name=filename, path=f"./{filename}", display="inline")
    ]
    await cl.Message(
        content=response,
        elements=elements,
    ).send()
