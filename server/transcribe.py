import argparse
import io
from datetime import datetime

from google.cloud import speech

# def save_file_to_gcloud(resp, bucket="my_bucket_name"):
    
#     filename = f"output_{datetime.now()}"
    
#     # Get the bucket that the file will be uploaded to.
#     storage_client = storage.Client()
#     bucket = storage_client.get_bucket(bucket)

#     # Create a new blob and upload the file's content.
#     my_file = bucket.blob(filename)

#     # create in memory file
#     output = io.StringIO("This is a test \n")
#     for i, result in enumerate(resp.results):
#         alternative = result.alternatives[0]
#         print("-" * 20)
#         f.write("-" * 20)
#         print(f"First alternative of result {i}")
#         f.write(f"First alternative of result {i}")
#         print(f"Transcript: {alternative.transcript}")
#         f.write(f"Transcript: {alternative.transcript}")
#     print("Finished writting the file")
#     f.close()

#     # upload from string
#     my_file.upload_from_string(output.read(), content_type="text/plain")

#     output.close()

#     # list created files
#     blobs = storage_client.list_blobs(bucket)
#     for blob in blobs:
#         print(blob.name)

#     # Make the blob publicly viewable.
#     my_file.make_public()

def transcribe_model_selection(
    speech_file: str,
    model: str,
) -> speech.RecognizeResponse:
    """Transcribe the given audio file synchronously with
    the selected model."""
    client = speech.SpeechClient()

    # with open(speech_file, "rb") as audio_file:
    #     content = audio_file.read()

    audio = speech.RecognitionAudio(uri=speech_file)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
        model=model,
    )
    response = client.recognize(config=config, audio=audio)

    # create in memory file
    f = open('output.txt', 'a')
    for i, result in enumerate(resp.results):
        alternative = result.alternatives[0]
        print("-" * 20)
        f.write("-" * 20)
        print(f"First alternative of result {i}")
        f.write(f"First alternative of result {i}")
        print(f"Transcript: {alternative.transcript}")
        f.write(f"Transcript: {alternative.transcript}")
    print("Finished writting the file")
    f.close()

    return response


def transcribe_open_ai()
    from openai import OpenAI
    client = OpenAI()

    audio_file= open("test_data/sample_1_on_1.mp4", "rb")
    transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
    )

def transcribe_gcp():
    # resp = transcribe_model_selection(speech_file="test_data/sample_1_on_1.mp4", model="latest_long")
    resp = transcribe_model_selection(speech_file="gcs://repwave_speech_output_test/conversation_test.mp4", model="latest_long")
    print(resp)

transcribe_open_ai()