from django.contrib.auth import get_user_model
import os

User = get_user_model()

username = "tahashaikh13"
email = "tahashaikh20082006@gmail.com"
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "taha20082006")

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superuser '{username}' created.")
else:
    print(f"Superuser '{username}' already exists.")