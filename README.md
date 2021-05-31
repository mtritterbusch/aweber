# Widget API

* clone repo
* install virtual environment (requires Python >= 3.6, tested with 3.9.2)
* activate virtual environment
* requirements.txt is in widget_project directory, change into that directory
* ```pip install -r requirements.txt``` to install used libraries and packages
* ```run_dev.sh``` and ```run_prod.sh``` are there for convenience, they set required environment variables
* ```bandit -r .``` to run security analysis
* ```./run_dev.sh migrate``` to apply migrations to db
* ```./run_dev.sh test``` to run tests
* ```./run_dev.sh runserver``` to run api in debug mode (browse to ```http://127.0.0.1:8000/widgets``` to interact with api)


