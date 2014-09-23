# -*- coding: utf-8 -*-

u"""
与えられた文書からマルコフ連鎖のためのチェーン（連鎖）を作成して、DBに保存するファイル
"""

class PrepareChain(object):
	u"""
	チェーンを作成してDBに保存するクラス
	"""

	def __init__(self, text):
		u"""
		初期化メソッド
		@param text チェーンを生成するための文章
		"""
		self.text = text


if __name__ == '__main__':
	pass
