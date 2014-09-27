# -*- coding: utf-8 -*-

u"""
マルコフ連鎖を用いて適当な文章を自動生成するファイル
"""

import os.path
import sqlite3

from PrepareChain import PrepareChain


class GenerateText(object):
    u"""
    文章生成用クラス
    """

    def __init__(self, n=5):
        u"""
        初期化メソッド
        @param n いくつの文章を生成するか
        """
        self.n = n

    def generate(self):
        u"""
        実際に生成する
        """
        # DBが存在しないときは例外をあげる
        if not os.path.exists(PrepareChain.DB_PATH):
            raise IOError(u"DBファイルが存在しません")

        # DBオープン
        con = sqlite3.connect(PrepareChain.DB_PATH)

        # 最終的にできる文章
        generated_text = u""

        # 指定の数だけ作成する
        for i in xrange(self.n):
            text = self._generate_sentence(con)
            generated_text += text

        # DBクローズ
        con.close()

        return generated_text

    def _generate_sentence(self, con):
        u"""
        ランダムに一文を生成する
        """
        return u"適当な文章。"


if __name__ == '__main__':
    generator = GenerateText()
    print generator.generate()



