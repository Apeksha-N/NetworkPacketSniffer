Network Packet Sniffer with Alert System

A real-time network monitoring and threat detection solution built using Python. It captures live packets, detects anomalies using rule-based security checks, logs critical events, and alerts administrators instantly through email. Interactive visual dashboards offer deep insights into network activity, making this tool ideal for security analysis and incident response.

Features

Real-time Packet Capture (Scapy)
Automated Threat & Anomaly Detection
SQLite Storage for Efficient Forensics
Email Alerts for Suspicious Traffic
Interactive Dashboard (Dash + Plotly + Matplotlib)
User-Friendly Tkinter GUI
Multithreaded Performance

Tech Stack
Programming Language - Python
Packet Capture - Scapy
Database	- SQLite
Visualization	- Matplotlib, Plotly, Dash, Pandas
GUI	- Tkinter
Alerts	- SMTP, email.mime
Performance	- Multithreading

Project Structure
NetworkPacketSniffer/
│
└── Network_Sniffer/
    ├── sniffer.py        # Real-time packet capture
    ├── gui.py            # Desktop UI
    ├── dashboard.py      # Interactive analytics dashboard
    ├── database.py       # SQLite operations
    ├── alerts.py         # Email alert handling
    ├── plotter.py        # Visualizations and charts
    ├── config.py         # SMTP credentials & settings
    ├── alerts.log        # Recorded threat alerts
    └── traffic.db        # Stored packet metadata

Running the Project
Install Dependencies
pip install scapy matplotlib pandas dash plotly

Step 1: Start Packet Capture
python Network_Sniffer/sniffer.py

Step 2: Launch GUI
python Network_Sniffer/gui.py

Step 3: Visual Dashboard (Optional)
python Network_Sniffer/dashboard.py
