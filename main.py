from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials,messaging



cred = credentials.Certificate("C:/Users/masih/Desktop/fcm/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
app = FastAPI()



@app.get('/')
def index():
    return "Fast A pi"

registration_token = 'YOUR_REGISTRATION_TOKEN'
response = messaging.send(messaging.Message(
    token=registration_token,
))

# print(response)

@app.post("/send-fcm-message")
async def send_fcm_message(token: str, message: str):
    # Construct the message payload
    payload = {
        'notification': {
            'title': 'New Message',
            'body': message
        }
    }
    # Send the message
    response = messaging.send(messaging.Message(
        token=token,
        notification=messaging.Notification(title='New Message', body=message)
    ))
    # Return the FCM response
    return {"success": True, "response": response}
