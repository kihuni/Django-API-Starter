import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_register():
    client = APIClient()
    data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpass123'
    }
    response = client.post('/api/users/register/', data)
    assert response.status_code == 201
    assert response.data['username'] == 'testuser'

@pytest.mark.django_db
def test_login():
    client = APIClient()
    user = User.objects.create_user(username='testuser', password='testpass123')
    response = client.post('/api/users/login/', {
        'username': 'testuser',
        'password': 'testpass123'
    })
    assert response.status_code == 200
    assert 'access' in response.data