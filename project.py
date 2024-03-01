import azure.cognitiveservices.speech as speechsdk

subscription_key = "dfac38a42a1e4787a372b3b063624eb1"
endpoint = "https://eastus.api.cognitive.microsoft.com/sts/v1.0/issuetoken"

speech_config = speechsdk.SpeechConfig(subscription=subscription_key, endpoint=endpoint)
speech_config.speech_recognition_language = "en-US"  

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

print("Speak something...")
result = speech_recognizer.recognize_once()

if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Recognized speech:", result.text)
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized")
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech recognition canceled:", cancellation_details.reason)
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details:", cancellation_details.error_details)

while True:
    a = 1