# raster-boundary
Get raster boundary excluding no-data values

## Build docker image
`docker build -t test .`

## Start the docker container
`docker run -p 5000:5000 test`

## Make a GET request to the server
Use web-browser, Postman or other tools of your choice to access `http://127.0.0.1:5000`

## Visualizing the output
Copy the entire JSON response from the GET request and paste it in [geojson.io](https://geojson.io)

## Sample input image
![](https://github.com/sdhegde/raster-boundary/blob/2570542e6f7ce5ef96cadb71c80f14020694c700/input.png?raw=true)

## Output boundary as visualized on [geojson.io](https://geojson.io)
![](https://github.com/sdhegde/raster-boundary/blob/2570542e6f7ce5ef96cadb71c80f14020694c700/output.png?raw=true)

