import json
from collections import defaultdict
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Collect VCI issuers by state issued. Write JSON to stdout."
    )
    parser.add_argument("metadata_filepath", help="JSON file of issuer metadata")
    args = parser.parse_args()

    with open(args.metadata_filepath) as metadata_file:
        metadata = json.load(metadata_file)

    issuer_websites_by_state = defaultdict(list)

    for issuer in metadata["issuer_metadata"]:
        for location in issuer["locations"]:
            if location["country"] == "US":
                issuer_websites_by_state[location["state"]].append(issuer["website"])

    print(json.dumps(issuer_websites_by_state, indent=2))
