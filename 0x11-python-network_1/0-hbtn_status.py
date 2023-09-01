#!/usr/bin/python3
import urllib.request

def fetch_url_content(url):
    """
    Fetches the content of a URL and returns it as a string.

    Args:
        url (str): The URL to fetch the content from.

    Returns:
        str: The content of the URL as a string.
    """
    try:
        with urllib.request.urlopen(url) as response:
            html_content = response.read().decode('utf-8')
            return html_content

    except urllib.error.HTTPError as e:
        return f"Error: {e.code} {e.reason}"
    except urllib.error.URLError as e:
        return f"Error: {e.reason}"

if __name__ == "__main__":
    url_to_fetch = 'https://alx-intranet.hbtn.io/status'
    content = fetch_url_content(url_to_fetch)

    if content.startswith("Error"):
        print(content)
    else:
        print(content)

