import argparse
import common
import json
from git import Repo, Commit
from typing import Iterator
import pandas as pd


def count_issuers(issuers_json: dict) -> int:
    entries_from_json = common.read_issuer_entries_from_json(issuers_json)
    num_issuers = len(entries_from_json)

    return num_issuers


def get_commits_changing_issuers_manifest(manifest_filepath: str) -> Iterator[Commit]:
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
