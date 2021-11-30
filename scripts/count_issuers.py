import argparse
import common


def count_issuers():
    parser = argparse.ArgumentParser(description='Counts SHC issuers')
    parser.add_argument('input_file', help='JSON file')

    args = parser.parse_args()
    entries_from_json = common.read_issuer_entries_from_json_file(args.input_file)

    print('Number of Issuers:', len(entries_from_json))

if __name__ == "__main__":
    count_issuers()
