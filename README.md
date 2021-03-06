Zgen beugro feladat.
Lists okex and binance bid and ask prices.

Steps to run project:
	1. Clone repo
	2. Go to project folder
	3. Create a virtual enviroment(in this case the name is "venv")
		with the "virtualenv venv" command
	4. Activate the enviroment:
		source venv/Scripts/activate
	5. Install all required packages:
		pip install -r requirements.txt
	6. Initalieze db migrations:
		python manage.py makemigrations
	7. Execute db migrations:
		python manage.py migrate
	8. Collect static files:
		python manage.py collectstatic
	9. Run server
		python manage.py runserver