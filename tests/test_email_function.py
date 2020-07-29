from unittest import TestCase

from functions.email import is_correct_email


class EmailFunctionTestCase(TestCase):
    def test_returns_True_for_correct_email(self):
        self.assertTrue(is_correct_email("masteraalish@gmail.com"))

    def test_returns_False_if_email_contains_two_at_signs(self):
        self.assertFalse(is_correct_email("mastera@alish@gmail.com"))
        self.assertFalse(is_correct_email("masteraalish@gmail@com"))
        self.assertFalse(is_correct_email("@masteraalish@gmail.com"))

    def test_returns_if_email_does_not_contain_username(self):
        self.assertFalse(is_correct_email("@gmail.com"))

    def test_email_must_contain_at_sign(self):
        self.assertFalse(is_correct_email("aidana.yahoo.com"))
