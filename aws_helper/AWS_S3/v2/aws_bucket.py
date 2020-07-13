from aws_helper.interfaces.aws_file_interface import AwsFileInterface
from aws_helper.AWS_S3.v2.base_client import Client


class AWSBucket(AwsFileInterface, Client):
    """The current class provides to create bucket,get a list of available buckets and delete bucket
        :param
                bucket_name  name of your bucket in AWS
        :param
                credentials access to AWS account
        :param
                region AWS maintains multiple geographic Regions, including Regions in North America, South America,
                Europe, China, Asia Pacific, and the Middle East.
    """

    @classmethod
    def create(cls, credentials: tuple, bucket_name: str, region: str = None):
        """The function that creates buckets"""
        if region is None:
            cls.get_client(*credentials).create_bucket(Bucket=bucket_name)
        else:
            cls.get_client(*credentials).create_bucket(Bucket=bucket_name,
                                                       CreateBucketConfiguration={"LocationConstraint": region})

    @classmethod
    def get_list_of_buckets(cls, credentials: tuple):
        """The function that returns available buckets"""
        response = cls.get_client(*credentials).list_buckets()
        for buckets in response["Buckets"]:
            print(f"{buckets['Name']}")

    @classmethod
    def delete_bucket_recursively(cls, credentials, bucket_name: str):
        """Provides to delete a bucket recursively"""
        bucket = cls.get_resource(*credentials).Bucket(bucket_name)
        bucket.objects.all().delete()
        bucket.delete()
