import socket
import threading
import time

print_lock = threading.Lock()   # Lock for safe printing

target = input("Enter target IP: ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

print(f"\nScanning {target} from port {start_port} to {end_port}\n")

# For efficiency evaluation
open_ports = []
total_ports = end_port - start_port + 1
start_time = time.time()


def detect_service(sock, port):
    try:
        sock.send(b"HEAD / HTTP/1.0\r\n\r\n")  # HTTP request header data as bytes
        banner = sock.recv(1024).decode(errors="ignore")

        if "HTTP" in banner:
            return "HTTP"
        elif "SSH" in banner:
            return "SSH"
        else:
            return "Unknown"

    except:
        return "Unknown"


# CHECK TO SEE IF PORT CAN HANDLE MULTIPLE CLIENTS
def multi_client_test(target, port):
    success = 0
    clients = []

    for i in range(3):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((target, port))

            clients.append(s)
            success += 1

        except:
            break

    for c in clients:
        c.close()

    if success >= 2:
        return "Multi-client supported"
    else:
        return "Limited clients"


def scan_port(port):
    retries = 3   # Retry logic: try each port up to 3 times

    for attempt in range(retries):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connect_ex((target, port))

            if result == 0: #if port is open
                service = detect_service(sock, port)
                multi = multi_client_test(target, port)

                with print_lock:
                    print(f"Port {port} OPEN → {service} | {multi}")
                    open_ports.append(port)

                sock.close()
                return   # Stop retrying if successful

            sock.close()

        except:
            pass

    # If all retries fail, do nothing


threads = []

for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = time.time()
scan_time = end_time - start_time

print("\nScan complete.")

# Scan efficiency evaluation
print("\n===== Scan Efficiency Evaluation =====")
print(f"Total ports scanned: {total_ports}")
print(f"Open ports found: {len(open_ports)}")
print(f"Open port list: {open_ports}")
print(f"Total scan time: {scan_time:.2f} seconds")
print(f"Average time per port: {scan_time / total_ports:.4f} seconds")