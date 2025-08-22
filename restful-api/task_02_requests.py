#!/usr/bin/python3
"""Module that fetch and print post from JSONplaceHolder
and then fetch and save into csv file ."""


import requests
import csv


def fetch_and_print_posts():
    """Function fetching and printing all post titles"""

    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Function fetching and saving posts to a CSV file"""

    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        data = []
        for post in posts:

            data.append(
                {"id": post["id"],
                 "title": post["title"],
                 "body": post["body"]}
            )

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:

            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)

        print("Data successfully structured into list of dict. into posts.csv")


fetch_and_print_posts()
fetch_and_save_posts()
