import argparse
import common
import json
from git import Repo, Commit
from typing import Iterator


def count_issuers(issuers_json: dict) -> int:
    entries_from_json = common.read_issuer_entries_from_json(issuers_json)
    num_issuers = len(entries_from_json)

    return num_issuers

def get_commits_changing_issuers_manifest(manifest_filepath: str) -> Iterator[Commit]:
    repo = Repo('.')
    scoped_commits = filter(
        lambda commit: manifest_filepath in commit.stats.files.keys(),
        repo.iter_commits()
    )

    return scoped_commits


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Counts SHC issuers at input filepath')
    parser.add_argument('input_filepath', help='JSON manifest file of issuers')
    args = parser.parse_args()

    commits_changing_issuers_manifest = get_commits_changing_issuers_manifest(args.input_filepath)
    for commit in commits_changing_issuers_manifest:
        vci_issuers_at_commit = json.load(
            commit.tree[args.input_filepath].data_stream
        )
        num_issuers = count_issuers(vci_issuers_at_commit)

        print('commit datetime:', commit.committed_datetime.isoformat())
        print('number of issuers:', num_issuers)
        print('---')
