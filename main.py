from google.oauth2 import service_account
from googleapiclient.discovery import build
import pandas as pd

# Path to your credentials file
KEY_FILE = 'google.json'
SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']

# Change the domain
SITE_URL = 'https://domain.co.id/'

# Authenticate and build the service
credentials = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)
service = build('searchconsole', 'v1', credentials=credentials)

# Function to fetch referring pages for a given URL
def get_referring_pages(service, url, site_url):
    try:
        inspection_request = {
            "inspectionUrl": url,
            "siteUrl": site_url
        }
        print(inspection_request)
        response = service.urlInspection().index().inspect(body=inspection_request).execute()
        print(response)
        referring_pages = response.get('inspectionResult', {}).get('indexStatusResult', {}).get('referringUrls',[])
        #append referring pages array to string
        referring_pages_str = ','.join(referring_pages)
        return referring_pages_str
    except Exception as e:
        print(f"Error fetching referring pages for {url}: {e}")
        return []

# Load URLs from CSV
df = pd.read_csv('Table.csv')
urls = df['URL'].tolist()  # Ensure your CSV has columns named 'url' and 'date'

# Collect URLs and their referring pages
referring_pages = []
for url in urls:
    linked_from = get_referring_pages(service, url, SITE_URL)
    referring_pages.append({
        'URL': url,
        'Referring Pages': linked_from
    })

# Convert to DataFrame and save to CSV
result_df = pd.DataFrame(referring_pages)
result_df.to_csv('404_errors_with_referring_pages.csv', index=False)

print("Data saved to 404_errors_with_referring_pages.csv")