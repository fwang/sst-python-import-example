from dir_a.file_a import hello

def multicenter(event, context):
  return {
    "statusCode": 200,
    "body": hello(),
  }
