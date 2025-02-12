import argparse
import csv
import os
import time
from typing import Iterable, Mapping

import github

from . import responses


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--submit", action="store_true", help="Submit comments to GitHub")
    parser.add_argument("--repo", help="username/repo for GitHub repo")
    parser.add_argument("proposals_file", help="Path to CSV file containing responses")
    return parser


def load_proposals(proposals_file: str) -> Iterable[Mapping[str, str]]:
    data = []
    with open(proposals_file) as f:
        reader = csv.reader(f)
        headers: list[str] = []
        for header in next(reader):
            assert isinstance(header, str)
            header_lines = header.splitlines()
            if header_lines:
                headers.append(header_lines[0].strip())
            else:
                headers.append("")
        for row in reader:
            row_data = {}
            for header, item in zip(headers, row):
                assert isinstance(item, str)
                row_data[header] = item
            data.append(row_data)
    return data


def get_proposal_comments(proposals: Iterable[Mapping[str, str]]) -> Mapping[int, str]:
    comments = {}
    for proposal in proposals:
        gh_id = int(proposal["ID"])
        template_key = "ACCEPT_TEMPLATE" if proposal["Included"] == "TRUE" else "REJECT_TEMPLATE"
        template = getattr(responses, template_key)
        proposal_name = proposal["Proposal"].replace("<", "&lt;").replace("`&lt;", "`<")
        focus_area = proposal.get("Area", "").replace("<", "&lt;").replace("`&lt;", "`<")
        comment = template.format(title=proposal_name, focus_area=focus_area, type=proposal["Type"].lower())

        comments[gh_id] = comment
    return comments


def print_comments(comments: Mapping[int, str]):
    for gh_id, comment in comments.items():
        print(f"# {gh_id}\n\n{comment}\n\n----\n")


def submit_comments(repo: github.Repository.Repository, comments: Mapping[int, str]) -> None:
    for gh_id, comment in comments.items():
        issue = repo.get_issue(gh_id)
        print(issue)
        issue.create_comment(comment)
        time.sleep(1)


def main():
    parser = get_parser()
    args = parser.parse_args()

    if args.submit:
        if os.environ.get("GH_TOKEN") is None:
            raise ValueError("GH_TOKEN environment variable is required to submit to GitHub")
        if args.repo is None:
            raise ValueError("--repo is required to submit to GitHub")
        try:
            token = github.Auth.Token(os.environ["GH_TOKEN"].strip())
        except Exception:
            raise ValueError(f"Failed to read GH_TOKEN environment variable")
        gh = github.Github(auth=token)
        try:
            repo = gh.get_repo(args.repo)
            print(repo.permissions)
        except Exception:
            raise ValueError(f"Failed to lookup repo {args.repo}")
    else:
        repo = None


    proposals = load_proposals(args.proposals_file)
    comments = get_proposal_comments(proposals)

    if not args.submit:
        print_comments(comments)
    else:
        submit_comments(repo, comments)


if __name__ == "__main__":
    main()
