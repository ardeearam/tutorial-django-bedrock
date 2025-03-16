```
  #Prepare Amazon Bedrock Knowledge Bases

  #Create a helper task that gets a URL, and removes HTML tags
  #tutorial-django-bedrock/
  python lib/url_to_text.py https://lawphil.net/statutes/repacts/ra1949/ra_386_1949.html > knowledge_base/ra386.txt

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