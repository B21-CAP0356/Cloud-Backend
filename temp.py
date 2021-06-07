# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\ASUS\Downloads\lofty-bolt-313607-e8b2d338b62e.json'

storage_client = storage.Client()

"""
Create Bucket
"""
bucket_name = 'just_test_bucket'
bucket = storage_client.bucket(bucket_name)
#bucket.location = 'US'
#bucket = storage_client.create_bucket(bucket)


"""
Accessing a specific Bucket(?)
"""

#my_bucket = storage_client.bucket(bucket_name)

"""
Upload files
"""
def upload_to_bucket(blop_name, file_path, bucket_name):
    #blop_name stands for name file in bucket 
    #file_path stands for file location
    
    #storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blop_name)

    blob.upload_from_filename(file_path)
    return blob
    
file_path = r'C:\Users\ASUS\Downloads' #local path
upload_to_bucket('Test Upload 2', os.path.join(file_path, '30749485.jpg'), 'just_test_bucket')
