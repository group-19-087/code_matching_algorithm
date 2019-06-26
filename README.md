### Building the docker image
`docker build --tag=codematcher:latest .`

### Run the image as a container and bind the current working directory as a volume 
`docker run --rm -it -v "${PWD}:/usr/src/app" codematcher:latest bash`

### Run the application inside the container
`python main.py --codefile <path_to_code> --video <path_to_video>`
