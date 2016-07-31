#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_knuth_shuffle
----------------------------------

Tests for `pyalgs.knuth_shuffle` module.
"""

import unittest

from pyalgs.basic import knuth_shuffle as ks


class TestKnuthShuffle(unittest.TestCase):

    def setUp(self):
        self.size = 100
        self.seq = list(range(self.size))

    def test_randomness(self):
        seq2 = ks.shuffle(self.seq[:])
        self.assertNotEqual(self.seq, seq2)

    def test_all_elements_present(self):
        seq2 = ks.shuffle(self.seq[:])
        seq3 = sorted(seq2)
        self.assertEqual(self.seq, seq3)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
