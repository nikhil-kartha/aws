html = """
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


