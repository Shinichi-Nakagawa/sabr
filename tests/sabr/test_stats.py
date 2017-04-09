#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Shinichi Nakagawa'


import unittest
from sabr.stats import Stats


class TestStats(unittest.TestCase):
    """
    Stats Class Tests
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ip(self):
        """
        Inning Pitched test
        :return:
        """
        # Yu Darvish(2013)
        ip = Stats.ip(629)
        self.assertEqual(ip, 209.7)

    def test_era(self):
        """
        Earned run average test
        :return:
        """
        # Yu Darvish(2013)
        era = Stats.era(66, 209.7)
        self.assertEqual(era, 2.83)

    def test_whip(self):
        """
        WHIP test
        :return:
        """
        # Yu Darvish(2013)
        whip = Stats.whip(80, 145, 209.7)
        self.assertEqual(whip, 1.073)

    def test_h9(self):
        """
        Hits / 9 test
        :return:
        """
        # Yu Darvish(2013)
        h9 = Stats.h9(145, 209.7)
        self.assertEqual(h9, 6.2)

    def test_so9(self):
        """
        Strike out / 9 test
        :return:
        """
        # Yu Darvish(2013)
        h9 = Stats.so9(277, 209.7)
        self.assertEqual(h9, 11.9)

    def test_bb9(self):
        """
        Base on ball / 9 test
        :return:
        """
        # Yu Darvish(2013)
        h9 = Stats.bb9(80, 209.7)
        self.assertEqual(h9, 3.4)

    def test_hr9(self):
        """
        Base on ball / 9 test
        :return:
        """
        # Yu Darvish(2013)
        hr9 = Stats.hr9(26, 209.7)
        self.assertEqual(hr9, 1.1)

    def test_avg(self):
        """
        Batting average test
        :return:
        """
        # Barry bonds(2004)
        avg = Stats.avg(135, 373)
        self.assertEqual(avg, 0.362)

    def test_slg(self):
        """
        Batting average test
        :return:
        """
        # Barry bonds(2004)
        tb = 45 * 4 + 3 * 3 + 27 * 2 + 60
        slg = Stats.slg(tb, 373)
        self.assertEqual(slg, 0.812)

    def test_obp(self):
        """
        On base percentage test
        :return:
        """
        # Barry bonds(2004)
        obp = Stats.obp(135, 232, 9, 373, 3)
        self.assertEqual(obp, 0.609)

    def test_ops(self):
        """
        On the base + slugging test
        :return:
        """
        # Barry bonds(2004)
        tb = 45 * 4 + 3 * 3 + 27 * 2 + 60
        ops = Stats.ops(135, 232, 9, 373, 3, tb)
        self.assertEqual(ops, 1.422)

    def test_single(self):
        """
        single test
        :return:
        """
        # ichiro suzuki(2004)
        single = Stats.single(262, 8, 24, 5)
        self.assertEqual(single, 225)

    def test_tb(self):
        """
        Total bases test
        :return:
        """
        # ichiro suzuki(2004)
        single = Stats.single(262, 8, 24, 5)
        tb = Stats.tb(single, 8, 24, 5)
        self.assertEqual(tb, 320)

    def test_rc(self):
        """
        Run created 2002 test
        :return:
        """
        # ichiro suzuki(2004)
        rc = Stats.rc(320, 262, 49, 4, 11, 6, 3, 2, 36, 63, 704, 19)
        self.assertEqual(rc, 131.6)

    def test_rc27(self):
        """
        Run created 27 test
        :return:
        """
        # ichiro suzuki(2004)
        rc = Stats.rc(320, 262, 49, 4, 11, 6, 3, 2, 36, 63, 704, 19)
        rc27 = Stats.rc27(rc, 704, 262, 2, 3, 11, 6)
        self.assertEqual(rc27, 7.7)

    def test_rc2002(self):
        """
        Run created 2002 test
        :return:
        """
        # ichiro suzuki(2004)
        single = Stats.single(262, 8, 24, 5)
        rc = Stats.rc2002(262, 49, 4, 11, 6, 3, 2, 36, 63, 704, 19, single, 24, 5, 8)
        self.assertEqual(rc, 136.5)

    def test_rc27_rc2002(self):
        """
        Run created 27 test
        :return:
        """
        # ichiro suzuki(2004)
        single = Stats.single(262, 8, 24, 5)
        rc = Stats.rc2002(262, 49, 4, 11, 6, 3, 2, 36, 63, 704, 19, single, 24, 5, 8)
        rc27 = Stats.rc27(rc, 704, 262, 2, 3, 11, 6)
        self.assertEqual(rc27, 7.9)

    def test_babip(self):
        """
        BABIP test
        :return:
        """
        # ichiro suzuki(2004)
        babip = Stats.babip(262, 8, 704, 63, 3)
        self.assertEqual(babip, 0.399)

    def test_adam_dunn_b(self):
        """
        adam dunn test(batter)
        :return:
        """
        # adam dunn 2012
        dunn = Stats.adam_dunn_batter(41, 105, 222, 649)
        self.assertEqual(dunn, 56.7)

    def test_adam_dunn_p(self):
        """
        adam dunn test(pitcher)
        :return:
        """
        # hisashi iwakuma 2013
        dunn = Stats.adam_dunn_pitcher(25, 42, 2, 185, 866)
        self.assertEqual(dunn, 29.3)

    def test_pa(self):
        """
        plate appearance test
        :return:
        """
        self.assertEqual(Stats.pa(704, 49, 4, 2, 3), 762)


if __name__ == '__main__':
    unittest.main()
