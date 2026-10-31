import pytest
from students.models import Course

@pytest.mark.django_db
def test_get_courses(client, course_factory):

    courses = course_factory(_quantity=10)

    response = client.get('http://127.0.0.1:8000/api/v1/courses/')

    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i,c in enumerate(data):
        assert c['name'] == courses[i].name

@pytest.mark.django_db
def test_retrieve_course(client, course_factory):

    courses = course_factory(_quantity=10)
    c_id = courses[0].id

    response = client.get(f'http://127.0.0.1:8000/api/v1/courses/{c_id}/')

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert courses[0].id == data['id']

@pytest.mark.django_db
def test_id_filter_course(client, course_factory):

    courses = course_factory(_quantity=10)
    c_id = courses[8].id

    response = client.get(f'http://127.0.0.1:8000/api/v1/courses/?id={c_id}')

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert courses[8].id == data[0]['id']

@pytest.mark.django_db
def test_name_filter_course(client, course_factory):

    courses = course_factory(_quantity=10)
    c_name = courses[8].name

    response = client.get(f'http://127.0.0.1:8000/api/v1/courses/?name={c_name}')

    assert response.status_code == 200
    data = response.json()
    assert courses[8].id == data[0]['id']
    assert courses[8].name == data[0]['name']

@pytest.mark.django_db
def test_create_course(client):

    count = Course.objects.count()

    response = client.post('http://127.0.0.1:8000/api/v1/courses/', data={'name':"Литература"})

    assert response.status_code == 201
    assert Course.objects.count() == count + 1

@pytest.mark.django_db
def test_patch_course(client):

    Course.objects.create(id=200, name='FFF')

    response = client.patch('http://127.0.0.1:8000/api/v1/courses/200/', data={'name':"Информатика"})

    assert response.status_code == 200
    response2 = client.get('http://127.0.0.1:8000/api/v1/courses/200/')
    data = response2.json()
    assert data['name'] == "Информатика"

@pytest.mark.django_db
def test_delete_course(client):

    Course.objects.create(id=400, name='FFF')
    count = Course.objects.count()

    response = client.delete('http://127.0.0.1:8000/api/v1/courses/400/')

    assert response.status_code == 204
    assert Course.objects.count() == count - 1

@pytest.mark.django_db
def test_max_students(client, settings):

    assert settings.MAX_STUDENTS_PER_COURSE











