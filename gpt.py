import keys as k
import os
from softtek_llm.chatbot import Chatbot
from softtek_llm.models import OpenAI
from softtek_llm.cache import Cache
from softtek_llm.vectorStores import PineconeVectorStore
from softtek_llm.embeddings import OpenAIEmbeddings
from softtek_llm.schemas import Filter
from dotenv import load_dotenv
from collections import Counter
import re

def start():
    load_dotenv()
    if k.OPENAI_API_KEY is None:
        raise ValueError("OPENAI_API_KEY not found in .env file")

    if k.OPENAI_API_BASE is None:
        raise ValueError("OPENAI_API_BASE not found in .env file")

    if k.OPENAI_EMBEDDINGS_MODEL_NAME is None:
        raise ValueError("OPENAI_EMBEDDINGS_MODEL_NAME not found in .env file")

    if k.OPENAI_CHAT_MODEL_NAME is None:
        raise ValueError("OPENAI_CHAT_MODEL_NAME not found in .env file")

    if k.PINECONE_API_KEY is None:
        raise ValueError("PINECONE_API_KEY not found in .env file")

    if k.PINECONE_ENVIRONMENT is None:
        raise ValueError("PINECONE_ENVIRONMENT not found in .env file")

    if k.PINECONE_INDEX_NAME is None:
        raise ValueError("PINECONE_INDEX_NAME not found in .env file")
    
def frequentWords(text):
    model = OpenAI(
        api_key=k.OPENAI_API_KEY,
        model_name=k.OPENAI_CHAT_MODEL_NAME,
        api_type="azure",
        api_base=k.OPENAI_API_BASE,
        verbose=False,
    )
    chatbot = Chatbot(
        model=model,
        description="From the following text, which are the 5 most commonly repeated phrases? Prepositions, Nouns, Adverbs, conjunctions and pronouns are not considered phrases. Answer only with the phrase separated by a space and then the amount of times that phrase was repeated. give me the list in a nice and readeble format with each element in a new line",
        verbose=False,
    )

    response = chatbot.chat(text)
    return response.message.content

def summary(text):
    model = OpenAI(
        api_key=k.OPENAI_API_KEY,
        model_name=k.OPENAI_CHAT_MODEL_NAME,
        api_type="azure",
        api_base=k.OPENAI_API_BASE,
        verbose=False,
    )
    chatbot = Chatbot(
        model=model,
        description="Summarize the following text. Separate into various paragraphs if needed",
        verbose=False,
    )

    response = chatbot.chat(text)
    return response.message.content

def keyIdeas(text):
    model = OpenAI(
        api_key=k.OPENAI_API_KEY,
        model_name=k.OPENAI_CHAT_MODEL_NAME,
        api_type="azure",
        api_base=k.OPENAI_API_BASE,
        verbose=False,
    )
    chatbot = Chatbot(
        model=model,
        description="Return 5 key concepts from the text in a nice and readable format, where each idea is in its own line",
        verbose=False,
    )

    response = chatbot.chat(text)
    return response.message.content

def normal(text):
    model = OpenAI(
        api_key=k.OPENAI_API_KEY,
        model_name=k.OPENAI_CHAT_MODEL_NAME,
        api_type="azure",
        api_base=k.OPENAI_API_BASE,
        verbose=False,
    )
    chatbot = Chatbot(
        model=model,
        verbose=False,
    )

    response = chatbot.chat(text)
    return response.message.content