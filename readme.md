## REST API Built on FastAPI and Postgresql

**Command To Run The App**
`uvicorn --port 8000 --host 127.0.0.1 main:app --reload`

*Some Important Points To Remember*
- API design and sample payloads can be accessed via SwaggerUI on http://127.0.0.1:8000/docs
- SQL query for the main table can be found in `db.sql`
- docker-compose is also added to create the table at the startup for using postgres
- db config (no worries!) is added in .env