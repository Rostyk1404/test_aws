import boto3
from aws_helper.v1_args.abstract_client import Client
from configparser import ConfigParser


class DeleteBucketsFoldersAndFiles(Client):
    """
        The current class provides delete Buckets on AWS S3
        :param
            bucket_name  name of your bucket in AWS
        :param
            aws_access_key_id access id to your AWS account
        :param
            aws_secret_access_key secret access key to your AWS account
        :param
            folder_name folder name in Bucket.
        :param
            file_name file name in Bucket.
    """

    def __init__(self, bucket_name: str, folder_name: str = None, file_name: str = None, aws_access_key_id: str = None,
                 aws_secret_access_key: str = None):
        """Initialization variables"""
        super(DeleteBucketsFoldersAndFiles, self).__init__()
        conf_file = ConfigParser()
        conf_file.read("/home/ross/test_aws_task/aws_helper/aws.conf")
        self.aws_access_key_id = conf_file.get("AWS", "aws_access_key_id") \
            if aws_access_key_id is None else aws_access_key_id
        self.aws_secret_access_key = conf_file.get("AWS", "aws_secret_access_key") \
            if aws_secret_access_key is None else aws_secret_access_key
        self.bucket_name = bucket_name
        self.folder_name = folder_name
        self.file_name = file_name

    def get_resource(self):
        return boto3.resource('s3', aws_access_key_id=self.aws_access_key_id,
                              aws_secret_access_key=self.aws_secret_access_key)

    def delete_all_files_inside_bucket(self):
        self.get_resource().Bucket(self.bucket_name).objects.all().delete().clear()

    def delete_bucket_recursively(self):
        bucket = self.get_resource().Bucket(self.bucket_name)
        bucket.objects.all().delete()
        bucket.delete()

    def delete_folder_and_file_recursively(self):
        """Provides to delete folder/folders with file/files in AWS S3"""

        bucket = self.get_resource()
        bucket.objects.filter(Prefix=self.folder_name).delete()

    #

    # def run(self):
    #     if not hasattr(self, 'folder_name'):
    #         self.delete_folder_and_file_recursively()
    #     elif not hasattr(self, 'folder_name', "file_name"):
    #         self.delete_file()


if __name__ == "__main__":
    obj = DeleteBucketsFoldersAndFiles("test-bucket-name-ross-aws", "docker.txt")
    obj.delete_file()
