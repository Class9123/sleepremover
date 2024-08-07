import requests

# List of URLs to monitor
urls_to_monitor = [
    "https://share-whiteboard.onrender.com",
    "https://whatsappv6.onrender.com"
]

def check_urls():
    for url in urls_to_monitor:
        try:
            response = requests.get(url)
            if response.status_code != 200:
                print(f"Warning: {url} is not reachable.")
        except requests.ConnectionError:
            print(f"Error: {url} is down.")

if __name__ == "__main__":
    check_urls()
  
