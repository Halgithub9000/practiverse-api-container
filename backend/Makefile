run:
	cd .. && uvicorn backend.main:app --reload

precommit:
	isort . --settings-path pyproject.toml
	black . --config pyproject.toml
	flake8 . --config pyproject.toml

# bandit:
# 	bandit -r .

# rate:
# 	pylint *

# deadcode:
# 	vulture . --min-confidence 100

update:
	pip install --upgrade pip
	pur -r ../requirements/base.txt
	pip install -r ../requirements/base.txt -r ../requirements/dev.txt

# docs:
# 	mkdir -p ../docs/images
# 	python manage.py graph_models --pygraphviz  auth --exclude-models BaseModel,AbstractBaseUser,PermissionsMixin,AbstractUser,Permission,Group -g -o ../docs/images/auth.png
# 	python manage.py graph_models --pygraphviz polls -g -o ../docs/images/polls.png
