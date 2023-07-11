from google.cloud import storage

def list_blobs(request):
  client = storage.Client()
  BUCKET_NAME = '<bucket_name>'
  bucket = client.get_bucket(BUCKET_NAME)
  blobs = bucket.list_blobs()
  
  b = ""
  for blob in blobs:
    b += blob.name
    b +="\n"
  
  return f'{b}'
