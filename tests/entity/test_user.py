"""Tests for the User entity."""

import pytest

from src.entity.user import User


def test_create_user_with_valid_values() -> None:
    """Create a user with valid values."""
    # Arrange
    user_id = 1
    username = "alice"
    email = "alice@example.com"

    # Act
    user = User(user_id=user_id, username=username, email=email)

    # Assert
    assert user.user_id == user_id
    assert user.username == username
    assert user.email == email
    assert user.is_active is True


def test_create_user_with_invalid_id_raises_value_error() -> None:
    """Raise ValueError when user_id is invalid."""
    # Arrange
    user_id = 0

    # Act / Assert
    with pytest.raises(ValueError, match="user_id must be a positive integer"):
        User(user_id=user_id, username="alice", email="alice@example.com")


def test_create_user_with_blank_username_raises_value_error() -> None:
    """Raise ValueError when username is blank."""
    # Arrange
    username = "   "

    # Act / Assert
    with pytest.raises(ValueError, match="username must not be empty"):
        User(user_id=1, username=username, email="alice@example.com")


def test_change_email_updates_email() -> None:
    """Update email when a valid new email is provided."""
    # Arrange
    user = User(user_id=1, username="alice", email="alice@example.com")
    new_email = "new-alice@example.com"

    # Act
    user.change_email(new_email)

    # Assert
    assert user.email == new_email


def test_change_email_with_invalid_value_raises_value_error() -> None:
    """Raise ValueError when new email is invalid."""
    # Arrange
    user = User(user_id=1, username="alice", email="alice@example.com")

    # Act / Assert
    with pytest.raises(ValueError, match="email must be a valid email address"):
        user.change_email("invalid-email")


def test_deactivate_and_activate_user() -> None:
    """Change active status with activate and deactivate."""
    # Arrange
    user = User(user_id=1, username="alice", email="alice@example.com")

    # Act
    user.deactivate()
    deactivated_status = user.is_active
    user.activate()
    activated_status = user.is_active

    # Assert
    assert deactivated_status is False
    assert activated_status is True
