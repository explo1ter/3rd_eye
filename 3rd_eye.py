import socket
from _datetime import datetime
import pyfiglet


print("\n" + "*" * 65)
print(pyfiglet.figlet_format("              3rd_eye"))
print("*\t\t\tBy Nibil Mathew\t\t\t\t*")
print("*\t\t\tgithub:explo1ter\t\t\t*")
print("\n" + "*" * 65)
print("\n")


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
