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


## Troubleshooting

### React/Vite won't start on Raspberry Pi
**Symptoms:**
- `npm run dev` fails with an error like:  
  `TypeError: crypto.hash is not a function`
- Or you get `Unsupported engine` warnings

**Cause:**
Node 18 (commonly used on Raspberry Pi 3) does not support `crypto.hash()`, which is used in **Vite 7** and **Tailwind CSS 4.x**. Vite 7 requires Node 20.19+ or even 22+.

**Solution:**
1. Remove existing installs:
   ```bash
   rm -rf node_modules package-lock.json
   ```
2. Install a compatible Vite version:
   ```bash
   npm install vite@4.4.9
   ```
3. Update your `package.json` to:
   ```json
   "vite": "^4.4.9"
   ```
4. Reinstall:
   ```bash
   npm install
   npm run dev
   ```

**Alternative:**
If the dev server is too heavy for the Pi:
```bash
npm run build
npx serve -s dist
```

---

### `npm` doesn't run or shows no output

**Symptoms:**
- Typing `npm` or `npm --version` gives no output

**Cause:**
Node.js is either missing, broken, or installed incorrectly. `npm` relies on a working `node` binary.

**Solution:**
Install Node.js 18 LTS using NodeSource:
```bash
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs
```
Then test:
```bash
node -v
npm -v
```



## License
This project is open source and available under the MIT License.
It’s free to use, modify and share — but comes with no warranty.
