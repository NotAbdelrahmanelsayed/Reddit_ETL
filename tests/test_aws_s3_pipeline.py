import sys 
import os 

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from unittest.mock import Mock, MagicMock, patch
from pipelines.aws_s3_pipeline import upload_s3_pipeline
from utils.constants import AWS_BUCKET_NAME
"""
We are testing

from utils.constants import AWS_BUCKET_NAME
from etls.aws_etl import connect_to_s3, create_bucket_if_not_exist, upload_to_s3


def upload_s3_pipeline(ti):
    file_path = ti.xcom_pull(
        task_ids="reddit_extraction", dag_id="etl_reddit_pipeline", key="return_value"
    )
    s3 = connect_to_s3()
    create_bucket_if_not_exist(s3, AWS_BUCKET_NAME)
    upload_to_s3(s3, file_path, AWS_BUCKET_NAME, file_path.split("/")[-1])
"""


@patch("pipelines.aws_s3_pipeline.upload_to_s3")
@patch("pipelines.aws_s3_pipeline.create_bucket_if_not_exist")
@patch("pipelines.aws_s3_pipeline.connect_to_s3")
def test_upload_s3_pipeline(mock_s3, mock_create_bucket, mock_upload_to_s3):
    # Mock xcom_pull
    mock_xcom = MagicMock()
    mock_xcom.xcom_pull.return_value = "fake/path"

    # Mock s3 connection
    mock_s3_connection = Mock()
    mock_s3.return_value = mock_s3_connection


    # Mock Crete bucket behaviour
    mock_create_bucket.return_value = True

    # Mock upload_to_s3
    mock_upload_to_s3.return_value = True
    
    
    upload_s3_pipeline(mock_xcom)

    assert mock_s3.called, "connect_to_s3() is not called"
    mock_create_bucket.assert_called_once_with(mock_s3_connection, AWS_BUCKET_NAME), "create_bucket_if_not_exist() is not called"
    mock_upload_to_s3.assert_called_once_with(mock_s3_connection, 'fake/path', AWS_BUCKET_NAME, "path")