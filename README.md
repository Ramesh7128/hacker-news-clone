## Hacker Story.

HackerStory is a redign of hacker news, rendering top trending articles from hacker news api. 

### Getting Started
These instruction will get you a copy of the projct up and running on your local machine for development and guide you with production setup.

### Prerequisites.
Eventhough this setup should work with python 2.x too, you might run into certain dependency issues. This was tested and deployed in the following setup.

* Python3
* ubuntu 18.04
* python3-venv
* nodejs>8
**(for production)**
* nginx
* gunicorn

## Installing.

### Development Setup.

### Django setup.

clone the repository: git clone https://github.com/Ramesh7128/hacker-news-clone.git

#### Creating virtualenvironment and activating it outside your project root directory.

* python3 -m env ./env
* source /env/bin/activate.
cd into the project directory.

#### Install Dependencies from requirements.txt.

(requirements.txt can be found in the project root directory. so make sure you are in projects root directory( directory where manage.py file can be found))

pip install -r requirements.txt

#### Make migrations to generate the db schema.
(In this proj i have made use of the default sqllite3 db, you are free to choose db of your choice. But make sure you install the required packages if you do so.)

python manage.py makemigrations

python manage.py migrate

#### Create a superuser

python manage.py createsuperuser

you can smash enter for all fields except for username and password question.

#### Populate db with top trending posts from hackerNews.

you can run django-admin custom command fetch_articles to load your db with the top posts.

python manage.py fetch_articles
(ideally in production you will put this as a cron updating your db every 3/5 minutes.)

#### Run your localserver and check the RestApi end point/ django's admin panel. 

python manage.py runserver
* Api end point for all stories: localhost:8000/api/stories
* end point for admin panel: localhost:8000/admin
(you would be asked to login.Login with the superuser creds you created earlier.You should be able to see all the top trending stories in Stories table.)

### Frontend.
Make sure you have node and npm isntalled.
Open an other terminal and cd into the frontend directory inside the project root directory.

#### Install dependencies and start the server.
npm install
npm start

open browser and fire localhost:3000 to see your react-app running and consuming the backends api from the django development server.

### Production setup.

In production nginx will be pointing to build folder in frontend directory.
cmd: npm build
In the server frontend directory for getting the build.
and all /api requests will proxy passed to gunicorn sock file.

Gunicorn will be app server running the django as systemctl service so that it makes sure the app is spawned back even if goes down accidently.

There will be a cron job running a bash script, for fetching article every 4 mins and updating the db.

the nginx configuration is as follows
```
upstream app_server {
    server unix:/path/to/your/gunicorn/sock/file fail_timeout=0;
}

server {
        listen 80;
        listen [::]:80;
        location = /favicon.ico { access_log off; log_not_found off; }
        root /path/to/your/build/folder;
        server_name ['domain name /ip'];
        index index.html index.htm index.nginx-debian.html;


        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files $uri /index.html;
        }
        <!-- for the rest api -->
        location /api {
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header Host $http_host;
                proxy_redirect off;
                proxy_pass http://app_server;
        }
        <!-- for the django admin -->
        location /admin {
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header Host $http_host;
                proxy_redirect off;
                proxy_pass http://app_server;
        }
}
```
### Built With

* Django
* React (using create-react-app setup)
* Django Rest Framework for apis.
* react-fuzzy-picker for fuzzy search.

### License
This project is licensed under the MIT License - see the LICENSE.md file for details


