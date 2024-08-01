import csv
from urllib.parse import urlparse
from datetime import datetime

def extract_domains_from_csv(csv_filename):
    domains = set()
    
    with open(csv_filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            referring_page = row.get("Referring Pages")
            if referring_page:
                parsed_url = urlparse(referring_page)
                domains.add(parsed_url.netloc)
    
    return domains

def save_domains_to_txt(domains):
    date_str = datetime.now().strftime("%d%m%y")
    output_filename = f"404_domain_{date_str}.txt"
    
    with open(output_filename, "w") as txtfile:
        for domain in sorted(domains):
            txtfile.write(f"{domain}\n")

# Replace "input.csv" with the path to your CSV file
domains = extract_domains_from_csv("404_errors_with_referring_pages.csv")
save_domains_to_txt(domains)
