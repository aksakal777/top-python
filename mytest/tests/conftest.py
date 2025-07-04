"""
@pytest.fixture
def db(scope='session'):
    conn = connect('sqlite:///memory')
    return conn

def test_database(db):
    assert db.execute('select 1').fetchone()[0] == 1
    assert is_connected(db) is True
    
@pytest.fixture(scope='session')
def connection():
    engine = create_engine(

    )
    return engine.connect()
"""

"""@pytest.fixture
def email_manager()
    return EmailManager()

@pytest.fixture
def sending_user(email_manager)
    user = email_manager.create_user()
    yield user
    email_manager.delete_user(user)"""

import pytest

@pytest.fixture(scope="session")
def default_messages():
    print("[setup] default_messages")
    return [
        "Hello there!",
        "This is urgent!",
        "   ",
        "Another one.",
        ""
    ]

@pytest.fixture(scope="function")
def clean_messages(default_messages):
    print("[setup] clean_messages")
    return [msg for msg in default_messages if msg.strip()]

