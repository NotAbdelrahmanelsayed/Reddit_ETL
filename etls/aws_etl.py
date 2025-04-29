import s3fs # type: ignore
from utils.constants import AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY

def connect_to_s3():
    try:
        s3 = s3fs.S3FileSystem(anon=True,
                               key=AWS_ACCESS_KEY, 
                               secret=AWS_SECRET_ACCESS_KEY)
        return s3
    except Exception as e:
        print(e)

def create_bucket_if_not_exist(s3: s3fs.S3FileSystem, bucket_name: str):
    try:
        if not s3.exists(bucket_name):
            s3.mkdir(bucket_name)
            print(f"bucket {bucket_name} created.")
        else:
            print(f'bucket {bucket_name} already exists.')
    except Exception as e:
        print(e)

def upload_to_s3(s3: s3fs.S3FileSystem, file_path: str, bucket_name: str, s3_filename: str):
    try:
        s3.put(file_path, rpath='/raw/' + s3_filename)
        print("File Uploaded to s3")
    
    except FileNotFoundError:
        print("The file was not found.")