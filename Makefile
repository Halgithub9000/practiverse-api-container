install:
	# sudo sin password
	echo "vscode ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/nopasswd

	# actualización del contenedor
	sudo apt update
	sudo apt -y upgrade

	# librerías para documentación
	sudo apt -y install nodejs npm pandoc chromium texlive-xetex graphviz libgraphviz-dev
	sudo npm install -g @marp-team/marp-core @marp-team/marp-cli

	# librerías para dev
	sudo apt -y install postgresql postgresql-contrib postgresql-client
	sudo pip install --upgrade pip
	pip install -r requirements/base.txt -r requirements/dev.txt

	# postgresql
	echo "INITIALIZING DATABASES..."
	sudo service postgresql start

	sudo -u postgres psql -c "DROP DATABASE IF EXISTS \"$$BACKEND_DB_NAME\";"
	sudo -u postgres psql -c "DROP USER IF EXISTS \"$$BACKEND_DB_USER\";"
	sudo -u postgres psql -c "CREATE DATABASE \"$$BACKEND_DB_NAME\";"
	sudo -u postgres psql -c "CREATE USER \"$$BACKEND_DB_USER\" WITH PASSWORD '$$BACKEND_DB_PASSWORD';"
	sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE \"$$BACKEND_DB_NAME\" TO \"$$BACKEND_DB_USER\";"
	sudo -u postgres psql -c "ALTER USER \"$$BACKEND_DB_USER\" CREATEDB;"
	sudo -u postgres psql -c "ALTER USER \"$$BACKEND_DB_USER\" WITH SUPERUSER;"
