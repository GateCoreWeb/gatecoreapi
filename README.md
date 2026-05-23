# GateCore API Terminal Tester 

An interactive command-line tool designed for developers and security researchers to test the **GateCore OSINT API** endpoints quickly and efficiently.

##  Key Features
- **Real-time API Interaction:** Test every module of the GateCore API without writing extra code.
- **Human-Readable Output:** JSON responses are beautifully formatted with syntax highlighting.
- **Comprehensive Coverage:** Supports Phone Search, Telegram Analysis, Username Recon (500+ sites), IP/MAC Intelligence, and Temp Mail management.
- **Ease of Use:** Interactive menu-driven navigation.

##  Prerequisites
Ensure you have Python 3.8+ installed. You will need the `requests` and `rich` libraries.

```bash
pip install requests rich
```

## Setup & Usage
1. Clone your project or copy the `api_tester.py` file to your environment.
2. Open `api_tester.py` and ensure the `API_KEY` matches your key from the https://gatecore.xyz/profile.
3. Run the script:
```bash
python3 api_tester.py
```

## 📡 Available API Modules
- **Phone Search:** Carrier, region, and network status identification.
- **Telegram Search:** Deep profile analysis including Bio, Name, and UserID (if API keys are set).
- **Username Recon:** Cross-platform identity search using Maigret integration.
- **Network Intel:** IP geolocation, ASN info, and MAC manufacturer lookup.
- **Temp Mail:** Instant temporary email generation and inbox polling.

---
*Note: This tool is for testing purposes only. For production integration, refer to the https://api.gatecore.xyz*
