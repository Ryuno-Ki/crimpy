import unittest

import pytest

from crimpy.repositories import TwitterRepository


class TwitterRepositoryTestCase(unittest.TestCase):
    @pytest.mark.skip('Needs a DB setup')
    def test_init(self):
        twitter_repository = TwitterRepository()
        assert len(twitter_repository.rows) == 0