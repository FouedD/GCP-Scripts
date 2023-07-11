from google.cloud import storage

def list_blobs(request):
  client = storage.Client()
  BUCKET_NAME = '<bucket_name>'
  bucket = client.get_bucket(BUCKET_NAME)
  blobs = bucket.list_blobs()
  
  filenames = ""
  for blob in blobs:
    filenames += blob.name
    filenames +="\n"
  
  return f'{filenames}'
