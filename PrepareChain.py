# -*- coding: utf-8 -*-

u"""
与えられた文書からマルコフ連鎖のためのチェーン（連鎖）を作成して、DBに保存するファイル
"""

import unittest

from collections import defaultdict


class PrepareChain(object):
	u"""
	チェーンを作成してDBに保存するクラス
	"""

	def __init__(self, text):
		u"""
		初期化メソッド
		@param text チェーンを生成するための文章
		"""
		if isinstance(text, unicode):
			text = text.encode("utf-8")
		self.text = text

	def do_prepare(self):
		u"""
		形態素解析からDB保存まで
		"""
		# 長い文章をセンテンス毎に分割
		sentences = self._divide(self.text)

		# 3つ組の出現回数
		triplet_freqs = defaultdict(int)

		# センテンス毎に3つ組にする
		for sentence in sentences:
			# 形態素解析
			morphemes = self._morphological_analysis(sentence)
			# 3つ組をつくる
			triplets = self._make_triplet(morphemes)
			# 出現回数を加算
			for (triplet, n) in triplets:
				triplet_freqs[triplet] += n

		# DBに保存
		self._save(triplet_freqs)

	def _divide(self, text):
		u"""
		「。」や改行などで区切られた長い文章を一文ずつに分ける
		@param text 分割前の文章
		@return 一文ずつの配列
		"""
		pass

	def _morphological_analysis(self, sentence):
		u"""
		一文を形態素解析する
		@param sentence 一文
		@return 形態素で分割された配列
		"""
		pass

	def _make_triplet(self, morphemes):
		u"""
		形態素解析で分割された配列を、形態素毎に3つ組にしてその出現回数を数える
		@param morphemes 形態素配列
		@return 3つ組とその出現回数の辞書 key: 3つ組（タプル） val: 出現回数
		"""
		pass

	def _save(self, triplet_freqs):
		u"""
		3つ組毎に出現回数をDBに保存
		@param triplet_freqs 3つ組とその出現回数の辞書 key: 3つ組（タプル） val: 出現回数
		"""
		pass


class TestFunctions(unittest.TestCase):
	u"""
	テスト用クラス
	"""
	
	def setUp(self):
		u"""
		テストが実行される前に実行される
		"""
		self.text = "こんにちは。今日は、楽しい運動会です。hello world.我輩は猫である\n名前はまだない。我輩は犬である\r\n名前は決まってるよ"
		self.chain = PrepareChain(self.text)
	
	def test_divide(self):
		u"""
		一文ずつに分割するテスト
		"""
		sentences = self.chain._divide(self.text)
		answer = ["こんにちは。", "今日は、楽しい運動会です。", "hello world.", "我輩は猫である", "名前はまだない。", "我輩は犬である", "名前は決まってるよ"]
		self.assertEqual(sentences.sort(), answer.sort())

	def tearDown(self):
		u"""
		テストが実行された後に実行される
		"""
		pass


if __name__ == '__main__':
	unittest.main()
