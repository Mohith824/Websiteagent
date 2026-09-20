import unittest
from backend.knowledge import load_college_facts, get_facts_summary


class KnowledgeLoaderTestCase(unittest.TestCase):
    def test_load_college_facts_contains_required_sections(self):
        """Verify facts.md loads and contains accurate codes and sections."""
        facts = load_college_facts(reload=True)
        self.assertIsInstance(facts, str)
        self.assertGreater(len(facts), 100)

        # Verify essential codes
        self.assertIn("E144", facts, "KCET code E144 must be present")
        self.assertIn("E138", facts, "COMEDK code E138 must be present")

        # Verify contact information
        self.assertIn("7026436197", facts, "Admissions contact phone must be present")
        self.assertIn("admission@sitmng.ac.in", facts, "Admissions email must be present")

        # Verify NOT AVAILABLE boundaries
        self.assertIn("NOT AVAILABLE", facts, "NOT AVAILABLE section must be present")
        for restricted_topic in ["Fee", "Cutoff", "Seat", "Scholarship", "Hostel", "Deadline"]:
            self.assertIn(
                restricted_topic.lower(),
                facts.lower(),
                f"Restricted topic '{restricted_topic}' must be documented in facts.md",
            )

    def test_nonexistent_file_raises_error(self):
        """Verify that loading a non-existent file raises FileNotFoundError."""
        with self.assertRaises(FileNotFoundError):
            load_college_facts("data/non_existent_file.md")

    def test_facts_summary(self):
        """Verify that get_facts_summary returns expected diagnostic flags."""
        summary = get_facts_summary()
        self.assertTrue(summary["has_kcet_code"])
        self.assertTrue(summary["has_comedk_code"])
        self.assertTrue(summary["has_not_available_section"])
        self.assertGreater(summary["character_count"], 0)


if __name__ == "__main__":
    unittest.main()
