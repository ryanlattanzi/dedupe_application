# data-eng

## Instructions

0. Clone this repo with `git clone https://github.com/ryanlattanzi/dedupe_service {local/save/path}`.
0. Open terminal and `cd` into this directory.
0. Ensure Docker is running.
0. Create the Docker image by running `make docker-image` in terminal.
<<<<<<< HEAD
0. If needed, alter the config files located in `/config`. There are two available services, `get_new_rows` and `dedupe_single_df`, and each one is set up with its own config file. Each has the same structure so theoretically only one config is needed, but two are included for ease of use. Put only the names of the files in `input_data:` and `output:` since the application already knows what directories to look in. *NOTE* If you are using `get_new_rows`, then you MUST list `new_data.csv` first due to application logic using left joins.
0. Run `make run-app config='{CONFIG_FILE}.yml'`. This will print out some statements in the console, and you should see the output file pop up in `/outputs`.
=======
0. Configure `/config/config.yml`. Available services are `get_new_rows` and `dedupe_single_df`. Put only the names of the files in `input_data:` and `output:` since the application already knows what directories to look in. **NOTE**: If you are using `get_new_rows`, then you MUST list `new_data.csv` first due to application logic using left joins.
2. Run `make run-app config='config.yml'`. This will print out some statements in the console, and you should see the output file pop up in `/outputs`.
>>>>>>> c0f175293e6e82a15e0b97b9d9734db7a5ab9131

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
