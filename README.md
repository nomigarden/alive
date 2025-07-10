# Alive

**Alive** is a personal “dead man's switch” system designed to protect my cat, Samu, in case I'm unable to check in for an extended time. It consists of a web interface for regular check-ins, a backend API, and a Discord bot that notifies me or a selected contact if I’ve been silent for too long.

---

## Roadmap

### Done
- React + TypeScript frontend with Tailwind CSS
- FastAPI backend to store and retrieve check-ins
- Discord bot to monitor last check-in and send private alerts

### Todo
- Validate incoming data and date formats
- Add settings panel (custom intervals, contacts)
- Dockerize (optional)

---

## Installation

### 1. Clone the repo

```sh
git clone https://github.com/yourname/alive.git
cd alive
```
### 2. Setup python environment

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```


### 3. Setup frontend
```sh
cd frontend/
npm install
```


## Run
### Start backend
```sh
cd backend/
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Start frontend
```sh
cd frontend/
npm run dev
```

### Start bot
```sh
cd bot/
python bot.py
```


## License
This project is open source and available under the MIT License.
It’s free to use, modify and share — but comes with no warranty.
