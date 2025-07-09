# Alive


## Roadmap
### todo
- validate data and date

### done
- add frontend to make requests
- simple backend with Python/FastAPI
- create discord bot to read checkin_data.json


## installation

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```



## run

### run backend
```sh
cd backend/
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### run frontend
```sh
cd frontend/
npm run dev
```

### run bot
```sh
cd bot/
python bot.py
```
