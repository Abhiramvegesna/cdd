import boto3

s3_client = boto3.client('s3')

# Define source and destination bucket names
SOURCE_BUCKET = "your-source-bucket-name"
DESTINATION_BUCKET = "your-destination-bucket-name"

def lambda_handler(event, context):
    try:
        # Automatically retrieve the uploaded file's key from the event trigger
        object_key = event['Records'][0]['s3']['object']['key']

        # Copy object from source bucket to destination bucket
        s3_client.copy_object(
            CopySource={'Bucket': SOURCE_BUCKET, 'Key': object_key},
            Bucket=DESTINATION_BUCKET,
            Key=object_key
        )

        print(f"File '{object_key}' copied from {SOURCE_BUCKET} to {DESTINATION_BUCKET}")

        return {
            'statusCode': 200,
            'body': f"File '{object_key}' successfully copied to {DESTINATION_BUCKET}"
        }
    
    except Exception as e:
        print(f"Error copying file: {str(e)}")
        return {
            'statusCode': 500,
            'body': f"Error copying file: {str(e)}"
        }