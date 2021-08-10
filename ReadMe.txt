1. Step into the GeoIpToAddress directory(the project root directory)
execute : docker build -t image_name:v1 .

2. After the build happens succesfully
docker run -dp 5000:5000 image_name:v1

Example to run execute the command in browser:
http://localhost:5000/get-location?ip=145.217.12.168

curl -s -X GET 'localhost:5000/get-location?ip=145.217.12.168'