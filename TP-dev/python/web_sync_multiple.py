import requests
import os
import sys

def fetch_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching content from {url}: {e}")
        return None

def save_to_file(url, content):
    filename = f"/tmp/web_{url.replace('https://', '').replace('/', '_')}.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Content from {url} saved to {filename}")

def process_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = file.read().splitlines()

    for url in urls:
        content = fetch_content(url)
        if content:
            save_to_file(url, content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python web_sync_multiple.py <file_path>")
        sys.exit(1)

    input_file = sys.argv[1]
    
    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    process_urls_from_file(input_file)