"""reddit.py
Functionas and classes for retrieving reddit threads
"""

from utils.console import print_markdown, print_step, print_substep
from dotenv import load_dotenv
import random
import praw
import os


class Reddit:

    def __init__(self, subreddit: str = 'askreddit'):
        load_dotenv()

        print_step("Connecting to Reddit...")

        # Initialize reddit object
        self.reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent="Accessing Reddit Threads",
            username=os.getenv("REDDIT_USERNAME"),
            password=os.getenv("REDDIT_PASSWORD")
        )

        # Create subredit instance
        self.subreddit = self.reddit.subreddit(subreddit)
