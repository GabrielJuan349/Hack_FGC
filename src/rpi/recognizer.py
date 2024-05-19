import base64
import logging
import speech_recognition as sr
import os

from server_communication import ServerCommunication


class Recognizer:
    def __init__(self, duration=0.5, timeout=None, phrase_time_limit=None):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        self.duration = duration
        self.timeout = timeout
        self.phrase_time_limit = phrase_time_limit

    def wav_to_base64(self, file_path):
        with open(file_path, "rb") as wav_file:
            return base64.b64encode(wav_file.read()).decode("utf-8")

    def recognize_speech_from_mic(self) -> str:
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=self.duration)
            audio = self.recognizer.listen(source, timeout=self.timeout, phrase_time_limit=self.phrase_time_limit)

            # Save the recorded audio to a .wav file in the working directory
            wav_file_path = "recorded_audio.wav"
            with open(wav_file_path, "wb") as wav_file:
                wav_file.write(audio.get_wav_data())

            try:
                # Convert the .wav file to base64
                audio_base64 = self.wav_to_base64(wav_file_path)
                return audio_base64
            finally:
                # Keep the file for testing, so no deletion here
                logging.info(f"File {wav_file_path} has been saved for testing.")
                if os.path.isfile(wav_file_path):
                    os.remove(wav_file_path)


# Example usage:
if __name__ == "__main__":
    recognizer = Recognizer(duration=3)
    base64_audio = recognizer.recognize_speech_from_mic()

    # save the base64 audio to a file
    with open("base64_audio.txt", "w") as file:
         file.write(base64_audio) 

    # Example usage
    server_communication = ServerCommunication({'host': 'http://192.168.65.203:8000', 'endpoint': 'call_gemini'})

    response = server_communication.call_server(frame="frame", location="location",
                                                audio=base64_audio)
    print(response)


    # convert the base64 audio to a .wav file
    with open("audio.wav", "wb") as file:
        file.write(base64.b64decode(response["audio"]))

    print("Audio has been saved to audio.wav")

    # play the audio
    os.system("aplay audio.wav")
