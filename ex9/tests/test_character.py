import pytest
from logging import getLogger
from src.character import Character  

def test_character_is_alive():
    """Test if a character with positive HP is considered alive."""
    char = Character("Hero", 10, 5, getLogger())
    assert char.is_alive() is True

def test_character_is_dead():
    """Test if a character with 0 HP is considered dead."""
    char = Character("Villain", 0, 8, getLogger())
    assert char.is_alive() is False

def test_character_dies():
    """Test if a character becomes dead when HP reaches 0."""
    char = Character("Knight", 5, 7, getLogger())
    char.hit_point = 0  # Simulate character losing all health
    assert char.is_alive() is False
