"""Tests for the clickshots package."""

import os
import pytest
from unittest.mock import patch, MagicMock
from clickshots.listeners import ScreenshotListener
from clickshots.utils import setup_screenshot_method, validate_directory


@pytest.fixture
def mock_environment():
    """Set up test environment."""
    with patch('platform.system', return_value='Linux'), \
         patch('PIL.ImageGrab') as mock_imagegrab:  # Mock PIL instead of subprocess
        mock_imagegrab.grab.return_value = MagicMock()  # Mock screenshot capture
        yield


def test_screenshot_listener_init():
    """Test ScreenshotListener initialization."""
    listener = ScreenshotListener()
    assert listener.mouse_screenshot_enabled is False
    assert listener.keyboard_screenshot_enabled is False
    assert listener.mouse_round_counter == 0
    assert listener.keyboard_round_counter == 0


def test_should_capture():
    """Test screenshot capture timing logic."""
    listener = ScreenshotListener()
    
    # Test mouse events when disabled
    assert not listener.should_capture("tap")
    assert not listener.should_capture("right_tap")
    
    # Test keyboard events when disabled
    assert not listener.should_capture("word_complete")
    
    # Enable mouse screenshots
    listener.mouse_screenshot_enabled = True
    assert listener.should_capture("tap")
    
    # Test delay between captures
    assert not listener.should_capture("tap")  # Should be blocked by delay


def test_screenshot_method_setup(mock_environment):
    """Test platform-specific screenshot method setup."""
    method, command = setup_screenshot_method()
    assert method == "pillow"  # Changed from "command_line" to "pillow"
    assert command is None     # Changed from "gnome-screenshot" to None


def test_validate_directory(tmp_path):
    """Test directory validation."""
    test_dir = tmp_path / "test_screenshots"
    assert validate_directory(str(test_dir)) is True
    assert os.path.exists(test_dir)


def test_capture_screenshot(mock_environment, tmp_path):
    """Test screenshot capture functionality."""
    from clickshots.utils import capture_screenshot
    
    test_dir = str(tmp_path / "screenshots")
    result = capture_screenshot(
        event_type="test",
        round_number=1,
        device_type="mouse",
        save_dir=test_dir
    )
    
    assert result is True
    assert os.path.exists(test_dir)