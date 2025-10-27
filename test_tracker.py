import pytest
import tempfile
import os
from project import Tracker

@pytest.fixture
def temp_file():
    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='') as tmpfile:
        tmpfile.write('type,amount,date\n')
        tmpfile.close()
        yield tmpfile.name
        if os.path.exists(tmpfile.name):
            os.remove(tmpfile.name)

def test_add_transaction(temp_file):
    tracker = Tracker(temp_file)
    tracker.add_transaction("income", 100, "2024-01-01")
    with open(temp_file, "r") as file:
        lines = file.readlines()
        assert len(lines) == 2
        assert "income" in lines[1]
        assert "100" in lines[1]
        assert "2024-01-01" in lines[1]

def test_calculate_savings(temp_file):
    tracker = Tracker(temp_file)
    tracker.add_transaction("income", 100, "2024-01-01")
    tracker.add_transaction("expense", 50, "2024-01-02")
    result = tracker.calculate_savings("2024-01-01", "2024-01-02")
    assert "You saved $50.0" in result

def test_generate_summary(temp_file):
    tracker = Tracker(temp_file)
    tracker.add_transaction("income", 100, "2024-01-01")
    tracker.add_transaction("expense", 50, "2024-01-02")
    result = tracker.generate_summary()
    assert result is True

def test_clear_data(temp_file):
    tracker = Tracker(temp_file)
    tracker.add_transaction("income", 100, "2024-01-01")
    tracker.clear_data()
    with open(temp_file, "r") as file:
        lines = file.readlines()
        assert len(lines) == 0