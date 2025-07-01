import os
import requests
from dotenv import load_dotenv

load_dotenv()

def send_sms(phone, license_plate, brand, model, expiry_date):
    conn_id = os.getenv("SMSLINK_CONNECTION_ID")
    password = os.getenv("SMSLINK_PASSWORD")

    message = f"Salut! ITP-ul pentru {license_plate} ({brand} {model}) expira pe {expiry_date}. Te asteptam la adresa Str. Costache Negri 18, Pitesti!"

    phone = phone.strip().replace(" ", "").replace("+", "")

    if not phone.startswith("07") or len(phone) != 10:
        print(f"[X] Invalid phone format: {phone}")
        return

    params = {
        'connection_id': conn_id,
        'password': password,
        'to': phone,
        'message': message
    }

    try:
        response = requests.post("http://smslink.ro/sms/gateway/communicate/index.php", data=params)
        if "OK" in response.text:
            print(f"[✓] SMS sent to {phone}")
        else:
            print(f"[!] SMSLink ERROR: {response.text}")
    except Exception as e:
        print(f"[X] SMSLink connection error: {e}")
