from flask import Flask
from flask_restful import Resource, Api
from aws_helper.v2.aws_bucket import AWSBucket
from aws_helper.v2.aws_file import AWSFile
from aws_helper.v2.aws_folder import AWSFolder
from configparser import ConfigParser

app = Flask(__name__)
api = Api(app)

conf_file = ConfigParser()
conf_file.read("/home/ross/test_aws_task/aws_helper/aws.conf")
# credentials = {"aws_access_key_id": conf_file.get("AWS", "aws_access_key_id"),
#                "aws_secret_access_key": conf_file.get("AWS", "aws_secret_access_key")}
credentials = (conf_file.get("AWS", "aws_access_key_id"),
               conf_file.get("AWS", "aws_secret_access_key"))


class Bucket(Resource):

    def get(self):
        list_of_buckets = AWSBucket.get_list_of_buckets(credentials)
        return list_of_buckets, 200

    def post(self, bucket_name):
        # повинен викликатися клас який буде витягати з бд креди
        AWSBucket.create(credentials, bucket_name=bucket_name)
        return 201

    def delete(self, bucket_name):
        AWSBucket.delete_bucket_recursively(credentials, bucket_name=bucket_name)
        return 204


class File(Resource):
    def get(self, bucket_name: str, source: str, file_path=None):
        """Dowload files from bucket"""
        AWSFile.download_file(credentials, bucket_name=bucket_name, source=source, file_path=file_path)
        return "File successfully downloaded", 200

    def post(self, bucket_name: str, file_lists: str):
        """Upload files in bucket"""
        AWSFile.upload_files(credentials, bucket_name=bucket_name, file_lists=file_lists)
        return "File successfully uploaded ", 201


class Folder(Resource):
    def delete(self, bucket_name: str, folder_name: str = None):
        """:return delete buckets"""
        if folder_name is None:
            AWSFolder.delete_all_data_in_bucket(credentials, bucket_name=bucket_name)
        else:
            AWSFolder.delete_folder_recursively(credentials, bucket_name=bucket_name, folder_name=folder_name)
        return 204


# api.add_resource(Buckets, '/buckets')
# api.add_resource(Bucket, '/buckets/<bucket_name>')
# api.add_resource(File, '/buckets/<bucket_name>/<path:source>')
# api.add_resource(Folder, '/buckets/<bucket_name>/<path:folder_name>')
# api.add_resource(Folder, '/buckets/<path:bucket_name>')

if __name__ == "__main__":
    app.run()
