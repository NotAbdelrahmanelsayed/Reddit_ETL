import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.reddit_pipeline import reddit_pipeline
from unittest.mock import patch
from praw import Reddit
from unittest.mock import Mock, patch


def fake_data():
    return [
        {
            "id": "1kc2mff",
            "title": "Guess skills are not transferable",
            "score": 379,
            "num_comments": 96,
            "author": "vitocomido",
            "created_utc": 1746083043.0,
            "url": "https://i.redd.it/p8t4uyicd4ye1.jpeg",
            "over_18": False,
            "edited": False,
            "spoiler": False,
            "stickied": False,
        },
        {
            "id": "1kbmyhk",
            "title": "What book after Fundamentals of Data Engineering?",
            "score": 64,
            "num_comments": 17,
            "author": "Khazard42o",
            "created_utc": 1746035940.0,
            "url": "https://www.reddit.com/r/dataengineering/comments/1kbmyhk/what_book_after_fundamentals_of_data_engineering/",
            "over_18": False,
            "edited": False,
            "spoiler": False,
            "stickied": False,
        },
    ]


@patch("pipelines.reddit_pipeline.pd.DataFrame.to_csv")
@patch("pipelines.reddit_pipeline.extract_post")
@patch("pipelines.reddit_pipeline.connect_reddit")
def test_reddit_pipeline(
    mock_reddit,
    mock_extract,
    mock_load_csv,
):
    """test reddit pipeline: connect_reddit -> extract_post -> transform_data -> load_to_csv"""

    # Mock Creating instance
    mock_reddit_instance = Mock()
    mock_reddit_instance.return_value = Reddit
    mock_reddit.return_value = mock_reddit_instance

    # Mock Extraction
    mock_extract.return_value = fake_data()

    # Mock Loading to csv
    mock_load_csv.return_value = None

    reddit_pipeline("file_name", "subreddit", "timefilter", None)

    assert mock_reddit.called, "connect_reddit() was not called"  # Test connecting to reddit
    assert mock_extract.called, "extract_post() was not called"  # Test Extraction
    assert mock_load_csv.called, "load_data_to_csv() was not called"  # Test Loading
