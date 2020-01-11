from flask import Flask, request, jsonify
import json
import boto3
import datetime


app = Flask(__name__)


html_doc = """
<h1> Add user info to S3 </h1>

<h2>Path</h2>
<bold>/zappa/pinfo</bold>

<h2>Method</h2>
<bold>POST</bold>

<h2>Parameters</h2>
Input json should have one of first_name, middle_name, last_name or zip_code

<h2> Success Response </h2>
<bold> 200: Returns the input json data </bold>

<h2> Error Response </h2>
<bold> 400: None of the expected json fields are present. </bold>

<h1>Usage</h1>

<h2>Run the following command</h2>
Note: Replace with appropriate hostname in the following command<br><br>
<code>
curl -w "%{http_code}" --header "Content-Type: application/json" \
--request POST \
--data '{"first_name":"nikhil7","middle_name":"narayan5", "last_name":"kartha5","zip_code":"94569"}' \
https://{hostname}/dev/zappa/pinfo
</code>

<h2>Sample Output</h2>
<code>
{"data":{"first_name":"nikhil7","last_name":"kartha5","middle_name":"narayan5","zip_code":"94569"}}
</code>
"""


@app.route('/')
def index():
    return f"{html_doc}", 200


@app.route('/zappa/pinfo', methods=['GET', 'POST'])
def pinfo():
    data = request.json
    first_name, middle_name, last_name, zip_code = data.get('first_name',''), data.get('middle_name', ''), data.get('last_name', ''), data.get('zip_code', '')
    if first_name or middle_name or last_name or zip_code:
        csv_out = f'first_name,middle_name,last_name,zip_code\n{first_name},{middle_name},{last_name},{zip_code}'
        write_to_s3(csv_out)
        return jsonify({'data': data}), 200
    else:
        error = "Invalid Data. Input json should have one of first_name, middle_name, last_name or zip_code"
        return jsonify({"error": error, "data":data}), 400


def write_to_s3(data):
    bucketname = <<bucketname>>
    fname = str(abs(hash(data)))
    date = datetime.datetime.utcnow()
    year, month, day = date.strftime("%Y"), date.strftime("%m"), date.strftime("%d")
    folder = f'year={year}/month={month}/day={day}'
    path = f'pinfodata/{folder}/{fname}.txt'

    s3 = boto3.resource('s3')
    s3.Object(bucketname, path).put(Body=data)


if __name__ == '__main__':
    app.run()
