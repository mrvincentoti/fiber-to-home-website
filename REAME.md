#### FTTH WEBSITE

###### SETUP

1. clone the repo `git clone repo_url`
2. In the same directory as settings.py, create a file called `.env` with this variables

`SECRET_KEY=your_key`
`DATABASE_NAME=your_database_name`
`DATABASE_USER=your_database_user`
`DATABASE_PASSWORD=database_password`
`EMAIL_HOST=email_host`
`EMAIL_HOST_USER=email_host_password`
`EMAIL_HOST_PASSWORD=database_password`

3. install virtualenv(on windows `py -m pip install --upgrade pip` on linux `python3 -m pip install --user --upgrade pip`)
4. create a virtual environment (on linux `python -m virtualenv venv`, on windows `py -m venv venv`)
5. activate the virtual environment on linux `source venv/bin/activate` on windows `venv\Scripts\activate`
6. install dependencies `pip install -r requirements.txt`

###### FREEZE REQUIREMENTS

1. run this command in the same location wehre requirement.txt is `pip freeze > requirements.txt`

###### WEBSITE COLORS

1. #ED1B33 - RED
2. rgb(237, 27, 51) - RED
3. #3954A5 - BLUE
4. rgb(57, 84, 165) - BLUE

#3C54A4 #EC1D35 #F46882 #F45C6C
