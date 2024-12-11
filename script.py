import requests

# URLs of the scam lists
LIST_URLS = [
    "https://raw.githubusercontent.com/elliotwutingfeng/GlobalAntiScamOrg-blocklist/refs/heads/main/global-anti-scam-org-scam-urls-pihole.txt",
    "https://raw.githubusercontent.com/Discord-AntiScam/scam-links/refs/heads/main/list.txt"
]

# Load the whitelist
def load_whitelist(filename):
    with open(filename, 'r') as file:
        return set(line.strip() for line in file if line.strip())

# Fetch the list from a URL
def fetch_list(url):
    response = requests.get(url)
    if response.status_code == 200:
        return set(line.strip() for line in response.text.splitlines() if line.strip())
    return set()

# Main function to fetch, merge and filter the lists
def main():
    # Load the whitelist
    whitelist = load_whitelist('whitelist.txt')

    # Initialize a set to hold all scam URLs
    scam_urls = set()

    # Fetch and merge the lists
    for url in LIST_URLS:
        scam_urls.update(fetch_list(url))

    # Remove whitelisted URLs
    filtered_urls = scam_urls - whitelist

    # Write the filtered list to a new file
    with open('antiscam.txt', 'w') as output_file:
        for url in sorted(filtered_urls):
            output_file.write(url + '\n')

    print(f"Filtered list created with {len(filtered_urls)} unique scam URLs.")

if __name__ == "__main__":
    main()