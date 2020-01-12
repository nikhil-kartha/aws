from flask import Flask, request, jsonify
import json
import boto3
import datetime
import userdoc
from collections import defaultdict


app = Flask(__name__)


@app.route('/')
def index():
    return f"{userdoc.html}", 200


@app.route('/zappa/pinfo', methods=['POST'])
def pinfo():
    data = extract_fields(request.json)
    if valid(data):
        out = format_output(data, data['ftype'])
        write_to_s3(out, data['bucketname'], data['ftype'])
        return jsonify({'data': request.json}), 200
    else:
        error = "Invalid Data. Input json should have one of first_name, middle_name, last_name or zip_code"
        return jsonify({"error": error, "data": request.json}), 400


def extract_fields(data):
    dd = defaultdict(lambda:"")
    dd.update(data)

    if not dd['bucketname']:
        dd['bucketname'] = <<bucketname>>
    
    if dd['ftype'] != 'json':
        dd['ftype'] = 'csv' # default to using csv format
 
    return dd


def valid(data):
    expected_fields = ['first_name', 'middle_name', 'last_name', 'zip_code']
    return any(data[field] for field in expected_fields)


def format_output(data, ftype):
    if ftype == 'json':
        out = data
    else:
        out = f'first_name,middle_name,last_name,zip_code\n{data["first_name"]},{data["middle_name"]},{data["last_name"]},{data["zip_code"]}'

    return out


def write_to_s3(data, bucketname, ftype):
    prefix = 'pinfodata'
    fname = str(abs(hash(data)))
    date = datetime.datetime.utcnow()
    year, month, day = date.strftime("%Y"), date.strftime("%m"), date.strftime("%d")
    folder = f'year={year}/month={month}/day={day}'
    path = f'{prefix}/{folder}/{fname}.{ftype}'

    s3 = boto3.resource('s3')
    s3.Object(bucketname, path).put(Body=data)


if __name__ == '__main__':
    app.run()
