# from deepeval.metrics import AnswerRelevancyMetric

import openai
from dotenv import load_dotenv
import os

from llama_index.core import ServiceContext, SimpleDirectoryReader, VectorStoreIndex, StorageContext, \
    load_index_from_storage


load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']

def get_query_engine():
    service_context = ServiceContext.from_defaults(chunk_size=1000)
    # check if storage already exists
    PERSIST_DIR = "./mystorage"
    if not os.path.exists(PERSIST_DIR):
        documents = SimpleDirectoryReader("./data").load_data()
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist(persist_dir=PERSIST_DIR)
    else:
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)

    query_engine = index.as_query_engine()
    return query_engine


ENGINE = get_query_engine()


def chat(prompt:str):
    response_object = ENGINE.query(prompt)
    print(response_object)
    return response_object
