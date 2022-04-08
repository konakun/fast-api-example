from fastapi.testclient import TestClient

from app import app


client = TestClient(app)

saved_employee_pk = 0
test_json = {
             'name': 'Johnny',
             'last_name': 'Boi',
             'age': 32,
             'salary': 123.45
            }

def test_get_all_employees():
    response = client.get('/employees')
    assert response.status_code == 200

def test_read_bad_employee():
    response = client.get('/employees/99')
    assert response.status_code == 404
    assert response.json() == {'detail': 'No se encontro al empleado.'}

def test_post_employee():
    response = client.post('/employees', json=test_json)
    assert response.status_code == 201
    saved_employee_pk = response.json()['pk_employee']
    test_json['pk_employee'] = saved_employee_pk
    assert response.json() == test_json

def test_bad_post_employee():
    response = client.post('/employees', json=test_json)
    assert response.status_code == 400
    assert response.json() == {'detail': 'No se pudo crear el empleado.'}

def test_get_employee():
    response = client.get('/employees/' + saved_employee_pk)
    assert response.status_code == 200

def test_del_employee_good():
    response = client.delete('/employees/' + str(saved_employee_pk))
    assert response.status_code == 202
    assert response.json() == {'detail': 'Se elimino correctamente al empleado.'}

def test_del_employee_bad():
    response = client.delete('/employees/99999')
    assert response.status_code == 400
    assert response.json() == {'detail': 'No se pudo eliminar al empleado.'}
