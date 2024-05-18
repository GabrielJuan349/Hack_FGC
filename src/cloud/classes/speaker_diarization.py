from collections import defaultdict
import torch
import base64
from pyannote.audio import Pipeline
from pydub import AudioSegment
import logging
import os
import tempfile

logging.basicConfig(level=logging.INFO)


class SpeakerDiarization:
    def __init__(self, base64: str):
        self.audio_base64 = base64
        self.pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization-3.1",
                                                 use_auth_token="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")
        self.pipeline.to(torch.device("cuda"))

    def extract_speaker_audio(self, audio, intervals):
        segments = [audio[start * 1000:end * 1000] for start, end in intervals]  # convert seconds to milliseconds
        return sum(segments)  # concatenate segments

    def base64_to_wav(self):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as wav_file:
            wav_file.write(base64.b64decode(self.audio_base64))
            return wav_file.name

    def wav_to_base64(self, file_path):
        with open(file_path, "rb") as wav_file:
            return base64.b64encode(wav_file.read()).decode("utf-8")

    def diarization(self):
        # Convert base64 audio to wav file
        wav_file_path = self.base64_to_wav()

        try:
            diarization = self.pipeline(wav_file_path)
            logging.info(f"Diarization completed:\n{diarization}")

            with open("audio.rttm", "w") as rttm:
                diarization.write_rttm(rttm)

            # Collect all time intervals for each speaker and calculate total speaking time
            speaker_intervals = defaultdict(list)
            speaker_durations = defaultdict(float)
            for turn, _, speaker in diarization.itertracks(yield_label=True):
                speaker_intervals[speaker].append((turn.start, turn.end))
                speaker_durations[speaker] += (turn.end - turn.start)

            if not speaker_intervals:
                logging.error("No speaker intervals found.")
                return None

            # Determine the most relevant speaker based on total speaking time
            most_relevant_speaker = max(speaker_durations, key=speaker_durations.get)
            logging.info(f"Total speaking time for each speaker:\n{speaker_durations}")

            # Load the original audio file
            audio = AudioSegment.from_wav(wav_file_path)

            # Extract and save audio for the most relevant speaker
            relevant_speaker_intervals = speaker_intervals[most_relevant_speaker]
            relevant_speaker_audio = self.extract_speaker_audio(audio, relevant_speaker_intervals)

            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as speaker_wav_file:
                relevant_speaker_audio.export(speaker_wav_file.name, format="wav")
                speaker_wav_path = speaker_wav_file.name

            # Convert the saved speaker audio to base64
            speaker_audio_base64 = self.wav_to_base64(speaker_wav_path)
            logging.info(f"Audio for the most relevant speaker ({most_relevant_speaker}) has been converted to base64.")

            return {
                "speaker_id": most_relevant_speaker,
                "speaker_duration": speaker_durations.get(most_relevant_speaker),
                "audio": speaker_audio_base64
            }

        finally:
            os.remove(wav_file_path)
            if 'speaker_wav_path' in locals() and os.path.exists(speaker_wav_path):
                os.remove(speaker_wav_path)
            logging.info(f"Temporary files have been deleted.")












