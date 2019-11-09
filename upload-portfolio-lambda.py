import boto3
import zipfile

s3= boto3.resource('s3')

portfolio_bucket=s3.Bucket('portfolio.navid.info')
build_bucket=s3.Bucket('portfoliobuild.navid.info')

build_bucket.download_file('buildportfolio.zip', '/tmp/buildportfolio.zip')

with zipfile.ZipFile('/tmp/buildportfolio.zip') as myzip:
    for nm in myzip.namelist():
        print(nm)
        obj= myzip.open(nm)
        portfolio_bucket.upload_fileobj(obj,nm)
        portfolio_bucket.Object(nm).Acl().put(ACL='public-read')
