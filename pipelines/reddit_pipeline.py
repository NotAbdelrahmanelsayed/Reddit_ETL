from utils.constants import CLIENT_ID, SECRET
from etls.reddit_etl import connect_reddit, extract_post

def reddit_pipeline(file_name, subreddit, time_filter="day", limit=None):
    # Connecting to reddit instance 
    instance = connect_reddit(CLIENT_ID, SECRET, 'notabdelrahman')
    # Extraction
    posts = extract_post(instance, subreddit, time_filter, limit)
    # Transformation 
    # Loading