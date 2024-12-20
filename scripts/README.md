for database connection string connection
First step: first Insatll PostgreSQl 
Second step: set envirometal variables like
1. C:\Program Files\PostgreSQL\17\bin
2. C:\Users\Admin\AppData\Roaming\pgadmin4
3. C:\Program Files\PostgreSQL\17\pgAdmin 4\python
4. C:\Program Files\PostgreSQL\17\pgAdmin 4\web
5. then Restart your device
Thrid step: Open or track cmmand prowershell on a folder that your sql databse file exist 
then first set password using the command 
1. set PGPASSWORD =My password
then dump or retore table and its data using the below command
2. psql -U postgres -d telecome_db -f ./telecom.sql

Fourth step: connecting the database to python script, for this I use psycopg2 library. to use this first install using a 
pip install psycopg2 -- if psycopg2 package can have issues with dependencies on Windows use 
pip install psycopg2-binary
or use
pip install sqlalchemy 
then install the below package for .env or for connection string file loading
pip install python-dotenv
