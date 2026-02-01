# python virtual environment cheatsheet

## 1. create a new virtual environment
`python -m venv env_name`

python -m venv venv

## 2. activate the new python environment (Windows)
`.\env_name\Scripts\activate`

.\venv\Scripts\activate

## or activate (macOS / Linux)
`source env_name/bin/activate`

source venv/bin/activate

## 3. Install packages
`pip install package_name` 

pip install pymongo

## 4. Save installed packages to a file
`pip freeze > requirements.txt`

or 
`pip list --format=freeze > requirements.txt`

# 5. run
`python app.py`

# 6. deactivate
`deactivate`
