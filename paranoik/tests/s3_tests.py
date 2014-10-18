import unittest
import mock

from paranoik.storage.s3 import S3


class S3Tests(unittest.TestCase):
    @mock.patch('paranoik.storage.s3.Key')
    @mock.patch('paranoik.storage.s3.S3Connection')
    def test_s3_valid_bucket(self, s):
        s3 = S3('access_key', 'private_key')
        s3.bucket = 'bucket_name'
        s3.add_file('/path/to/some/file')

    @mock.patch('paranoik.storage.s3.Key')
    @mock.patch('paranoik.storage.s3.S3Connection')
    def test_s3_valid_bucket(self, s3_connection, key):
        s3 = S3('access_key', 'private_key')
        self.assertRaises(ValueError, lambda: s3.add_file('/path/to/file'))


if __name__ == "__main__":
    unittest.main()