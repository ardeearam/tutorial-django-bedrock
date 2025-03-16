```
  #Prepare Amazon Bedrock Knowledge Bases

  #Create a helper task that gets a URL, and removes HTML tags

  mkdir tutorial-django-bedrock
  cd tutorial-django-bedrock
  python3 -m venv venv
  source venv/bin/activate

  pip install django
  pip freeze > requirements.txt

  django-admin startproject app
  cd app
  python manage.py runserver


  # app/lib/html_to_text.py
  #cd app
  #mkdir -p management/commands
  #Create management/commands/html_to_text.py


```