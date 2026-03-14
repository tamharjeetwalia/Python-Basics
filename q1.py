def validate_ip(ip):

    parts = ip.split(".")

    if len(parts) != 4:
        print("Invalid IP Address: Must contain 4 octets")
        return

    for part in parts:

        if not part.isdigit():
            print("Invalid IP Address: Non-numeric value found")
            return

        num = int(part)

        if num < 0 or num > 255:
            print("Invalid IP Address: Value out of range (0-255)")
            return

    print("Valid IPv4 Address")


def validate_email(email):

    if "@gmail.com" not in email:
        print("Invalid Email: Must contain @gmail.com")
        return

    username = email.split("@")[0]

    allowed = "abcdefghijklmnopqrstuvwxyz0123456789._"

    for char in username:
        if char not in allowed:
            print("Invalid Email: Username contains invalid characters")
            return

    print("Valid Gmail Address")


ip = input("Enter IP Address: ")
email = input("Enter Gmail Address: ")

validate_ip(ip)
validate_email(email)