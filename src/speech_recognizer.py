# Smart Contracts Scenario builder
# SmartContractsBuilder_SpeechRecognizer - class for recognize user speech

# Example User scenario provided: Send money to other person if there is sufficient balance
# Example Solidity output: public transfer(address receiver, uint amount) {
#   balances[msg.sender] -= amount
#   balances[receiver] += amount
# }
from google.cloud import speech
import io


class SmartContractsBuilder_SpeechRecognizer():
    def recognize(_self, speech_audio_path):
        if _self.speech_client != None:
            print("Recognize user voice input:", speech_audio_path)

            client = speech.SpeechClient()

            with io.open(speech_audio_path, "rb") as audio_file:
                content = audio_file.read()

            audio = speech.RecognitionAudio(content=content)
            config = speech.RecognitionConfig(
                encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
                audio_channel_count=2,
                language_code="en-US",
            )

            response = client.recognize(config=config, audio=audio)

            for result in response.results:
                recognized_command = result.alternatives[0].transcript

    def __init__(_self):
        _self.speech_client = speech.SpeechClient()
        _self.speech_configs = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="en-US",
            audio_channel_count=2
        )
