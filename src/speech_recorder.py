# Smart Contracts Scenario builder
# SmartContractsBuilder_SpeechRecorder - class for recording user speech

import sounddevice as sd
from scipy.io.wavfile import write
import time

subtype = 'PCM_16'
dtype = 'int16'


class SmartContractsBuilder_SpeechRecorder():
    def get_recording(_self):
        return './test-speech-data/export.wav'

    def stop_recording(_self, recorded_audio, audio_name):
        print("Stop recording")
        write(audio_name, 44100, recorded_audio)

    def start_recording(_self, audio_file_name):
        sd.default.samplerate = 44100
        sd.default.channels = 1
        myrecording = sd.rec(int(1 * 44100), dtype=dtype)
        # TODO: Stop and save recording
