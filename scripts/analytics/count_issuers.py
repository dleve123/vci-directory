import argparse
import json
from git import Repo, Commit
from collections import namedtuple
from typing import Iterator, List
import pandas as pd

IssuerEntry = namedtuple('IssuerEntry', 'name iss website canonical_iss')
NAME_KEY = 'name'
ISS_KEY = 'iss'
WEBSITE_KEY = 'website'
CANONICAL_ISS_KEY = 'canonical_iss'
PARTICIPATING_ISSUERS_KEY = 'participating_issuers'

# This function was lifted from common.py instead of implemented there in effort
# to maintain strong boundaries between analytics code and validation code.
def read_issuer_entries_from_json(
    input_dict: dict
) -> List[IssuerEntry]:
    entries = {}
    for entry_dict in input_dict[PARTICIPATING_ISSUERS_KEY]:
        name = entry_dict[NAME_KEY].strip()
        iss = entry_dict[ISS_KEY].strip()
        website = entry_dict[WEBSITE_KEY].strip() if entry_dict.get(WEBSITE_KEY) else None
        canonical_iss = entry_dict[CANONICAL_ISS_KEY].strip() if entry_dict.get(CANONICAL_ISS_KEY) else None
        entry = IssuerEntry(
            name=name,
            iss=iss,
            website=website,
            canonical_iss=canonical_iss
        )
        entries[iss] = entry

    return list(entries.values())


def count_issuers(issuers_json: dict) -> int:
    entries_from_json = read_issuer_entries_from_json(issuers_json)
    num_issuers = len(entries_from_json)

    return num_issuers


def get_commits_changing_issuers_manifest(manifest_filepath: str) -> Iterator[Commit]:
    # TODO: should this only be run on `main`? Maybe.
    repo = Repo(".")
    scoped_commits = filter(
        lambda commit: manifest_filepath in commit.stats.files.keys(),
        repo.iter_commits(),
    )

    return scoped_commits


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Counts SHC issuers at input filepath. Writes CSV of counts to stdout."
    )
    parser.add_argument("input_filepath", help="JSON manifest file of issuers")
    args = parser.parse_args()

    commits_changing_issuers_manifest = get_commits_changing_issuers_manifest(
        args.input_filepath
    )
    data = []
    for commit in commits_changing_issuers_manifest:
        vci_issuers_at_commit = json.load(commit.tree[args.input_filepath].data_stream)
        total_num_issuers = count_issuers(vci_issuers_at_commit)
        commit_datetime = commit.committed_datetime.isoformat()
        data.append([commit_datetime, total_num_issuers])

    df = pd.DataFrame(data, columns=["commit_datetime", "total_num_issuers"])
    print(df.to_csv(index=False))
