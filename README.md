# Road-Accident-Detection-Alert-System

Overview

The Road Accident Detection and Alert System is an innovative solution designed to detect road accidents in real-time using object detection and  AI techniques. Once an accident is detected, the system:

Sends Emergency Alerts: Uses the Twilio API to notify and call nearby hospitals.

Includes Geographical Location: Shares the accident's exact location to assist emergency responders.

Minimizes Response Time: Ensures prompt medical assistance by prioritizing nearby hospitals.

Features

Real-Time Accident Detection: Utilizes YOLO for quick and accurate accident detection.

Twilio API Integration: Sends SMS and call notifications for emergencies.

Location Tracking: Captures and shares the exact location of the accident using GPS.

Scalable Backend: Efficiently processes accident data and manages communication.

User-Friendly Dashboard: Displays data and system operations for real-time monitoring.

Prerequisites

Python 3.8 or higher

Required Libraries: yolov5, opencv-python, pandas, numpy, flask, requests

Twilio Account (API credentials)

Google Maps API Key for geolocation services

Installation

Clone the repository:

git clone https://github.com/your-username/road-accident-detection.git
cd road-accident-detection

Install dependencies:

pip install -r lib.txt

Configure environment variables:

Create a .env file in the project root directory.

Add the following details:

TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
GOOGLE_MAPS_API_KEY=your_google_maps_api_key

Start the application:

python app.py

Twilio API Integration

The Twilio API facilitates emergency notifications via SMS and phone calls. The process includes:

Setting Up Twilio:

Sign up for a Twilio account.

Obtain your Account SID, Auth Token, and a verified phone number.

Sending Alerts:

The system generates an alert with:

A brief description of the incident.

T

Run the application and ensure all APIs and detection models are configured.

Monitor the dashboard for real-time accident detection.

Emergency alerts are triggered automatically upon detecting an accident.

Project Structure

models/: Pre-trained YOLO model files

scripts/: Detection and alert scripts

app.py: Main application file

templates/: Frontend dashboard templates

static/: Static files (CSS, JS)

Contributions

Contributions are welcome! Fork the repository and create a pull request with your improvements.

License

This project is licensed under the MIT License. See the LICENSE file for more details.

Contact

Data Set is from kagggle Road Accident System Dataset

For queries or feedback, reach out to:

Email: 07santoshsharma2004@gmail.com


