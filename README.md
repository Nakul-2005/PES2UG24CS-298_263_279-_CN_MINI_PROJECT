# Custom Port Scanner with Service Detection

## Overview

This project is a TCP-based Custom Port Scanner developed using Python socket programming and multithreading. The scanner is capable of detecting open ports on a target system, identifying services running on those ports using banner grabbing, checking multi-client support, and evaluating scan efficiency.

The project follows a client-server architecture:

* The **Target Server** hosts multiple TCP services on different ports.
* The **Scanner Client** scans the target system and analyzes the ports and services.

---

# Features

* TCP-based port scanning
* Open port detection
* Service detection using banner grabbing
* Concurrent scanning using multithreading
* Timeout handling
* Retry logic
* Multi-client support testing
* Scan efficiency evaluation
* Client-server communication

---

# Technologies Used

* Python
* Socket Programming
* TCP Protocol
* Multithreading

---

# Project Structure

```text
project-folder/
│
├── scanner.py          # Client-side port scanner
├── target_server.py    # Server-side target system
├── README.md
```

---

# How the Project Works

## 1. Target Server Side

The target server opens multiple TCP ports and listens for incoming client connections.

Example open ports:

* 5000
* 6000
* 8080

Different ports simulate different services by sending different response banners:

* HTTP banner
* SSH banner
* Custom/Unknown banner

The server also supports multiple simultaneous client connections using threads.

---

## 2. Scanner Client Side

The scanner accepts:

* Target IP address
* Start port
* End port

The scanner then:

1. Scans all ports concurrently using threads
2. Attempts TCP connection using `connect_ex()`
3. Detects open ports
4. Performs banner grabbing for service detection
5. Tests multi-client support
6. Uses retry logic for failed attempts
7. Measures scan efficiency statistics

---

# Concepts Implemented

| Concept                    | Description                                   |
| -------------------------- | --------------------------------------------- |
| TCP Communication          | Uses TCP sockets (`SOCK_STREAM`)              |
| Concurrent Scanning        | Uses multithreading for faster scanning       |
| Banner Grabbing            | Detects services from server response banners |
| Timeout Handling           | Prevents hanging connections                  |
| Retry Logic                | Retries failed scans up to 3 times            |
| Scan Efficiency Evaluation | Measures scan time and statistics             |
| Multi-client Support       | Checks simultaneous client handling           |

---

# Running the Project

## Step 1: Run the Target Server

On the target system:

```bash
python target_server.py
```

Expected output:

```text
Listening on port: 8080
Listening on port: 5000
Listening on port: 6000
Servers running....
```

---

## Step 2: Run the Scanner

On the scanner/client system:

```bash
python scanner.py
```

Example input:

```text
Enter target IP: 10.x.x.x
Start port: 4999
End port: 8081
```

---

# Example Output

```text
Port 5000 OPEN → SSH | Multi-client supported
Port 6000 OPEN → Unknown | Multi-client supported
Port 8080 OPEN → HTTP | Multi-client supported

===== Scan Efficiency Evaluation =====
Total ports scanned: 3083
Open ports found: 3
Open port list: [5000, 6000, 8080]
Total scan time: 4.12 seconds
Average time per port: 0.0013 seconds
```

---

# Scan Efficiency Evaluation

The scanner evaluates performance using:

* Total number of scanned ports
* Number of open ports found
* Total scan time
* Average time per port

This helps analyze scanner speed and efficiency.

---

# Limitations

* Only supports TCP scanning
* Basic banner-based service detection
* Does not perform vulnerability analysis
* Limited service fingerprinting

---

# Future Enhancements

* UDP port scanning
* Graphical User Interface (GUI)
* Advanced service fingerprinting
* Operating system detection
* Vulnerability scanning integration
* SSL/TLS detection support

---

# Conclusion

This project successfully demonstrates the implementation of a TCP-based Custom Port Scanner with Service Detection using Python. It provides practical understanding of socket programming, concurrent scanning, banner grabbing, retry logic, timeout handling, and scan efficiency evaluation.

The project also highlights the importance of client-server communication and network analysis techniques in modern computer networking.
