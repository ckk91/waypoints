# Solution Stack
# environment
- docker dir
- docker-compse
- multi stage docker file for building and executing
- makefile as entry point and to provide abstraction layer
- surgically copying file 
## Backend
- Python 3, typed
- Pytest
- formatted with black, flake8, isort
- poetry as a dependency
- normally a fan of boring software. wanted to take this opportunity to jump on the async bandwagon
- fastapi, async automagic openapi spec TODO mention docs
- after smoke test w/ locus changed to compiled async uvicorn
- added gunicorn as a robust prod grad eserver w/ uvicorn workers
  - first tested on echo run
  - async all the things, inckuding db
  - result of async conversion: 1000 users and db doesn't complain
  - locust linear load test initial, later wirh random time jitter
- aiofiles to serve static files
- jinja2 for index templatiing
- 
- psycopg2 and sqlalchemy as orm
- parsing and cleanup robust via regex --> comma oiptional
## Frontend
- VueJS, vuex via vue-cli. life'S too short to config webpack
- VueJS bootstrap
- axios
- ???
- natural input: lat ölong as comma separated form, parsed in backend
- frontend is served by backend aplpication in docker container
  - as such its a monolith. two layer app, but can be split up into two independent services. this was a convenience decision


TODO into droplet? --> heroku
- TODO work on queue pool issue
- TODO make async, locust makes it crap out at 500 users / s
