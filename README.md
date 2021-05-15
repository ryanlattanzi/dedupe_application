# data-eng

## Instructions

0. Clone this repo with Clone this repo (`git clone https://github.com/ryanlattanzi/dedupe_service {local/save/path}`).
0. Open terminal and `cd` into this directory.
0. Ensure Docker is running.
0. Create the Docker image by running `make docker-image` in terminal.
0. Configure `/config/config.yml`. Available services are `get_new_rows` and `dedupe_single_df`. Put only the names of the files in `/input_data` and `/outputs` since the application already knows what directories to look in.
0. Run `make run-app config='config.yml'`. This will print out some statements in the console, and you should see the output file pop up in `/outputs`.

## Explanation of Files and Directories

- `Makefile`: Contains two commands: making the docker image, and running the app in the docker image. Comments in this file are examples of how to execute each command. A config file must be passed to the run-app command.
- `Dockerfile`: Contains information needed to build the docker image.
- `requirements.txt`: Package dependencies to add to the Docker container.
- `/bin`: Two shell scripts that are executed by the Makefile commands.
- `/config`: Includes a YAML config file that defines the service, input files, and output file name for the app.
- `/input_data`: Place to store the input data to be referenced by `config.yml` and accessed by the application.
- `/outputs`: Where the app will spit its output file.
- `/src`: Source code
	- `main.py`: Process the config information, runs the appropriate service, and saves the output.
	- `objects.py`: Includes the Deduplicator object which abstracts the application logic away from `main.py`.
	- `error_handler.py`: Basic error handling class that catches a couple common errors.