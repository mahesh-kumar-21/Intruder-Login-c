# capture_image.py
import cv2
import datetime
import os
import subprocess

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
if ret:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"intruder_{timestamp}.jpg"
    cv2.imwrite(filename, frame)
    cap.release()
    print(f"📸 Captured image saved as {filename}")
    print(f"{filename}|{timestamp}")
    
    # Send email with image
    try:
        subprocess.run(["python", "send_email.py", filename, timestamp])
    except Exception as e:
        print(f"❌ Error sending email: {e}")
else:
    print("❌ Failed to capture image")
