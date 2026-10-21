import unittest
from app import classify_intent, lead_score, retrieve, DEFAULT_KNOWLEDGE

class InquiryAssistantTests(unittest.TestCase):
    def test_service_intent(self):
        self.assertEqual(classify_intent("We want to build an AI automation service"), "Service inquiry")

    def test_pricing_intent(self):
        self.assertEqual(classify_intent("Can you share the pricing and cost?"), "Pricing / commercial inquiry")

    def test_score_is_bounded(self):
        score, priority, reasons = lead_score(
            "Our company needs to implement an AI project urgently next week with a budget and proposal"
        )
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 100)
        self.assertIn(priority, ["Low", "Medium", "High"])
        self.assertTrue(reasons)

    def test_retrieval_returns_documents(self):
        results = retrieve("What AI automation services does Cynbit offer?", DEFAULT_KNOWLEDGE)
        self.assertTrue(results)
        self.assertEqual(results[0][1]["title"], "AI automation and autonomous agents")

if __name__ == "__main__":
    unittest.main()
