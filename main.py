import time

import chainlit as cl

from avatar import create_clip
from upload import upload_blob
from voice import text_to_wav
from document_chat import chat

from google.cloud import storage

def upload_to_bucket(blob_name, path_to_file, bucket_name='audio-examples-enterprise'):
    """Upload data to a bucket."""

    # Explicitly use service account credentials by specifying the private key file.
    storage_client = storage.Client()

    # Get the bucket that the file will be uploaded to.
    bucket = storage_client.get_bucket(bucket_name)

    # Create a new blob and upload the file's content.
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(path_to_file)
    time.sleep(2)
    print("UPLOADED TO BUCKET")

    return blob.public_url


@cl.on_message
async def main(message: cl.Message):

    response = chat(message.content)
    await cl.Message(
        content=str(response),
    ).send()

    await cl.Message(
        content="Generating audio..."
    ).send()

    filename = text_to_wav("en-GB-Neural2-D", str(response))
    elements = [
        cl.Audio(name=filename, path=f"./{filename}", display="inline")
    ]

    link_url = upload_blob(bucket_name='audio-examples-enterprise', source_file_name=f"./{filename}",
                destination_blob_name=filename)

    print("AUDIO LINK: ", link_url)

    await cl.Message(
        content="Audio:",
        elements=elements,
    ).send()

    await cl.Message(
        content="Generating video..."
    ).send()

    time.sleep(10)

    video_file = create_clip(link_url)
    # video_file = 'ec3ef606-dd41-4b8c-9ff5-afa8888c0bb0.mp4'

    elements = [
        cl.Video(name=video_file, path=f"./{video_file}", display="inline"),
    ]

    await cl.Message(
        content="Video",
        elements=elements,
    ).send()
