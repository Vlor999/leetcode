#! /usr/bin/env python3
import unittest
from timeBasedKeyValueStore import TimeMap

class TestTimeMap(unittest.TestCase):
    def setUp(self):
        self.timeMap = TimeMap()

    def test_set_and_get(self):
        self.timeMap.set("ctondw", "ztpearaw", 1)
        self.timeMap.set("vrobykydll", "hwliiq", 2)
        self.timeMap.set("gszaw", "ztpearaw", 3)
        self.timeMap.set("ctondw", "gszaw", 4)

        self.assertEqual(self.timeMap.get("ctondw", 1), "ztpearaw")
        self.assertEqual(self.timeMap.get("vrobykydll", 2), "hwliiq")
        self.assertEqual(self.timeMap.get("gszaw", 3), "ztpearaw")
        self.assertEqual(self.timeMap.get("ctondw", 4), "gszaw")
        self.assertEqual(self.timeMap.get("gszaw", 5), "ztpearaw")
        self.assertEqual(self.timeMap.get("ctondw", 5), "gszaw")
        self.assertEqual(self.timeMap.get("nonexistent", 1), "")

if __name__ == "__main__":
    unittest.main()