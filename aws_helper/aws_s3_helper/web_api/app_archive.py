from flask import Flask
from flask_restful import Resource, Api
from aws_helper.aws_s3_helper.v1_args import DownloadFile
from aws_helper.aws_s3_helper.v1_args import CreateNewBucket
from aws_helper.aws_s3_helper.v1_args import UploadToAws
from aws_helper.aws_s3_helper.v1_args import DeleteBucketsFoldersAndFiles

app = Flask(__name__)
api = Api(app)

download_bucket_aws = DownloadFile("new/arparser_training.py",
                                   'rostiklox')

create_bucket_aws = CreateNewBucket("sadsadsadsadsadsadasdsad")

upload_file_aws = UploadToAws(["/home/ross/myscript.py"],
                              "rostiklox")
delete_file_aws = DeleteBucketsFoldersAndFiles("rostiklox")


class FirstBucket(Resource):

    def get(self):
        # input_key = request.get_json(force=True)
        download_bucket_aws.run()
        return 200

    def put(self):
        upload_file_aws.run()
        return 204

    def post(self):
        create_bucket_aws.run()
        return 201

    def delete(self):
        delete_file_aws.run()
        return 204
    # def delete(self):
    #     # DATA -->       {"2": {"name": "Ross",
    #     #                 "Task": "Create dict with data",
    #     #                 "Task Description": "After u create method post u have update it in method put"}}
    #     input_key = request.get_json(force=True)
    #     if input_key == "":
    #         DATA.clear()
    #         return "Delete all data without key"
    #     elif input_key:
    #         DATA.get(input_key).clear()
    #         return "Delete data by key"


api.add_resource(FirstBucket, '/firstbucket')
if __name__ == "__main__":
    app.run()

#
# class Buckets(Resource):
#     def get(self):
#         """:return list buckets"""
#         pass

    # def post(self):
    #     """:return create buckets must create few buckets (list buckets)"""
        # bucket_names = request.get_data()
        # ["asdsad","sadsadsad"]
        # for bucket_name in bucket_names:
            # for щось одне з списку
            # BKT.create(bucket=bucket_name)
            # BKT.create(bucket="asdsad")
        #     bucket.create(bucket=bucket_name)
        #   клас, метод класу, ключ, назва бакету
        # pass
#     def delete(self):
#         """return delete all buckets"""
#         # Взяти список бакетів записати їх в змінну. видалити
#         pass
#
#
# class Bucket(Resource):
#     def get(self, bucket_name: str):
#         """get all info for one bucket"""
#         pass
#
#     def post(self, bucket_name: str):
#         """create one bucket"""
#         pass
#         # BKT.create(bucket=bucket_name)
#
#     def delete(self, bucket_name: str):
#         """delete one bucket by name"""
#         pass
#
#
# class Files:
#     def get(self):
#         """return list of files"""
#         pass
#     # ...
#
#
# class File:
#     def get(self, file_name):
#         """get singel file"""
#         pass  # ...
#
#
# class User:
#     def get(self):
#         pass

# api.add_resource(Buckets, '/buckets')
# api.add_resource(Bucket, '/buckets/<bucket_name>')
# api.add_resource(Files, '/buckets/<bucket_name>/files')
# api.add_resource(File, '/buckets/<bucket_name>/files/<file_name>')
# api.add_resource(Users, '/users')
# api.add_resource(User, '/users/<id>')
