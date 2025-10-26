# =============================================================================
# Network Packet Sniffer Configuration File
# =============================================================================

# --- Email Alert Settings ---
EMAIL_SETTINGS = {
    "enabled": True,                       # Enable/disable email alerts
    "smtp_server": "smtp.gmail.com",       # SMTP server (Gmail example)
    "smtp_port": 587,                      # TLS port
    "sender_email": "apekshan2005@gmail.com",
    "receiver_email": "billavaapeksha@gmail.com", # Where to send alerts
    "password": "nifvjmijroknzeqw",       # Use App Password (Gmail)
}

# --- Alert Thresholds (for anomaly detection) ---
ALERT_THRESHOLD = {
    "port_scan": 100,          # Max ports scanned per IP
    "syn_flood": 500,          # Max SYN packets per minute
    "icmp_flood": 200,         # Max ICMP packets per minute
    "udp_flood": 1000,         # Max UDP packets per minute
    "http_flood": 800,         # Max HTTP requests per minute
    "unusual_protocol": True,  # Enable alert for non-standard protocols
}

# --- Database and Logging Settings ---
DB_FILE = "traffic.db"         # SQLite database file
LOG_FILE = "alerts.log"        # Log file for alerts

# --- Time Window (in seconds) for rate-based alerts ---
ALERT_TIME_WINDOW = 60          # 60 seconds = 1 minute

# --- Protocol Whitelist (for unusual protocol detection) ---
WHITELISTED_PROTOCOLS = {
    1: "ICMP",
    6: "TCP",
    17: "UDP",
}

# --- Optional Advanced Settings ---
LOG_LEVEL = "INFO"             # Log level: DEBUG, INFO, WARNING, ERROR
MAX_LOG_SIZE = 10 * 1024 * 1024  # Max log size before rotation (10MB)
BACKUP_COUNT = 5               # Number of backup logs to keep
