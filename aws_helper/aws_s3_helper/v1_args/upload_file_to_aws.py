import os
from aws_helper.aws_s3_helper.v1_args import Client


class UploadToAws(Client):
    """
        The current class provides upload files and folders with file/files to AWS S3
        :param
            file_list return list of files
        :param
            bucket_name name of your bucket in AWS
        :param
            aws_access_key_id access id to your AWS account
        :param
            aws_secret_access_key secret access key to your AWS account
    """

    def __init__(self, file_list, bucket_name: str):
        """Initialization variables"""
        super(UploadToAws, self).__init__()
        self.file_list = file_list
        self.bucket_name = bucket_name

    def run(self):
        for file in self.file_list:
            object_name_on_bucket = os.path.relpath(file, os.environ.get('HOME'))
            self.get_client().upload_file(file, self.bucket_name, object_name_on_bucket)


if __name__ == '__main__':
    obj = UploadToAws(["/home/ross/new/test.py"],  # name of file
                      "test-bucket-name-ross-aws"  # name of bucket
                      )
    obj.run()
