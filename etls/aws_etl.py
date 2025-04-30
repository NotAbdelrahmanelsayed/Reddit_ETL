import s3fs  # type: ignore
from utils.constants import logger, AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY


def connect_to_s3():
    try:
        s3 = s3fs.S3FileSystem(
            anon=False, key=AWS_ACCESS_KEY, secret=AWS_SECRET_ACCESS_KEY
        )
        return s3
    except Exception as e:
        logger.exception(e)


def create_bucket_if_not_exist(s3: s3fs.S3FileSystem, bucket_name: str):
    try:
        if not s3.exists(bucket_name):
            s3.mkdir(bucket_name)
            logger.info(f"bucket {bucket_name} created.")
        else:
            logger.info(f"bucket {bucket_name} already exists.")
    except Exception as e:
        logger.exception(e)


def upload_to_s3(
    s3: s3fs.S3FileSystem, file_path: str, bucket_name: str, s3_filename: str
):
    try:
        s3.put(file_path, bucket_name + "/raw/" + s3_filename)
        logger.info("File Uploaded to s3")

    except FileNotFoundError:
        logger.info("The file was not found.")
