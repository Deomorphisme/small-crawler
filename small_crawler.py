#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import argparse
from urllib.parse import urlparse, urljoin

def ensure_https(url):
    if not url.startswith(('http://', 'https://')):
        return f'https://{url}'
    return url

def is_valid_url(url):
    # Excluding mailto or javascript link
    return not url.startswith(('mailto:', 'javascript:'))

def get_links(url, subdir=None):
    try:
        url = ensure_https(url)
        print("[+] URL seems correct...")

        print(f"[+] Trying to get a response from {url}...")
        response = requests.get(url)
        print("[+] The server responded!")

        # Check if the request was successful
        response.raise_for_status()

        # HTML parsing
        soup = BeautifulSoup(response.text, 'html.parser')
        print("[+] Soup successfully parsed")

        # Getting all tags that contains a link
        links = [a['href'] for a in soup.find_all('a', href=True)]
        print("[+] All tags found...")

        # Parse the base URL to get the domain
        base_domain = urlparse(url).netloc

        # Filter links to keep only those from the same domain and valid URLs
        same_domain_links = set() # Using a set to avoid duplicates
        for link in links:
            # Ensure the link is not empty
            if not link:
                continue

            full_link = urljoin(url, link)

            if not is_valid_url(full_link):
                continue

            try:
                link_domain = urlparse(full_link).netloc
                link_path = urlparse(full_link).path
            except ValueError:
                continue

            if link_domain == base_domain or not link_domain:
                if subdir:
                    # Check if the link path starts with the specified subdirectory
                    if link_path.startswith(f'/{subdir}/') or link_path == f'/{subdir}':
                        same_domain_links.add(full_link)
                else:
                    same_domain_links.add(full_link)

        return list(same_domain_links)
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except requests.exceptions.ConnectionError as conn_err:
        print(f'Connection error occurred: {conn_err}')
    except requests.exceptions.Timeout as timeout_err:
        print(f'Timeout error occurred: {timeout_err}')
    except requests.exceptions.RequestException as req_err:
        print(f'An error occurred: {req_err}')
    return []

if __name__ == "__main__":
    # Set up the argument parser
    parser = argparse.ArgumentParser(description='Retrieve all links from a webpage.')
    parser.add_argument('url', type=str, help='The URL of the webpage to analyze.')
    parser.add_argument('subdir', nargs='?', type=str, help='The subdirectory to crawl.', default=None)

    # Parse the command line arguments
    args = parser.parse_args()

    links = get_links(args.url, args.subdir)

    links_sorted = sorted(links)

    for link in links_sorted:
        print(f">> {link}")

    print(f"\n[+] Number of pages: {len(links_sorted)}")

