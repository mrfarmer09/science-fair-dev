<link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">

# Science Fair project Development

## System reqiurments

Minimum:

- Windows 10/11 or Ubuntu 20.04
- Ryzen 3 1200 or Intel equivalent
- 8 GB of RAM
- GTX/RTX 10 series or Newer or AMD equivanlent
- 250 GB of HDD storage

Recommended:

- Windows 10/11 or Ubuntu 22.04
- Ryzen 5 3600 or Intel equivalent
- 16 GB of RAM
- RTX 2060
- 500 GB of SSD storage

## Installing and Running the image

All you need to do to install
the docker image is,
run the command:

```bash
docker pull mrfarmerofficial/science-fair-dev && docker run -i -t mrfarmerofficial/science-fair-dev:latest
```

and the image should be installed and running!

### Prerequisites

- Windows 10/11 or Ubuntu 20.04
- WSL2 (Windows subsystem for Linux, required only for Windows)
- Docker
- Python 3
- Hardware meets all minimum reqiurements

## Building the image

To build the Docker image,
use the command:

```bash
docker build .
```

To build the Docker image with a tag,
use the command:

```bash
docker build . -t yourname/science-fair-dev
```

Use:

```bash
docker image
```

to check the installed docker images.

Once you're all done with that,
you can use the command:

```bash
docker run -p80:3000 yourname/science-fair-dev
```

This will run the docker image.

## Exporting the files

To export the files from the Docker image,
use the commands:

```bash
container_id=$(docker create "$image")
docker cp "$container_id:$source_path" "$destination_path"
docker rm "$container_id"
```

## Uploading files to GitHub

All you need to do is,
Install GitHub desktop on your Windows or Ubuntu device.

Then clone this repo in github desktop,
set the destination to

```text
\\wsl.localhost\Ubuntu\home\your-uname\project-directory
```

Then you are all set to work on the project!

[GitHub page](https://github.com/mrfarmer09/science-fair-dev/tree/main)
