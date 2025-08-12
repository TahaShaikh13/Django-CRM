# create_superuser_view.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CRM.settings')  # Change CRM to your project name
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = "tahashaikh13"
email = "tahashaikh20082006@gmail.com"
password = "taha20082006"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superuser created successfully!")
else:
    print("Superuser already exists.")