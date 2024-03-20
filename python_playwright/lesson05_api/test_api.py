from typing import Generator
import pytest
from playwright.sync_api import Playwright, Page, APIRequestContext, expect

@pytest.fixture(scope="module")
def myIds():
    keys = []
    yield keys


@pytest.fixture(scope='session')
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url="http://localhost:3000/"
    )
    yield request_context
    request_context.dispose()


def test_post_todo(api_request_context: APIRequestContext, myIds) -> None:
    data = {
        "completed": False,
        "title": "do next tutorial tomorrow!",
    }
    new_todo = api_request_context.post(f"/todos", data=data)
    assert new_todo.ok
    
    todos_response = new_todo.json()
    print("")
    print(f"todo Var: {new_todo}")
    print(f"todo_resonse Var: {todos_response}")

    myIds.append(todos_response['id'])



def test_get_todo(api_request_context: APIRequestContext, myIds) -> None:
    get_todo = api_request_context.get(f"/todos/{myIds[-1]}")
    assert get_todo.ok

    get_response = get_todo.json()
    print("")
    print(f"get Var: {get_todo}")
    print(f"get_resonse Var: {get_response}")

    assert get_response['title'] == "do next tutorial tomorrow!"
    assert get_response['completed'] == False


def test_update_todo(api_request_context: APIRequestContext, myIds) -> None:
    payload = {
        "completed": True
    }
    update_todo = api_request_context.patch(f"/todos/{myIds[-1]}", data=payload)
    assert update_todo.ok

    update_response = update_todo.json()
    print("")
    print(f"update Var: {update_todo}")
    print(f"update_resonse Var: {update_response}")

    assert update_response['title'] == "do next tutorial tomorrow!"
    assert update_response['completed'] == True


def test_delete_todo(api_request_context: APIRequestContext, myIds) -> None:
    delete_todo = api_request_context.delete(f"/todos/{myIds[-1]}")
    assert delete_todo.ok

    delete_response = delete_todo.json()
    print("")
    print(f"delete Var: {delete_todo}")
    print(f"delete_resonse Var: {delete_response}")