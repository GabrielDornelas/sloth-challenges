from datetime import timedelta
import unittest

def damage(damage: float, speed: int = 1, time: str = 'minute') -> float | str:
    """
    Calculate damage with given speed in given time.
    
    Args:
        damage (float): The amount of damage that is given by hit (must be positive).
        speed (int): The number of hits per second (must be positive).
        time (str): The amount of time while damage is applied ('second', 'minute', or 'hour').
        
    Returns:
        float | str: The total damage would be dealt or an error message if the input is invalid.
    """
    clock = {
        'second': timedelta(seconds=1).total_seconds(),
        'minute': timedelta(minutes=1).total_seconds(),
        'hour': timedelta(hours=1).total_seconds()
    }
    if time not in clock:
        return f"Invalid time unit: '{time}'. Must be one of {list(clock.keys())}."
    if damage <= 0:
        return "Damage must be a positive number."
    if speed <= 0:
        return "Speed must be a positive number."
    return damage * speed * clock[time]


class TestDamageFunction(unittest.TestCase):
    def test_valid_inputs(self):
        self.assertEqual(damage(40, 5, "second"), 200)
        self.assertEqual(damage(100, 1, "minute"), 6000)
        self.assertEqual(damage(2, 100, "hour"), 720000)
    
    def test_invalid_damage(self):
        self.assertEqual(damage(-10, 1, "minute"), "Damage must be a positive number.")
    
    def test_invalid_speed(self):
        self.assertEqual(damage(10, 0, "minute"), "Speed must be a positive number.")
    
    def test_invalid_time(self):
        self.assertEqual(damage(10, 1, "day"), "Invalid time unit: 'day'. Must be one of ['second', 'minute', 'hour'].")

if __name__ == '__main__':
    unittest.main()
