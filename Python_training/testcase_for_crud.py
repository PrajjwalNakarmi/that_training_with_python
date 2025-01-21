import pytest
from unittest.mock import patch, mock_open
from crud import (
    add_employees,
    edit_employees,
    delete_employee,
    read_employee_detail,
    save_employees,
    employee_file
)

# Mock employee data
mock_employee_data = [
    {"employee_id": 1, "name": "John Smith", "designation": "Developer", "company_mail": "john@example.com", "contact": "1234567890"},
    {"employee_id": 2, "name": "Jane Doe", "designation": "Tester", "company_mail": "jane@example.com", "contact": "9876543210"}
]

# Mock the JSON file handling
def mock_employee_file():
    return mock_employee_data

@patch("crud.employee_file", side_effect=mock_employee_file)
@patch("crud.save_employees")
@patch("builtins.input", side_effect=["3", "Alice Johnson", "Engineer", "alice@example.com", "9999999999"])
def test_add_employee(mock_input,mock_save, mock_file):
    add_employees()

    # Check if the new employee was added
    assert len(mock_employee_data) == 3
    new_employee = mock_employee_data[-1]
    assert new_employee["name"] == "Alice Johnson"
    assert new_employee["designation"] == "Engineer"
    assert new_employee["company_mail"] == "alice@example.com"
    assert new_employee["contact"] == "9999999999"

    # Verify save_employees was called
    mock_save.assert_called_once_with(mock_employee_data)

@patch("crud.employee_file", side_effect=mock_employee_file)
@patch("crud.save_employees")
@patch("builtins.input", side_effect=["1", "Alice Updated", "Senior Engineer", "alice.updated@example.com", "8888888888"])
def test_edit_employee(mock_input, mock_save, mock_file):
    edit_employees()

    # Check if the employee details were updated
    updated_employee = mock_employee_data[0]
    assert updated_employee["name"] == "Alice Updated"
    assert updated_employee["designation"] == "Senior Engineer"
    assert updated_employee["company_mail"] == "alice.updated@example.com"
    assert updated_employee["contact"] == "8888888888"

    # Verify save_employees was called
    mock_save.assert_called_once_with(mock_employee_data)

@patch("crud.employee_file", side_effect=mock_employee_file)
@patch("crud.save_employees")
@patch("builtins.input", side_effect=["1", "yes"])
def test_delete_employee(mock_input, mock_save, mock_file):
    delete_employee()

    # Check if the employee was deleted
    assert len(mock_employee_data) == 1, f"Expected 1 employee, found {len(mock_employee_data)}"
    assert mock_employee_data[0]["employee_id"] == 2

    # Verify save_employees was called
    mock_save.assert_called_once_with(mock_employee_data)

@patch("crud.employee_file", side_effect=mock_employee_file)
@patch("builtins.print")
def test_read_employee_detail(mock_print, mock_file):
    read_employee_detail()

    # Verify that employee details were printed
    mock_print.assert_any_call("\nEmployee Details:")
    mock_print.assert_any_call("Employee ID: 1")
    mock_print.assert_any_call("  Name: John Smith")
    mock_print.assert_any_call("  Designation: Developer")
    mock_print.assert_any_call("  Company Email: john@example.com")
    mock_print.assert_any_call("  Contact: 1234567890")

@patch("crud.employee_file", side_effect=mock_employee_file)
@patch("builtins.input", side_effect=["3", "John Smith","yes"])
def test_add_employee_duplicate_id(mock_input, mock_file):
    with patch("builtins.print") as mock_print:
        add_employees()

        # Verify that the duplicate ID warning was printed
        mock_print.assert_any_call("Employee ID already exists. Please enter a unique ID.")