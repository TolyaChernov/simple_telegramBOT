start_mint: #start on linux mint
	python3 -m venv .venv
	.venv/bin/python3 -m pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt




lint: #format
	pip freeze > requirements.txt
	black .
	isort .
	autopep8 ./ --recursive --in-place -a
	autoflake --in-place --remove-all-unused-imports --remove-unused-variables -r ./




#	python -m venv .venv
#	source .venv/Scripts/activate
#	source .venv/bin/activate
#	python -m pip install --upgrade pip
#	pip install -r requirements.txt

#   python3 manage.py collectstatic

	





# djang:
# 	pip install django
# 	django-admin startproject lesson26
# 	cd lesson29
# 	python manage.py startapp signal
# 	python manage.py makemigrations
# 	python manage.py migrate
# 	python manage.py createsuperuser
# 	python3 manage.py runserver
# 	python3 manage.py runserver localhost:8000

# 	python manage.py dumpdata --exclude auth.permission > db.json
# 	python manage.py loaddata --exclude contenttypes> db.json
