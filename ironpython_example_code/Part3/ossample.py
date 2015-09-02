# -*- coding: shift_jis -*-
import sys

sys.path.append("C:\\Python24\\Lib")     # CPythonライブラリのパスを追加する
import os                                # osのインポート
# osモジュールのwalk()関数を使ったフォルダの再帰処理
for dpath, dnames, fnames in os.walk("./"):
        for fname in fnames:             # ファイル名でループ
                if fname.endswith("py"): # 拡張子を判断する
                        print fname      # ファイル名を表示
