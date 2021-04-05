from django.test import Client


def test_not_found(client: Client):
    resp = client.get('/')
    assert resp.status_code == 200


# def test_status_code_polls(client: Client):
#     resp = client.get('/polls')
#     assert resp.status_code == 200
#
# def test_status_code_admin(client: Client):
#     resp = client.get('/admin')
#     assert resp.status_code == 200
