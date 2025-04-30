from pipelines.reddit_pipeline import reddit_pipeline
from utils.constants import OUTPUT_PATH
import os
import pytest
import pandas as pd
from datetime import datetime
from unittest.mock import patch
from etls.reddit_etl import connect_reddit, extract_post, transform_data, load_data_to_csv
from etls.aws_etl import connect_to_s3, create_bucket_if_not_exist, upload_to_s3
from pipelines.aws_s3_pipeline import upload_s3_pipeline
from utils.constants import AWS_BUCKET_NAME
from unittest.mock import MagicMock



