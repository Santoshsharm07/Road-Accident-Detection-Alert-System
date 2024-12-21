import cv2
from detection import AccidentDetectionModel
import numpy as np
import os
import winsound
import threading
import time
import tkinter as tk
from twilio.rest import Client
from PIL import Image, ImageTk

emergency_timer = None
alarm_triggered = False  # Flag to track if an alarm has been triggered

model = AccidentDetectionModel("model.json", "model_weights.keras")
font = cv2.FONT_HERSHEY_SIMPLEX


#Sending Accident Photos to The number by sms
'''
def send_accident_photo_via_sms(photo_path):
    try:
        # Twilio credentials
        account_sid = "  "
        auth_token = "  "
        client = Client(account_sid, auth_token)
        
        # Send MMS with the photo
        message = client.messages.create(
            body="Alert: Accident detected! Here is the photo of the incident.",
            from_="   ",  # Twilio phone number
            to="   ",    # Verified recipient's phone number
            media_url=f"https://your-server.com/{photo_path}"  # Replace with actual hosted photo URL
        )
        print(f"Message sent with SID: {message.sid}")
    except Exception as e:
        print(f"Error sending SMS with photo: {e}")
'''





def save_accident_photo(frame):
    try:
        current_date_time = time.strftime("%Y-%m-%d-%H%M%S")
        directory = "accident_photos"
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = f"{directory}/{current_date_time}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Accident photo saved as {filename}")
    except Exception as e:
        print(f"Error saving accident photo: {e}")

def call_ambulance():
    try:
        # Replace these with your Twilio credentials
        account_sid = "   "
        auth_token = "  "
        client = Client(account_sid, auth_token)

        # Use a verified Twilio number or a purchased one
        twilio_number = "  "  # Replace with a valid Twilio number
        recipient_number = "  "  # Replace with the verified recipient number

        call = client.calls.create(
            url="https://handler.twilio.com/twiml/EHcbc30d7e5fb03b07f5c7116e0dacceaf",  #  URL
            to=recipient_number,
            from_=twilio_number
        )
        print(f"Call initiated successfully, SID: {call.sid}")
    except Exception as e:
        print(f"Error calling ambulance: {e}")

def show_alert_message():
    def on_call_ambulance():
        call_ambulance()
        alert_window.destroy()

    # Play the beep sound
    frequency = 2500
    duration = 2000
    winsound.Beep(frequency, duration)

    alert_window = tk.Tk()
    alert_window.title("Alert")
    alert_window.geometry("500x250")  # Size of the message box
    alert_label = tk.Label(alert_window, text="Alert: Accident Detected!\n\nIs the Accident Critical?", fg="black", font=("Helvetica", 16))
    alert_label.pack()

    # Load and display the GIF
    gif_path = "path_to_your_gif.gif"  # Correct the path here
    try:
        gif = Image.open(gif_path)
        resized_gif = gif.resize((150, 100), Image.BICUBIC)

        global gif_image
        gif_image = ImageTk.PhotoImage(resized_gif)
        gif_label = tk.Label(alert_window, image=gif_image)
        gif_label.pack()
    except Exception as e:
        print(f"Error loading GIF: {e}")

    call_ambulance_button = tk.Button(alert_window, text="Call Ambulance", command=on_call_ambulance)
    call_ambulance_button.pack()

    cancel_button = tk.Button(alert_window, text="Cancel", command=alert_window.destroy)
    cancel_button.pack()

    alert_window.mainloop()

def start_alert_thread():
    alert_thread = threading.Thread(target=show_alert_message)
    alert_thread.daemon = True  # Thread as daemon so it doesn't block the main thread
    alert_thread.start()

def startapplication():
    global alarm_triggered  
    video = cv2.VideoCapture("new.mp4")
    while True:
        ret, frame = video.read()
        if not ret:
            print("No more frames to read")
            break
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        roi = cv2.resize(gray_frame, (250, 250))

        pred, prob = model.predict_accident(roi[np.newaxis, :, :])
        if pred == "Accident" and not alarm_triggered:
            prob = round(prob[0][0] * 100, 2)
            
            if prob > 99:
                save_accident_photo(frame)
                alarm_triggered = True  
                start_alert_thread()  

            cv2.rectangle(frame, (0, 0), (280, 40), (0, 0, 0), -1)
            cv2.putText(frame, pred + " " + str(prob), (20, 30), font, 1, (255, 255, 0), 2)

        if cv2.waitKey(33) & 0xFF == ord('q'):
            return
        cv2.imshow('Video', frame)  

if __name__ == '__main__':
    startapplication()
