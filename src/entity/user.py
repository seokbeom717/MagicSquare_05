"""User entity for the MagicSquare domain."""

from __future__ import annotations

import re


class User:
    """Represent a user in the domain layer.

    This class belongs to the ECB entity layer and contains
    user-related domain data and invariants.
    """

    _EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

    def __init__(
        self,
        user_id: int,
        username: str,
        email: str,
        is_active: bool = True,
    ) -> None:
        """Initialize a User entity.

        Args:
            user_id: Unique positive identifier for the user.
            username: Display name of the user.
            email: Email address of the user.
            is_active: Whether the user is active.

        Raises:
            ValueError: If any input value is invalid.
        """
        self._validate_user_id(user_id)
        self._validate_username(username)
        self._validate_email(email)

        self._user_id = user_id
        self._username = username.strip()
        self._email = email.strip()
        self._is_active = is_active

    @property
    def user_id(self) -> int:
        """Return the user identifier."""
        return self._user_id

    @property
    def username(self) -> str:
        """Return the username."""
        return self._username

    @property
    def email(self) -> str:
        """Return the email address."""
        return self._email

    @property
    def is_active(self) -> bool:
        """Return whether the user is active."""
        return self._is_active

    def change_username(self, new_username: str) -> None:
        """Change username after validation.

        Args:
            new_username: New username value.

        Raises:
            ValueError: If username is empty.
        """
        self._validate_username(new_username)
        self._username = new_username.strip()

    def change_email(self, new_email: str) -> None:
        """Change email after validation.

        Args:
            new_email: New email address value.

        Raises:
            ValueError: If email format is invalid.
        """
        self._validate_email(new_email)
        self._email = new_email.strip()

    def activate(self) -> None:
        """Mark user as active."""
        self._is_active = True

    def deactivate(self) -> None:
        """Mark user as inactive."""
        self._is_active = False

    def to_dict(self) -> dict[str, int | str | bool]:
        """Convert the entity to a serializable dictionary."""
        return {
            "user_id": self._user_id,
            "username": self._username,
            "email": self._email,
            "is_active": self._is_active,
        }

    @staticmethod
    def _validate_user_id(user_id: int) -> None:
        if user_id <= 0:
            raise ValueError("user_id must be a positive integer")

    @classmethod
    def _validate_email(cls, email: str) -> None:
        normalized_email = email.strip()
        if not cls._EMAIL_PATTERN.match(normalized_email):
            raise ValueError("email must be a valid email address")

    @staticmethod
    def _validate_username(username: str) -> None:
        if not username.strip():
            raise ValueError("username must not be empty")
