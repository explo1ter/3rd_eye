import socket
from _datetime import datetime


def port_scan(target_ip):

    try:
        h_name = socket.gethostbyname(target_ip)
        print(f"\nScanning target {h_name}")
        print("Time started : ", datetime.now())

        for port in range(0, 49151):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((h_name, port))
            if result == 0:
                print(f"Port {port}:open")
            sock.close()
        print("Scan completed time ended:",datetime.now())

    except socket.gaierror:
        print("Target hostname could not be resolved")
    except socket.error:
        print("Could not connect to the host")


if __name__ == "__main__":
    target_ip = input("Enter the ip address to scan : ")
    port_scan(target_ip)