from utils.constants import CLIENT_ID, SECRET, OUTPUT_PATH
from etls.reddit_etl import (
    connect_reddit,
    extract_post,
    transform_data,
    load_data_to_csv,
)
import pandas as pd  


def reddit_pipeline(file_name, subreddit, time_filter="day", limit=None):
    # Connecting to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, "notabdelrahman")
    # Extraction
    posts = extract_post(instance, subreddit, time_filter, limit)
    posts_df = pd.DataFrame(posts)
    # file_path = f"{OUTPUT_PATH}/{file_name}-raw.csv"
    # load_data_to_csv(posts_df, file_path)

    # Transformation
    post_df = transform_data(posts_df)
    # Loading to csv
    file_path = f"{OUTPUT_PATH}/{file_name}.csv"
    load_data_to_csv(post_df, file_path)

    return file_path
