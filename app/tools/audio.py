import os
from gtts import gTTS


def text_to_speech(article):
    """
    Converts the news description to speech and saves the output to a file.

    Args:
        article (dict): A dictionary containing the 'uuid' and 'description' of the news article.

    Returns:
        str: The file path of the saved MP3 file.
    """
    uuid = article['uuid']
    description = article['description']

    directory = f"./swarmzero-data/output/{uuid}/"
    os.makedirs(directory, exist_ok=True)

    tts = gTTS(text=description, lang='en')

    mp3_filename = f"./swarmzero-data/output/{uuid}/audio.mp3"

    tts.save(mp3_filename)

    return mp3_filename
