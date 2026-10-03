import sqlite3
import os

# HARDCODED SECRET (Gitleaks / Secret Scanner will detect this)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
GITHUB_TOKEN = "ghp_1234567890abcdef1234567890abcdef1234"

def get_user(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # SQL INJECTION VULNERABILITY (Bandit / SAST will detect this)
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()

def ping_server(ip_address):
    # COMMAND INJECTION VULNERABILITY (Bandit / SAST will detect this)
    os.system(f"ping -c 4 {ip_address}")

if __name__ == "__main__":
    user = input("Enter username: ")
    print(get_user(user))
    
    ip = input("Enter IP to ping: ")
    ping_server(ip)
