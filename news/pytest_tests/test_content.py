# from http import HTTPStatus

from django.urls import reverse
import pytest

# from pytest_django.asserts import assertRedirects


def test_create_comment_page_not_contains_form(client, news):
    url = reverse('news:detail', kwargs={'pk': news.pk})
    response = client.get(url)
    assert 'form' not in response.context


def test_create_comment_page_contains_form(author_client, news):
    url = reverse('news:detail', kwargs={'pk': news.pk})
    response = author_client.get(url)
    assert 'form' in response.context


'''@pytest.mark.parametrize('client_type', ('client', 'author_client'))
def test_create_comment_page_contains_form_2(client_type, news):
    url = reverse('news:detail', kwargs={'pk': news.pk})
    if client_type == 'client':
        response = client_type.get(url)
        assert 'form' not in response.context
    else:
        assert 'form' in response.context
'''