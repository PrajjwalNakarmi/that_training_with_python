import pytest
from unittest.mock import patch
from employee_management import add_employees, edit_employees, delete_employee, read_employee_detail, save_employees, employee_file

@pytest.fixture
def reset_employee_file():
    """Fixture to reset the employee data file before each test."""
    save_employees([])

@patch("builtins.input", side_effect=["101", "John Doe", "Developer", "john.doe@example.com", "1234567890"])
def test_add_employees(mock_input, reset_employee_file):
    """Test adding an employee."""
    add_employees()
    employees = employee_file()
    assert len(employees) == 1
    assert employees[0]["employee_id"] == 101
    assert employees[0]["name"] == "John Doe"
    assert employees[0]["designation"] == "Developer"
    assert employees[0]["company_mail"] == "john.doe@example.com"
    assert employees[0]["contact"] == "1234567890"

@patch("builtins.input", side_effect=["101", "Jane Doe", "", "jane.doe@example.com", "9876543210"])
def test_edit_employees(mock_input, reset_employee_file):
    """Test editing an employee."""
    save_employees([{"employee_id": 101, "name": "John Doe", "designation": "Developer", "company_mail": "john.doe@example.com", "contact": "1234567890"}])
    edit_employees()
    employees = employee_file()
    assert len(employees) == 1
    assert employees[0]["name"] == "Jane Doe"
    assert employees[0]["company_mail"] == "jane.doe@example.com"
    assert employees[0]["contact"] == "9876543210"

@patch("builtins.input", side_effect=["3", "101", "yes"])
def test_delete_employee(mock_input, reset_employee_file):
    """Test deleting an employee."""
    save_employees([{"employee_id": 101, "name": "John Doe", "designation": "Developer", "company_mail": "john.doe@example.com", "contact": "1234567890"}])
    delete_employee()
    employees = employee_file()
    assert len(employees) == 0

def test_read_employee_detail(reset_employee_file, capsys):
    """Test reading employee details."""
    save_employees([
        {"employee_id": 101, "name": "John Doe", "designation": "Developer", "company_mail": "john.doe@example.com", "contact": "1234567890"}
    ])
    read_employee_detail()
    captured = capsys.readouterr()
    assert "Employee ID: 101" in captured.out
    assert "Name: John Doe" in captured.out
    assert "Designation: Developer" in captured.out
    assert "Company Email: john.doe@example.com" in captured.out
    assert "Contact: 1234567890" in captured.out