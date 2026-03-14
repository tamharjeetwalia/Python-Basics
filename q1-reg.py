import re

def validate_ip(ip):
    pattern = r'^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$'
    
    if re.match(pattern, ip):
        print("Valid IPv4 Address")
    else:
        print("Invalid IPv4 Address")

def validate_email(email):
    pattern = r'^[a-z0-9._%+-]+@gmail\.com$'
    
    if re.match(pattern, email):
        print("Valid Gmail Address")
    else:
        print("Invalid Gmail Address")
        print("Email must:")
        print("- Contain @gmail.com")
        print("- Use only lowercase letters, numbers, and permitted symbols")

ip = input("Enter IP Address: ")
email = input("Enter Gmail Address: ")

validate_ip(ip)
validate_email(email)