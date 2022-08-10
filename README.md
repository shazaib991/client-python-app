# React Flask example

## Installation

Requires python and node.

1. `pip install flask`
2. `pip install flask-cors`
3. `cd client && npm install`

<b> The run.py Python file is configured with the react build path which contains the static webpage (template_folder & static_folder), so test with Production </b>

## Development

1. In the client directory: `npm start`
2. In a separate terminal, in the root directory: `python run.py`
3. Go to [http://localhost:3000/](http://localhost:3000/)

## Production

1. In the client directory: `npm run build`
2. After the build finishes: In the root directory: `python run.py`
3. Go to [http://localhost:5000/](http://localhost:5000/)
