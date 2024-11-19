import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'woman.settings')  # Replace 'your_project_name' with your actual project name
django.setup()

from safety_app.models import Alert

# Delete rows with invalid user_id
Alert.objects.filter(user_id=3).delete()

print("Deleted alerts with user_id=3.")
