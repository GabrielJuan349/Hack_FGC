import base64
# from google.cloud import texttospeech, speech
from google.cloud import texttospeech, speech

def text_to_speech(input_text : str, type: str = "base64"):
    """Synthesizes speech from the input string of text.

    Args:
        input_text (str): Text to be converted to speech

    Returns:
        base64 (str): Base64 encoded audio file
    """

    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=input_text)

    # Characteristic of the voice
    voice = texttospeech.VoiceSelectionParams(language_code="es-ES", name="es-ES-Wavenet-C", ssml_gender="FEMALE")

    audio_config = texttospeech.AudioConfig(pitch=0.8, speaking_rate=1.00, effects_profile_id=["medium-bluetooth-speaker-class-device"], audio_encoding=texttospeech.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
    
    return base64.b64encode(response.audio_content).decode('utf-8')

def speech_to_text(audio_encoded : str):
    """Synthesizes speech from the input string of text.

    Args:
        base64 (str): Base64 encoded audio file

    Returns:
        output_text (str): Text to be converted to speech
    """

    client = speech.SpeechClient()
    input_audio = base64.b64decode(audio_encoded)

    audio = speech.RecognitionAudio(content=input_audio)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code="es-ES",
    )

    response = client.recognize(config=config, audio=audio)

    output_text=""
    for result in response.results:
        output_text=result.alternatives[0].transcript
    return output_text


# def read_audio(file_name: str, type: str = "wav") -> bytes:
#     file_path = f"{file_name}.{type}"
    
#     # Verificar si el archivo existe
#     if not os.path.isfile(file_path):
#         raise FileNotFoundError(f"El archivo {file_path} no existe en el directorio {os.getcwd()}")
    
#     # Leer el contenido de audio de un archivo wav
#     with open(file_path, "rb") as audio_file:
#         # Leer el contenido del archivo y devolverlo
#         audio_content = audio_file.read()
#         return audio_content

# filename="SPEAKER_02_audio"
# # filename="prueba"

# audio = read_audio(filename)
# audio_input = base64.b64encode(audio).decode('utf-8')
# print("Audio leído correctamente")
# print(speech_to_text(audio_input))