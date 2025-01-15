from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(_name_)

# Initialize Flask app
app = Flask(_name_)

# Twilio credentials
account_sid = 'ACbde67f6dcb1f9d17b8382ddeed8eb104'
auth_token = '694313cf48963bae31b79af293047249'
client = Client(account_sid, auth_token)

# Twilio phone number
TWILIO_PHONE_NUMBER = '+1 218 757 2555'

@app.route("/")
def index():
    logger.info("Index route accessed")
    return "AI Phone Agent is Running!"

@app.route("/make_call", methods=['POST'])
def make_call():
    logger.info("Make call route accessed")
    to_number = request.form.get('to')
    
    if not to_number:
        logger.error("No phone number provided")
        return "Phone number is missing", 400
    
    logger.info(f"Initiating call to: {to_number}")
    
    try:
        # Get the ngrok URL from form data or use default
        webhook_url = request.form.get('webhook_url', 'https://ec59-2409-40c2-3016-74cc-48f4-39fc-699c-880d.ngrok-free.app/voice')
        logger.info(f"Using webhook URL: {webhook_url}")
        
        call = client.calls.create(
            to=to_number,
            from_=TWILIO_PHONE_NUMBER,
            url=webhook_url
        )
        logger.info(f"Call initiated successfully with SID: {call.sid}")
        return f"Call initiated: {call.sid}"
    
    except Exception as e:
        logger.error(f"Error initiating call: {str(e)}", exc_info=True)
        return f"Error: {str(e)}", 500

@app.route("/voice", methods=['POST'])
def voice_response():
    logger.info("Voice route accessed")
    logger.debug(f"Request data: {request.form}")
    
    try:
        response = VoiceResponse()
        response.say("Hello! This is Alex from XYZ Corp. How can I assist you today?")
        response_str = str(response)
        logger.info("Voice response generated successfully")
        logger.debug(f"Response XML: {response_str}")
        return response_str
    
    except Exception as e:
        logger.error(f"Error in voice response: {str(e)}", exc_info=True)
        # Return a basic response in case of error
        response = VoiceResponse()
        response.say("I apologize, but I'm having trouble at the moment.")
        return str(response)

if _name_ == "_main_":
    print("Starting Flask app...")
    print("Make sure your ngrok URL is correct in the make_call function!")
    print("Current webhook URL:  https://ec59-2409-40c2-3016-74cc-48f4-39fc-699c-880d.ngrok-free.app/voice")
    app.run(debug=True)

import requests
import os

def test_tts():
    # Your Smallest AI API key
    api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI2NzdhMzI3OWM0NDE1ODdhYjZlODJhNjUiLCJ0eXBlIjoiYXBpS2V5IiwiaWF0IjoxNzM2MDYxNTYxLCJleHAiOjQ4OTE4MjE1NjF9.zxIiI4jVl21xaqi6rOX68aO69CB1lm9eCN_6z_9nS20"  # Replace this with your actual API key
    
    # Test message
    text = "Hello, this is a test message!"
    
    # API endpoint
    url = "https://waves.smallest.ai/apikeys"
    
    # Headers
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Request body
    data = {
        "text": text,
        "voice": "default",
        "language": "en-US"
    }
    
    print("Testing TTS API...")
    print(f"Endpoint: {url}")
    print(f"Text to convert: {text}")
    
    try:
        response = requests.post(url, headers=headers, json=data)
        print(f"Status code: {response.status_code}")
        print(f"Response: {response.text[:200]}")  # Print first 200 chars of response
        
        if response.status_code == 200:
            # Save the audio file
            with open('test_output.mp3', 'wb') as f:
                f.write(response.content)
            print("\nSuccess! Audio file saved as 'test_output.mp3'")
        else:
            print(f"\nError: API returned status code {response.status_code}")
            
    except Exception as e:
        print(f"\nError making request: {str(e)}")

if _name_ == "_main_":
    test_tts()