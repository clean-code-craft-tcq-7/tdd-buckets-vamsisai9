import unittest
import tdd_range 
import bitToAmpConverter

class TestGetRanges(unittest.TestCase):
    def test_single_range(self):
        samples = [4, 5]
        expected = [("4-5", 2)]
        self.assertEqual(tdd_range.get_ranges(sorted(samples)), expected)

    def test_multiple_ranges(self):
        samples = [3, 4, 5, 10, 11, 12]
        expected = [("3-5", 3), ("10-12", 3)]
        self.assertEqual(tdd_range.get_ranges(sorted(samples)), expected)

    def test_single_sample(self):
        samples = [3]
        expected = []
        self.assertEqual(tdd_range.get_ranges(sorted(samples)), expected)


class TestCurrentSensor(unittest.TestCase):
    def test_ignore_error_readings(self):
        self.assertIsNone(bitToAmpConverter.convert_to_amps(4095))
        
    def test_convert_to_amps(self):
        self.assertEqual(bitToAmpConverter.convert_to_amps(0), 0)
        self.assertEqual(bitToAmpConverter.convert_to_amps(2047), 5)
        self.assertEqual(bitToAmpConverter.convert_to_amps(4094), 10)
        self.assertEqual(bitToAmpConverter.convert_to_amps(1146), 3)

class TestAnotherTenSensor(unittest.TestCase):
    def test_convert_to_current(self):
        # Test case 1: ADC reading of 0
        a2d_reading = 0
        expected_current = 15
        result = bitToAmpConverter.convert_to_current(a2d_reading)
        assert result == expected_current, f"Expected {expected_current} but got {result}"

        # Test case 2: ADC reading of 1023
        a2d_reading = 1023
        expected_current = 15
        result = bitToAmpConverter.convert_to_current(a2d_reading)
        assert result == expected_current, f"Expected {expected_current} but got {result}"

        # Test case 3: ADC reading of 511
        a2d_reading = 511
        expected_current = 0
        result = bitToAmpConverter.convert_to_current(a2d_reading)
        assert result == expected_current, f"Expected {expected_current} but got {result}"

        # Test case 4: ADC reading of 256
        a2d_reading = 256
        expected_current = 7
        result = bitToAmpConverter.convert_to_current(a2d_reading)
        assert result == expected_current, f"Expected {expected_current} but got {result}"

        # Test case 5: ADC reading of 767
        a2d_reading = 767
        expected_current = 7
        result = bitToAmpConverter.convert_to_current(a2d_reading)
        assert result == expected_current, f"Expected {expected_current} but got {result}"




if __name__ == '__main__':
    unittest.main()
