import base64
import logging
import speech_recognition as sr
import os



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

    def recognize_speech_from_mic(self, onlistencallback, onstopcallback) -> str:
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=self.duration)
            print("Say something!")
            onlistencallback()
            audio = self.recognizer.listen(source, timeout=self.timeout, phrase_time_limit=self.phrase_time_limit)

            # Save the recorded audio to a .wav file in the working directory
            wav_file_path = "recorded_audio.wav"
            with open(wav_file_path, "wb") as wav_file:
                wav_file.write(audio.get_wav_data())

            try:
                # Convert the .wav file to base64
                audio_base64 = self.wav_to_base64(wav_file_path)
                onstopcallback()
                return audio_base64
            finally:
                # Keep the file for testing, so no deletion here
                logging.info(f"File {wav_file_path} has been saved for testing.")
                if os.path.isfile(wav_file_path):
                    os.remove(wav_file_path)



