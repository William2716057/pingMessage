# Ping with Message
This Python script allows you to send ICMP Echo Request (ping) packets with a custom message as the payload. The script utilizes the scapy library to create and send the packet.

## Features
- Sends a ping (ICMP Echo Request) to a target IP address.
- Allows embedding a custom message in the ping packet's payload.

## Requirements
- Python 3.x
- scapy library

You can install the required library using pip:
```
pip install scapy
```

## Usage
1. Clone the repository or download the script.
2. Run the script from the command line.
```
python pingSmuggle.py
```
3. Enter the target IP address when prompted.
4. The script will send a ping with the default message "Message to be sent through ping". You can change the message to suit your own needs.

## Important Notes
- Running this script may require administrative privileges depending on your operating system.
- Be mindful of the legality and ethical implications of sending ping packets with custom payloads, especially across networks you do not own or control.


