# To bypass the request for uuid and secret and
# go to previously inserted ones
test_mode = "ON"

if test_mode != "ON":
    uuid = input("Enter UUID: ")
    secret = input("Enter secret: ")
    url_base = input("Enter base url: ")
else:
    url_base = "https://uudemo.remindotoets.nl/api/v1"
    uuid = "615b9c5e-354c-6731-e5e8-babdb36d9f5a"
    secret = "66e11c5cda915d"
