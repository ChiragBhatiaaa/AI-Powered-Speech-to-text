import tkinter as tk
from PIL import ImageTk, Image
import azure.cognitiveservices.speech as speechsdk

subscription_key = "dfac38a42a1e4787a372b3b063624eb1"
endpoint = "https://eastus.api.cognitive.microsoft.com/sts/v1.0/issuetoken"

def on_button_click():
    print("Button clicked!")
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, endpoint=endpoint)
    speech_config.speech_recognition_language = "en-US"

    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    print("Speak something...")
    result = speech_recognizer.recognize_once()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        label.config(text=result.text)
    elif result.reason == speechsdk.ResultReason.NoMatch:
        label.config(text = "No speech could be recognized")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech recognition canceled:", cancellation_details.reason)
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details:", cancellation_details.error_details)


root = tk.Tk()
root.title("Speech to text app")

# Load microphone image
image_path = "mic.jpg"  # Replace with the path to your microphone image
image = Image.open(image_path)
image = image.resize((500, 500), Image.ANTIALIAS)  # Adjust the size as per your requirement
photo = ImageTk.PhotoImage(image)

# Create button with microphone image
button = tk.Button(root, image=photo, command=on_button_click)
button.pack(pady=50)

label_text = "Your speech appears here"
label = tk.Label(root, text=label_text, font=("Arial", 16))
label.pack(pady=10)

root.mainloop()


