#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Shinichi Nakagawa'


class Stats(object):

    def __init__(self):
        pass

    @classmethod
    def ip(cls, ip_outs):
        """
        Inning Pitched
        :param ip_outs: inning pitched outs
        :return: (float) ip
        """
        return round(ip_outs / 3, 1)

    @classmethod
    def era(cls, er, ip):
        """
        Earned run average
        :param er: earned run
        :param ip: inning pitched
        :return: (float) era
        """
        return round((9 * er) / ip, 2)

    @classmethod
    def whip(cls, bb, h, ip):
        """
        Walks + Hits / IP
        :param bb: base on ball
        :param h: hits
        :param ip: inning pitched
        :return: (float) whip
        """
        return round((bb + h) / ip, 3)

    @classmethod
    def h9(cls, h, ip):
        """
        Hits / 9
        :param h: hits
        :param ip: inning pitched
        :return: (float) h9
        """
        return round((9 * h) / ip, 1)

    @classmethod
    def so9(cls, so, ip):
        """
        Strike out / 9
        :param so: strike out
        :param ip: inning pitched
        :return: (float) so9
        """
        return round((9 * so) / ip, 1)

    @classmethod
    def bb9(cls, bb, ip):
        """
        BB / 9
        :param bb: base on ball
        :param ip: inning pitched
        :return: (float) b9
        """
        return round((9 * bb) / ip, 1)

    @classmethod
    def hr9(cls, hr, ip):
        """
        HR / 9
        :param hr: home run
        :param ip: inning pitched
        :return: (float) hr9
        """
        return round((9 * hr) / ip, 1)

    @classmethod
    def single(cls, h, hr, _2b, _3b):
        """
        Single hits
        :param h: hits(all)
        :param hr: home run
        :param _2b: double
        :param _3b: triple
        :return: (int)single hits
        """
        return h - (hr + _2b + _3b)

    @classmethod
    def pa(cls, ab, bb, hbp, sf, sh):
        """
        Plate appearance
        :param ab: at bat
        :param bb: base on ball
        :param hbp: hit by pitch
        :param sf: sacrifice fly
        :param sh: sacrifice hit
        :return: (int)Plate appearance
        """
        return ab + bb + hbp + sf + sh

    @classmethod
    def tb(cls, single, hr, _2b, _3b):
        """
        Total bases
        :param single: single hits
        :param hr: home run
        :param _2b: double
        :param _3b: triple
        :return: (int)total bases
        """
        return hr * 4 + _3b * 3 + _2b * 2 + single

    @classmethod
    def avg(cls, h, ab):
        """
        Batting average
        :param h: hits
        :param ab: at bat
        :return: (float)avg
        """
        return round(h / ab, 3)

    @classmethod
    def slg(cls, tb, ab):
        """
        Slugging
        :param tb: total bases
        :param ab: at bat
        :return: (float)slugging
        """
        return round(tb / ab, 3)

    @classmethod
    def obp(cls, h, bb, hbp, ab, sf):
        """
        On base percentage
        :param h: hits
        :param bb: base on ball
        :param hbp: hit by pitch
        :param ab: at bat
        :param sf: sacrifice fly
        :return: (float)obp
        """
        return round((h + bb + hbp) / (ab + bb + hbp + sf), 3)

    @classmethod
    def ops(cls, h, bb, hbp, ab, sf, tb):
        """
        On the base + slugging
        :param h: hits
        :param bb: base on ball
        :param hbp: hit by pitch
        :param ab: at bat
        :param sf: sacrifice fly
        :param tb: total bases
        :return: (float) ops
        """
        # OBPとSLGを計算してから足して四捨五入
        return round(((tb / ab) + (h + bb + hbp) / (ab + bb + hbp + sf)), 3)

    @classmethod
    def babip(cls, h, hr, ab, so, sf):
        """
        Batting average on balls in play(BABIP)
        :param h: hits
        :param hr: home run
        :param ab: at bat
        :param so: strike out
        :param sf: sacrifice fly
        :return: (float) babip
        """
        return round((h - hr) / (ab - so - hr + sf), 3)

    @classmethod
    def rc(cls, h, bb, hbp, cs, gidp, sf, sh, sb, so, ab, ibb, single, _2b, _3b, hr):
        """
        Runs Created of 2002 ver.
        [note]
        http://en.wikipedia.org/wiki/Runs_created#2002_version_of_runs_created
        :param h: hits
        :param bb: base on ball
        :param hbp: hit by pitch
        :param cs: caught stealing
        :param gidp: ground into duble play
        :param tb: total bases
        :param sf: sacrifice fly
        :param sh: sacrifice hit
        :param sb: stolen base
        :param so: strike out
        :param ab: at bat
        :param ibb: intentional base on balls
        :param single: single hits
        :param _2b: double
        :param _3b: triple
        :param hr: home run
        :return: (float) run created
        """
        # (出塁能力A * 進塁能力B) / 出塁機会C
        custom_tb = round(1.125 * single) + round(1.69 * _2b) + round(3.02 * _3b) + round(3.73 * hr)
        a = h + bb + hbp - cs - gidp
        b = custom_tb + round(0.29 * (bb + hbp - ibb)) + round(0.492 * (sf + sh + sb)) - round(0.04 * so)
        c = ab + bb + hbp + sf + sh
        a_b = round(a + 2.4 * c) * (b + 3 * c)
        _9c = 9 * c
        _09c = round(0.9 * c)
        rc = round(a_b / _9c - _09c, 1)
        return rc

    @classmethod
    def rc27(cls, rc, ab, h, sh, sf, cs, gidp):
        """
        Runs created 27
        :param rc: run created
        :param ab: at bat
        :param h: hits
        :param sh: sacrifice hit
        :param sf: sacrifice fly
        :param cs: caught stealing
        :param gidp: ground into duble play
        :return: (float) run created 27
        """
        to = ab - h + sh + sf + cs + gidp
        rc27 = round(27 * rc / to, 1)
        return rc27

    @classmethod
    def adam_dunn_batter(cls, hr, bb, so, pa):
        """
        Adam dunn %(batter)
        :param hr: home run
        :param bb: base on ball
        :param so: strike out
        :param pa: plate appearance
        :return: (float) adam dunn
        """
        return round(((hr + bb + so) / pa) * 100, 1)

    @classmethod
    def adam_dunn_pitcher(cls, hr, bb, hbp, so, bfp):
        """
        Adam dunn %(pitcher)
        :param hr: home run
        :param bb: base on ball
        :param hbp: hit by pitch
        :param so: strike out
        :param bfp: batters faced
        :return: (float) adam dunn
        """
        return round(((hr + bb + hbp + so) / bfp) * 100, 1)