# python-postgres-tkinter

first create your virtualenv

`$ python3 -m venv venv`

activate venv

`$ source venv/bin/activate`

then install requeriments

`$ pip install -r requirements.txt`

install postgresql, login and open de db.sql file and copy the content in the psql shell

create a .env file in the root folder

`$ touch .env`

and add your postgresql credentials to .env file


>ENV_DB_NAME="students_example"\
ENV_USER="{your db user}"\
ENV_PASSWORD="{your db user password}"\
ENV_HOST="{your host or localhost}"\
ENV_PORT="{your port or 5432}"


finally the project run with: 

`$ python src/student.py`
