# Unit Testing

import unittest
from unittest.mock import patch,MagicMock
from utils.validators import (validate_ports,validate_timeout,validate_scan_type)
from utils.constants import (
    MAX_PORT_NUMBER,
    MAX_PORT_RANGE,
    MIN_TIMEOUT_LIMIT,
    MAX_TIMEOUT_LIMIT,
)
from models.scan_type import ScanType
from models.scan_config import ScanConfig
from controller.controller import ScanController
from scanner.tcp_scanner import tcp_scan
from scanner.udp_scanner import udp_scan
from models.port_state import PortState
from models.scan_result import ScanResult

class TestValidatorPorts(unittest.TestCase):
    # Test for validate_ports
    def test1_validInputs(self):
        # Arrange
        min_port, max_port = 1,100
        
        # Act
        result = validate_ports(min_port, max_port)
        
        # Assert
        self.assertTrue(result.valid)

    def test2_singleport_boundary(self):
        # Arrange
        min_port, max_port = 80,80
        
        # Act
        result = validate_ports(min_port, max_port)
        
        # Assert
        self.assertTrue(result.valid)

    def test3_min_greater_than_max_invalid(self):
        # Arrange
        min_port, max_port = 100,1

        # Act
        result = validate_ports(min_port, max_port)

        # Assert
        self.assertFalse(result.valid)
        
    def test4_min_below_zero_invalid(self):
        # Arrange
        min_port, max_port = 0,100

        # Act
        result = validate_ports(min_port, max_port)

        # Assert
        self.assertFalse(result.valid)

    def test5_max_port_range_boundary(self):
        # Arrange
        min_port, max_port = 1,MAX_PORT_RANGE

        # Act
        result = validate_ports(min_port, max_port)

        # Assert
        self.assertTrue(result.valid)

    def test6_max_port_boundary(self):
        # Arrange
        min_port, max_port = 1,MAX_PORT_NUMBER
        
        # Act
        result = validate_ports(min_port, max_port)
        
        # Assert
        self.assertTrue(result.valid)

    def test7_over_max_boundary(self):
        # Arrange
        min_port, max_port = 1,MAX_PORT_NUMBER+1
        
        # Act
        result = validate_ports(min_port, max_port)
        
        # Assert
        self.assertFalse(result.valid)

    def test8_negative_number_invalid(self):
        # Arrange
        min_port, max_port = -1,100
        
        # Act
        result = validate_ports(min_port, max_port)
        
        # Assert
        self.assertFalse(result.valid)


class TestValidatorTimeout(unittest.TestCase):
    # Test for validate_timeout
    def test1_min_timeout_boundary(self):
        # Arrange
        timeout = MIN_TIMEOUT_LIMIT
        
        # Act
        result = validate_timeout(timeout)
        
        # Assert
        self.assertTrue(result.valid)

    def test2_below_min_invalid(self):
        # Arrange
            timeout = MIN_TIMEOUT_LIMIT - 1

        # Act
            result = validate_timeout(timeout)

        # Assert
            self.assertFalse(result.valid)
    

    def test3_max_timeout_boundary(self):
        # Arrange
            timeout = MAX_TIMEOUT_LIMIT

        # Act
            result = validate_timeout(timeout)

        # Assert
            self.assertTrue(result.valid)
        
    def test4_above_max_invalid(self):
        # Arrange
            timeout = MAX_TIMEOUT_LIMIT + 1

        # Act
            result = validate_timeout(timeout)

        # Assert
            self.assertFalse(result.valid)

    def test5_zero_number_invalid(self):
        # Arrange
            timeout = 0

        # Act
            result = validate_timeout(timeout)

        # Assert
            self.assertFalse(result.valid)

    def test6_negative_number_invalid(self):
        # Arrange
            timeout = -1

        # Act
            result = validate_timeout(timeout)

        # Assert
            self.assertFalse(result.valid)

    def test7_float_number_valid(self):
        # Arrange
            timeout = 1.11

        # Act
            result = validate_timeout(timeout)

        # Assert
            self.assertTrue(result.valid)


class TestScanControler(unittest.TestCase):
    # Tests for the Scan Controller
    def setUp(self):
        self.controller = ScanController()

    # 1:  TCP function called
    @patch("controller.controller.tcp_scan", return_value=["tcp-result"])
    def test1_run_tcp_scan(self, mock_tcp):
        # Arrange
        config = ScanConfig(
        ip="192.168.100.20",
        ports=[20, 25],
        scan_type=ScanType.TCP,
        timeout=1,)

        # Act
        result = self.controller.run_scan(config)

        # Assert
        self.assertEqual(result, ["tcp-result"])


    # 2: UDP function called
    @patch("controller.controller.udp_scan", return_value=["udp-result"])
    def test2_run_udp_scan(self, mock_udp):
        # Arrange
        config = ScanConfig(
            ip="192.168.100.20",
            ports=[53],
            scan_type=ScanType.UDP,
            timeout=1,
        )

        # Act
        result = self.controller.run_scan(config)

        # Assert
        self.assertEqual(result, ["udp-result"])

    # 3: Valid IP

    @patch("controller.controller.get_target_ip",return_value="192.168.100.20")
    def test3_valid_IP_address(self, mock_ip):
        # Arrange + Act
        result = self.controller.get_scan_ip_address()
        # Assert
        self.assertEqual(result, "192.168.100.20")

    # 4: Invalid IP then Valid

    @patch("controller.controller.get_target_ip",side_effect=["999.999.999.999", "192.168.100.20"])
    def test4_invalid_ip_then_valid(self, mock_ip):
        # Arrange + Act
        with patch("builtins.print"):
            result = self.controller.get_scan_ip_address()
        # Assert
        self.assertEqual(result, "192.168.100.20")

    # 5: Min > Max then Valid

    @patch("controller.controller.get_target_min_port", return_value=10)
    @patch("controller.controller.get_target_max_port",
           side_effect=[1, 20])
    def test5_min_greater_than_max_then_valid(self, mock_max, mock_min):
        # Arrange + Act
        with patch("builtins.print"):
            result = self.controller.get_ports()
        # Assert
        self.assertEqual(result, list(range(10, 21)))

    # 6: Valid ports

    @patch("controller.controller.get_target_min_port", return_value=1)
    @patch("controller.controller.get_target_max_port", return_value=20)
    def test6_valid_ports_(self, mock_max, mock_min):
        # Arrange + Act
        result = self.controller.get_ports()
        # Assert
        self.assertEqual(result, list(range(1, 21)))

    # 7: Timeout = 0

    @patch("controller.controller.get_prompt_timeout",
           side_effect=["0", "1"])
    def test7_zero_timeout_then_valid(self, mock_timeout):
        # Arrange + Act
        with patch("builtins.print"):
            result = self.controller.get_timeout()
        # Assert
        self.assertEqual(result, 1.0)

    # 8: Timeout above max then valid

    @patch("controller.controller.get_prompt_timeout",
           side_effect=["10", "1"])
    def test8_above_max_timeout_then_valid(self, mock_timeout):
        # Arrange + Act
        with patch("builtins.print"):
            result = self.controller.get_timeout()
        # Assert
        self.assertEqual(result, 1.0)

    # 9: Full valid scan

    @patch("controller.controller.get_prompt_timeout", return_value="1")
    @patch("controller.controller.get_prompt_scan_type", return_value="TCP")
    @patch("controller.controller.get_target_max_port", return_value=20)
    @patch("controller.controller.get_target_min_port", return_value=1)
    @patch("controller.controller.get_target_ip",
           return_value="192.168.100.20")
    def test9_full_valid_scan(self, mock_ip, mock_min, mock_max, mock_type, mock_timeout):
        # Arrange + Act
        config = self.controller.get_scan_config()
        # Assert
        self.assertEqual(config.ip, "192.168.100.20")
        self.assertEqual(config.ports, list(range(1, 21)))
        self.assertEqual(config.scan_type, ScanType.TCP)
        self.assertEqual(config.timeout, 1.0)

   