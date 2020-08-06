from aws_helper.aws_s3_helper.v1_args import Client


class CreateNewBucket(Client):
    """
            The current class provides create Bucket on AWS S3
            :param
                bucket_name  name of your bucket in AWS
            :param
                aws_access_key_id access id to your AWS account
            :param
                aws_secret_access_key secret access key to your AWS account
            :param
                region AWS maintains multiple geographic Regions, including Regions in North America, South America,
                Europe, China, Asia Pacific, and the Middle East.
        """

    def __init__(self, bucket_name: str = None, region: str = None):
        """Initialization variables"""
        super(CreateNewBucket, self).__init__()
        self.region = region
        self.bucket_name = bucket_name

    def buckets_list(self):  # show all available buckets
        """The function that returns available buckets"""
        response = self.get_client().list_buckets()
        for buckets in response["Buckets"]:
            print(f"{buckets['Name']}")

    def run(self):
        """The function that creates buckets"""
        if self.region is None:
            self.get_client().create_bucket(Bucket=self.bucket_name)
        else:
            self.get_client().create_bucket(Bucket=self.bucket_name,
                                            CreateBucketConfiguration={"LocationConstraint": self.region})


if __name__ == "__main__":
    obj = CreateNewBucket()  # bucket_name``
    obj.run()
