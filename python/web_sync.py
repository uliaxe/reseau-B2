import requests
import os
import sys

def get_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        content = response.text
        print(content)
        return content  
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

def write_content(content, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    if len(sys.argv) != 2:
        print("Usage: python web_sync.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    content = get_content(url)

    output_directory = '/tmp/web_page'
    os.makedirs(output_directory, exist_ok=True)
    file_path = os.path.join(output_directory, 'web_page.html')

    write_content(content, file_path)
    print(f"Web content has been downloaded and saved to: {file_path}")

if __name__ == "__main__":
    main()
