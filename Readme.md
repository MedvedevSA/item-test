psql -U postgres -c "CREATE DATABASE abc"

docker cp ./setup.sql some-postgres:/home/setup.sql

psql -U postgres -d ecommerce_db -f /home/setup.sql

sudo docker exec some-postgres psql -U postgres -d ecommerce_db -f /home/setup.sql


POST /items/
http://localhost:8000/api/v1/items/

{
  "name": "name",
  "description": "string",
  "price": 7
}
