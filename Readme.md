## Подготовка SQL бд
```
  docker run -d --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres
  docker exec some-postgres psql -U postgres -c "CREATE DATABASE ecommerce_db"
  docker cp ./sql/setup.sql some-postgres:/home/setup.sql
  docker exec some-postgres psql -U postgres -d ecommerce_db -f /home/setup.sql
```

## Инсталяция сервиса 
```
  pip install pipenv
  pipenv install
```

## Запуск сервиса 
```
  uvicorn app.main:app
```


## REST API Методы

### GET /items/   

Получить список всех элементов
```
curl http://localhost:8000/api/v1/items/
```

### GET /items/name

Фильтр по имени
```   
curl -X 'GET' \
  'http://localhost:8000/api/v1/items/name?substr=on&desc=false' \
  -H 'accept: application/json'
```

### GET /items/price

Фильтр по цене   
```
curl -X 'GET' \
  'http://localhost:8000/api/v1/items/price?from_=200&to=400&desc=false' \
  -H 'accept: application/json'
```
  
### GET /items/{id}  

Получить список элементов с указанным id
```
curl http://localhost:8000/api/v1/items/2
curl http://localhost:8000/api/v1/items/3
```


### PUT /items/{id}  

Изменить элемент с указанным id
```
curl -X 'PUT' \
  'http://localhost:8000/api/v1/items/2' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "UpdatedName",
  "description": "New description",
  "price": 999
}'
```


### POST /order/

Добавить в корзину
```
curl -X 'POST' \
  'http://localhost:8000/api/v1/order/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "item_id": 4,
  "amount": 2,
  "price": 0
}'
```


### PUT /order/
Изменить количество штук продукта
```
curl -X 'PUT' \
  'http://localhost:8000/api/v1/order/1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "item_id": 1,
  "amount": 3,
  "price": 0
}'
```