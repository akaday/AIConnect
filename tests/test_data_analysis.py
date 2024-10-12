# tests/test_data_analysis.py
import unittest
from src.skills.data_analysis import DataAnalysisSkill

class TestDataAnalysisSkill(unittest.TestCase):
    def setUp(self):
        self.skill = DataAnalysisSkill("https://jsonplaceholder.typicode.com/posts")

    def test_analyze(self):
        result = self.skill.analyze()
        self.assertIn("total_items", result)
        self.assertGreater(result["total_items"], 0)
        self.assertIn("sample_item", result)

if __name__ == '__main__':
    unittest.main()
