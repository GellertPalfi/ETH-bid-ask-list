Lists okex and binance bid and ask prices for Etherum using Django and python requests modul.  
  
Steps to run project:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Clone repo  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Go to project folder  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. Create a virtual enviroment(in this case the name is "venv")  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;with the "virtualenv venv" command  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4. Activate the enviroment:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source venv/Scripts/activate  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5. Install all required packages:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pip install -r requirements.txt  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6. Initalieze db migrations:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python manage.py makemigrations  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7. Execute db migrations:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python manage.py migrate  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8. Collect static files:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python manage.py collectstatic  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9. Run server  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python manage.py runserver  
