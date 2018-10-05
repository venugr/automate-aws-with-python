import boto3
import click

session = boto3.Session ( profile_name='default' )
s3 = session.resource ( 's3' ) 


@click.group()
def cli():
   "Webotron deploys websites to AWS"

@cli.command( 'list-buckets' ) 
def list_buckets():
   "List all S3 Buckets"
   for b in s3.buckets.all():
      print ( b )

@cli.command ( 'list-bucket-objects' )
@click.argument ( 'bucket' ) 
def list_bucket_objects ( bucket ):
   "List object in an S3 Bucket"
   for obj in s3.Bucket(bucket).objects.all():
      print ( obj ) 

if __name__ == '__main__':
   cli()
