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
        return round(float(ip_outs) / 3, 1)

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
    def fip(cls, hr, bb, hbp, so, ip, ibb=0, c=3.12):
        """
        Fielding Independent Pitching(FIP)
        :param hr: home run
        :param bb: base on ball
        :param hbp: hit by pitch
        :param so: strike out
        :param ip: inning pitched
        :param ibb: intentional base on balls(default:0)
        :param c: league constant(default:3.12)
        :return: (float)FIP
        """
        _13hr = float(13.0 * hr)
        _3bb = 3.0 * float(bb + hbp - ibb)
        _2so = 2.0 * float(so)
        return round((_13hr + _3bb - _2so) / float(ip) + c, 2)

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
        return round(float(h) / float(ab), 3)

    @classmethod
    def slg(cls, tb, ab):
        """
        Slugging
        :param tb: total bases
        :param ab: at bat
        :return: (float)slugging
        """
        return round(float(tb) / float(ab), 3)

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
        return round(float(h + bb + hbp) / float(ab + bb + hbp + sf), 3)

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
        return round((float(tb) / float(ab) + float(h + bb + hbp) / float(ab + bb + hbp + sf)), 3)

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
        return round(float(h - hr) / float(ab - so - hr + sf), 3)

    @classmethod
    def rc(cls, tb, h, bb, hbp, cs, gidp, sf, sh, sb, so, ab, ibb):
        """
        Runs Created
        :param tb: total bases
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
        :return: (float) run created
        """
        # (出塁能力A * 進塁能力B) / 出塁機会C
        a = float(h + bb + hbp - cs - gidp)
        b = float(tb) + round(0.24 * float(bb + hbp - ibb), 1) + round(0.62 * float(sb), 1)\
            + round(0.5 * float(sh + sf), 1) - round(0.03 * float(so), 1)
        c = float(ab + bb + hbp + sf + sh)
        a_b = round(a + 2.4 * c) * (b + 3.0 * c)
        _9c = round(9.0 * c, 1)
        _09c = round(0.9 * c, 1)
        rc = round(a_b / _9c - _09c, 1)
        return rc

    @classmethod
    def rc2002(cls, h, bb, hbp, cs, gidp, sf, sh, sb, so, ab, ibb, single, _2b, _3b, hr):
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
        custom_tb = round(1.125 * float(single), 1) + round(1.69 * float(_2b), 1)\
                    + round(3.02 * float(_3b), 1) + round(3.73 * float(hr), 1)
        a = float(h + bb + hbp - cs - gidp)
        b = custom_tb + round(0.29 * float(bb + hbp - ibb), 1)\
            + round(0.492 * float(sf + sh + sb), 1) - round(0.04 * float(so), 1)
        c = float(ab + bb + hbp + sf + sh)
        a_b = round(a + 2.4 * c, 1) * (b + 3.0 * c)
        _9c = round(9.0 * c, 1)
        _09c = round(0.9 * c, 1)
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
        return round(((float(hr) + float(bb) + float(so)) / pa) * 100, 1)

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
        return round(((float(hr) + float(bb) + float(hbp) + float(so)) / float(bfp)) * 100, 1)