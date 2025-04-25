from praw import Reddit # type: ignore
from utils.constants import POST_FIELDS
import sys

def connect_reddit(client_id, client_secret, user_agent) -> Reddit:
    try:
        reddit = Reddit(
            client_id=client_id, 
            client_secret=client_secret,
            user_agent=user_agent
        )
        print("Connected to reddit")
        return reddit
    
    except Exception as e:
        print(e)
        sys.exit(1)

def extract_post(reddit_instance, subreddit, time_filter, limit=None) -> None:
    subreddit = reddit_instance.subreddit(subreddit)
    posts = subreddit.top(time_filter=time_filter, limit=limit)

    post_list = []

    for post in posts:
        post_dict = vars(post)
        post = {key: post_dict[key] for key in POST_FIELDS}
    
    return post_list