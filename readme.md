##Flask

flask --app server run --host=0.0.0.0 --debug  --cert=adhoc

waitress-serve --host 0.0.0.0 server:app