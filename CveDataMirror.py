import requests
import json
import time

base_url = "https://services.nvd.nist.gov/rest/json/cves/2.0"

params = {
    "startIndex": 0,  # Starting point for the data
    "resultsPerPage": 2000,  # Maximum results per page (2000 is the limit)
}


def fetch_cves():
    all_cves = []
    while True:
        response = requests.get(base_url, params=params)
        if response.status_code != 200:
            print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
            break

        # Load the data as JSON
        data = response.json()
        cve_items = data.get("vulnerabilities", [])
        if not cve_items:
            break

        all_cves.extend(cve_items)
        print(f"Fetched {len(cve_items)} CVEs...")

        # Update the start index for the next page
        params["startIndex"] += len(cve_items)

        # Check if we've fetched all results
        if len(cve_items) < params["resultsPerPage"]:
            break

        time.sleep(1)

    return all_cves


def save_to_file(cve_data, filename="cve_data.json"):
    with open(filename, "w") as file:
        json.dump(cve_data, file, indent=4)
    print(f"Data saved to {filename}")


if __name__ == "__main__":
    cve_data = fetch_cves()
    save_to_file(cve_data)
