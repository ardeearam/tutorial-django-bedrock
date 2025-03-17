```
  # Prepare Amazon Bedrock Knowledge Bases

  # Create a helper task that gets a URL, and removes HTML tags
  # tutorial-django-bedrock/
  python lib/url_to_text.py https://lawphil.net/statutes/repacts/ra1949/ra_386_1949.html > knowledge_base/ra386.txt

  # Upload ra386.txt to S3
  # Tweak the LLM prompt
  # Test Bedrock Knowledge Base in Console to see if it is sane

  # Summary of the RAG system - what we have so far

  # Create the python code that will connect to Amazon Bedrock

  mkdir tutorial-django-bedrock
  cd tutorial-django-bedrock
  python3 -m venv venv
  source venv/bin/activate

  pip install django
  pip freeze > requirements.txt

  django-admin startproject app
  cd app
  python manage.py runserver

  # Add a minimal frontend

  # create views.py
  # app/app/urls.py - add route to home
  # app/app/settings.py - add apps to INSTALLED_APPS 
  # app/app/templates/app/index.html





```