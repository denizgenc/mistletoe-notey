import unittest
from mistletoe_notey.span_token import tokenize_inner
from mistletoe_notey.latex_token import Math
from mistletoe_notey.latex_renderer import LaTeXRenderer


class TestLaTeXToken(unittest.TestCase):
    def setUp(self):
        self.renderer = LaTeXRenderer()
        self.renderer.__enter__()
        self.addCleanup(self.renderer.__exit__, None, None, None)

    def test_span(self):
        token = next(iter(tokenize_inner('$ 1 + 2 = 3 $')))
        self.assertIsInstance(token, Math)
        self.assertEqual(token.content, '$ 1 + 2 = 3 $')
