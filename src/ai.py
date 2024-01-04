import json

from openai import OpenAI
from typing import List
from .model.MeetingTemplate import MeetingTemplate


def get_openai_client() -> OpenAI:
    with open('../server/certs/keys.json', 'r') as f:
        key = json.load(f)['openai']
        return OpenAI(api_key=key)
    
def process_meeting_summary(transcript_filepath: str, meeting_template: MeetingTemplate, additional_information: str=None):
    client = get_openai_client()

    with open(transcript_filepath, 'r') as f:
        transcript = f.read()
    system_context = meeting_template.generate_prompt()

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": system_context
            },
            {
                "role": "user",
                "content": transcript
            }],
        temperature=0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    chat_response = response.choices[0].message.content.strip()
    return chat_response

# def embed_knowledge_article(input_files: List[str]):
#     # Knowledge Article: https://cookbook.openai.com/examples/embedding_wikipedia_articles_for_search
#     import mwclient  # for downloading example Wikipedia articles
#     import mwparserfromhell  # for splitting Wikipedia articles into sections
#     import openai  # for generating embeddings
#     import pandas as pd  # for DataFrames to store article sections and embeddings
#     import re  # for cutting <ref> links out of Wikipedia articles
#     import tiktoken  # for counting tokens