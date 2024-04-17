import unittest
import io
import sys

from mod5.task4 import Redirect


class TestRedirect(unittest.TestCase):
    def test_redirect_both_streams(self):
        stdout_buffer = io.StringIO()
        stderr_buffer = io.StringIO()

        with Redirect(stdout=stdout_buffer, stderr=stderr_buffer):
            print('Hello stdout')
            print('Hello stderr', file=sys.stderr)

        self.assertEqual(stdout_buffer.getvalue().strip(), 'Hello stdout')
        self.assertEqual(stderr_buffer.getvalue().strip(), 'Hello stderr')

    def test_redirect_stdout_only(self):
        stdout_buffer = io.StringIO()

        with Redirect(stdout=stdout_buffer):
            print('Hello stdout')

        self.assertEqual(stdout_buffer.getvalue().strip(), 'Hello stdout')

    def test_redirect_stderr_only(self):
        stderr_buffer = io.StringIO()

        with Redirect(stderr=stderr_buffer):
            print('Hello stderr', file=sys.stderr)

        self.assertEqual(stderr_buffer.getvalue().strip(), 'Hello stderr')

if __name__ == '__main__':
    unittest.main()
