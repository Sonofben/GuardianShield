# tests/windows/test_system_monitor.py
import pytest
from src.windows.core.system_monitor import SystemMonitor

def test_system_monitor_init():
    monitor = SystemMonitor()
    assert monitor is not None

def test_get_system_info():
    monitor = SystemMonitor()
    info = monitor.get_system_info()
    assert isinstance(info, dict)
    assert "cpu_usage" in info
    assert "memory_usage" in info
    assert "disk_usage" in info

def test_get_running_processes():
    monitor = SystemMonitor()
    processes = monitor.get_running_processes()
    assert isinstance(processes, list)
    if processes:  # If there are processes
        assert isinstance(processes[0], dict)
        assert "pid" in processes[0]

# tests/windows/test_network_monitor.py
import pytest
from src.windows.core.network_monitor import NetworkMonitor

def test_network_monitor_init():
    monitor = NetworkMonitor()
    assert monitor is not None

def test_get_network_connections():
    monitor = NetworkMonitor()
    connections = monitor.get_network_connections()
    assert isinstance(connections, list)

# tests/conftest.py
import pytest
import os
import sys

# Add source directory to Python path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)

# Add any pytest fixtures here
@pytest.fixture
def test_file_path():
    """Provide a test file path."""
    return os.path.join(os.path.dirname(__file__), 'test_files', 'test_file.txt')