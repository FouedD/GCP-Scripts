from google.cloud import storage

def checkExtension(filename):
    if filename.endswith("js"):
        return 1
    else:
        return 0

def read_content(request):
    client = storage.Client()
    bucket_name = '<bucket_name>'
    bucket = client.get_bucket(bucket_name)
    blobs = bucket.list_blobs()

    all = ""
    for blob in blobs:
      if (checkExtension(blob.name) == 1):
        content = blob.download_as_text()
        msg = blob.name + " :  " + content
        all += "{} \n -------------------------------\n".format(msg)

    return f'{all}'
