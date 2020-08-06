import os
from aws_helper.aws_s3_helper.v1_args import Client


class DownloadFile(Client):
    """
     The current class provides download files from AWS S3
        :param
            source path to file
        :param
            bucket_name name of your bucket in AWS
        :param
            aws_access_key_id access id to your AWS account
        :param
            aws_secret_access_key secret access key to your AWS account
        :param
            file_path full path to directory where you want to save a file
    """

    DEFAULT_FILE_PATH = "/home/ross/"

    # if DEFAULT_FILE_PATH == "":
    #     folder = input("Please enter your directory name:")
    #     DEFAULT_FILE_PATH = f"/home/ross/{folder}"
    def __init__(self, source: str, bucket_name: str, file_path=None):
        """Initialization variables"""
        super(DownloadFile, self).__init__()
        self.source = source
        self.bucket_name = bucket_name
        self.file_path = file_path
        if file_path is None:
            self.file_path = os.environ.get("HOME")
        self.file_name = os.path.basename(self.source)

    def run(self):
        """Download file and creates folder if folder in directory does not exist"""
        if not os.path.exists(self.file_path):
            os.makedirs(self.file_path)
        full_path = os.path.join(self.file_path, self.file_name)
        self.get_client().download_file(self.bucket_name, self.source, full_path)


if __name__ == "__main__":
    obj = DownloadFile("roos.txt",
                       "test-bucket-name-ross-aws")
    obj.run()
