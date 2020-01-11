curl -w "%{http_code}" --header "Content-Type: application/json" \
  --request POST \
  --data '{"first_name":"nikhil7","middle_name":"narayan5", "last_name":"kartha5","zip_code":"94569"}' \
https://{hostname}/dev/zappa/pinfo
