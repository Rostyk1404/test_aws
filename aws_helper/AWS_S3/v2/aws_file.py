import os
from typing import Iterable
from aws_helper.interfaces.aws_file_interface import AwsFileInterface
from aws_helper.AWS_S3.v2.base_client import Client
from configparser import ConfigParser

conf_file = ConfigParser()
conf_file.read("/home/ross/test_aws_task/aws_helper/aws.conf")
credentials = (conf_file.get("AWS", "aws_access_key_id"),
               conf_file.get("AWS", "aws_secret_access_key"))


class AWSFile(AwsFileInterface, Client):
    """The current class provides us to upload folders with file/file/download files
        :param
                bucket_name  name of your bucket in AWS
        :param
                credentials access to AWS account
        :param
                file_list return list of files"""

    @classmethod
    def upload_files(cls, credentials: tuple, bucket_name: str, file_lists: Iterable[str] = None) -> None:
        """Function that upload file/files and folder with file to AWS"""
        for file in file_lists:
            object_name_on_bucket = os.path.relpath(file, os.environ.get('HOME'))
            cls.get_client(*credentials).upload_file(bucket_name, file, object_name_on_bucket)

    @classmethod
    def download_file(cls, credentials: tuple, bucket_name: str, source: str, file_path=None):
        """Download file and creates folder if folder in directory does not exist"""
        if file_path is None:
            file_path = os.environ.get("HOME")
        file_name = os.path.basename(source)

        if not os.path.exists(file_path):
            os.makedirs(file_path)
        full_path = os.path.join(file_path, file_name)
        cls.get_client(*credentials).download_file(bucket_name, source, full_path)

    @classmethod
    def delete_file(cls, credentials: tuple, bucket_name: str, file_path: str):
        """Function that delete file from AWS S3 and from inside the folder"""

        cls.get_client(*credentials).delete_object(Bucket=bucket_name, Key=file_path)
        return 204

#
# if __name__ == "__main__":
#     AWSFile.delete_file(credentials, "test-bucket-name-ross-aws",
#                         "docker.txt")
