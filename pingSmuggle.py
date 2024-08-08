from scapy.all import IP, ICMP, send

def send_ping_with_message(target_ip, message):
    # Create IP packet
    ip_packet = IP(dst=target_ip)

    # Create ICMP Echo Request packet
    icmp_packet = ICMP()

    # Set payload to the message
    message_bytes = message.encode('utf-8')
    icmp_packet.add_payload(message_bytes)

    # Combine IP and ICMP packets
    packet = ip_packet / icmp_packet

    # Send packet
    send(packet)

if __name__ == "__main__":
    target_ip = input("Enter IP: ") 
    message = "Message to be sent through ping"

    send_ping_with_message(target_ip, message)
