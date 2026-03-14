import requests
import time
import logging

# URLs to monitor
urls = [
    "https://tools-httpstatus.pickup-services.com/404",
    "https://tools-httpstatus.pickup-services.com/500",
    "https://tools-httpstatus.pickup-services.com/200"
]

# Logging configuration
logging.basicConfig(
    filename="uptime_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def check_urls():

    for url in urls:

        try:
            response = requests.get(url, timeout=5)
            status = response.status_code

            print(f"\nChecking URL: {url}")
            print(f"Status Code: {status}")

            logging.info(f"{url} -> {status}")

            if 400 <= status < 500:
                print(f"ALERT: 4xx error encountered for URL: {url}")
                logging.warning(f"4xx error at {url}")

            elif 500 <= status < 600:
                print(f"ALERT: 5xx error encountered for URL: {url}")
                logging.warning(f"5xx error at {url}")

            else:
                print("The website is UP and running.")

        except requests.exceptions.RequestException as e:

            print(f"ERROR connecting to {url}")
            logging.error(f"{url} connection error: {e}")


while True:

    check_urls()

    print("\nWaiting 10 seconds before next check...\n")

    time.sleep(10)