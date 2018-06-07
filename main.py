import pandas as pd
import twitter_connection as tc
import config
import os

def create_csv(file):
    open_file = open("files/" + file, 'r')
    save_file = open("csv/" + file.replace(".txt", ".csv"), 'w')
    df = pd.read_csv(open_file, sep="\t", header=None)
    df.to_csv(path_or_buf=save_file, sep="\t")


def create_csvs():
    for file in os.listdir("files"):
        if file.endswith(".txt"):
            create_csv(file)

    create_csv(config.user_name + ".txt")


def pull_tweets():
    twitter_handles = config.twitter_handles

    for user in twitter_handles:
        tc.connect(user)

    tc.connect(config.user_name)

def main():
    pull_tweets()
    create_csvs()


if __name__ == "__main__":
    main()