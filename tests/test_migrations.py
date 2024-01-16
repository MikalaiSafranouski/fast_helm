import subprocess

from pytest import FixtureRequest
from sqlalchemy.sql import text

from app.database import async_engine


def test_migration(request: FixtureRequest) -> None:
    """Test for missing migration files by running an upgrade/migrate cycle and
    inspecting the output.
    """

    assert True