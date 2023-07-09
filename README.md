# Lab Class 33 --- Authentication & Production Server
<!-- this is the link for docker image contaier http://localhost:8000/api/v1/things   -->

## project name:  Auth & Production Server

## Author: Amer Al-omari

## setup

```bash
pip install -r requirements.txt
```

## How to run the app ?

```bash
python manage.py runserver
```

## How to run the test ?

```bash
python manage.py test
```

## how to Create Docker image ?

```bash
docker-compose up  # if the link from the compose did not  run, use this link: http://localhost:8000/api/v1/things
```

## Routes

### Token genration

- Method: POST
- Endpoint: /api/token/
- Required token: No

### Token refresh

- Method: POST
- Endpoint: /api/token/refresh/
- Required token: Yes (refresh token)

### CRUD Routes

---

- Method: GET
- Endpoint: /api/v1/things/
- Required token: Yes

---

- Method: POST
- Endpoint: /api/v1/things/
- Required token: Yes

---

- Method: GET
- Endpoint: /api/v1/things/`<id>`/
- Required token: Yes

---

- Method: PUT
- Endpoint: /api/v1/things/`<id>`/
- Required token: Yes

---

- Method: DELETE
- Endpoint: /api/v1/things/`<id>`/
- Required token: Yes
