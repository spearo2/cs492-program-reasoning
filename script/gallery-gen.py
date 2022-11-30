#!/usr/bin/python3

import getpass
import re

from github import Github

cols = 5


def print_line():
    line = "|"
    for i in range(cols):
        line += ":-:|"
    return line


def main():
    username = input("Username: ")
    password = getpass.getpass()
    g = Github(username, password)
    org = g.get_organization("prosyslab-classroom")
    repo = org.get_repo("cs492-program-reasoning")
    issues = repo.get_issues(labels=["art competition"])
    index = 0
    line = "|"
    line_printed = False
    for issue in issues:
        title = issue.title.split("] ")[1]
        issue_url = issue.url.replace("api.", "").replace("/repos/", "/")
        image_url = re.search(r"https.+png", issue.body).group(0)
        user = issue.user.login
        user_url = issue.user.url
        line += f"[![{title}]({image_url})]({issue_url}){title}<br>by [{user}]({user_url})|"
        index += 1
        if index % cols == 0:
            if not line_printed:
                line += "\n"
                line_printed = True
                line += print_line()
            line += "\n|"
    print(line)


if __name__ == "__main__":
    main()
