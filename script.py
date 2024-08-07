import requests
import datetime
import time

def fetch_urls(urls):
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Successfully fetched {url} at {datetime.datetime.now()}")
            else:
                print(f"Failed to fetch {url}. Status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    urls = [
        "https://whatsappv6.onrender.com",
        "https://share-whiteboard.onrender.com"
    ]

    while True:
        fetch_urls(urls)
        time.sleep(540)  # Sleep for 540 seconds (9 minutes)
