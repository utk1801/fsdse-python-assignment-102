from unittest import TestCase


class TestIs_rotation(TestCase):
    def test_is_rotation(self):
        try:
            from build import is_rotation
        except ImportError:
            self.assertFalse("no function found")

        self.assertEqual(is_rotation('o', 'oo'), False)
        self.assertEqual(is_rotation(None, 'foo'), False)
        self.assertEqual(is_rotation('', 'foo'), False)
        self.assertEqual(is_rotation('', ''), True)
        self.assertEqual(is_rotation('foobarbaz', 'barbazfoo'), True)
