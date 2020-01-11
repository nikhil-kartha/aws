# Description
Setup an API Endpoint to upload json data to an S3 bucket, and query it using AWS Glue.


## Setup
Create a virtualenv and install flask and zappa
```
python3 -mvenv env3
source env3/bin/activate
pip install flask zappa
zappa init
```
*NOTE*: Replace _bucketname_ in the files *app.py* and *pinfo-crawler.yaml*, with the bucketname configured during "zappa init".


## Lambda
### Deploy lambda function
Install Zappa. ref: https://github.com/Miserlou/Zappa
```
zappa deploy dev
```


### Generate data in S3 (Manual)
Replace the URL in the following command with an appropriate one from the API gateway.
```
curl -w "%{http_code}" --header "Content-Type: application/json" \
  --request POST \
  --data '{"first_name":"nikhil7","middle_name":"narayan5", "last_name":"kartha5","zip_code":"94569"}' \
https://{hostname}/dev/zappa/pinfo
```


## AWS Glue (uses cloudformation stack)
```
aws cloudformation create-stack --stack-name pinfo-crawler --template-body file://pinfo-crawler.yaml --capabilities CAPABILITY_IAM
```


## Athena (manual)
Setup query results location, go to settings in "query editor" and add the s3 bucket location to store query results.

At this point you should be able to run sql queries against the created tables.

