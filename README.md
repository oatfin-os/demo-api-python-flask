# Oatfin Demo API 

## Testing:
```
docker compose -f test.yml up --build --abort-on-container-exit --exit-code-from web
```

## To run locally:
a. make sure docker and docker-compose are installed

b. run: 

```
docker-compose up --build
```

## To use the app locally: 
a. First create a user:

```
POST http://localhost:5000/v1/users
   {
       "username": "admin",
       "password": "password"
   }
```


b. Login as the user above to get a JWT token:
```
POST http://localhost:5000/v1/login
    {
        "username": "admin",
        "password": "password"
    }
```

c. Make a request:
```
POST http://localhost:5000/v1/tasks 
    -H 'Authorization: Bearer ACCESS_TOKEN_FROM_LOGIN'
```
