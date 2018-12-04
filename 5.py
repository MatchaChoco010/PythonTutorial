# %% [markdown]
# # 5. データ構造
# %% [markdown]
# ## 5.1. リスト型についてもう少し
# %% [markdown]
# リスト型のメソッドをいくつか。
#
# - `list.append(x)`: リストの末尾に要素を追加する
# - `list.extend(iterable)`: リストにイテラブルのすべての要素を追加する
# - `list.insert(i, x)`: 指定した位置に要素を挿入する
# - `list.remove(x)`: 値xをもつ最初の要素を削除。なければエラー
# - `list.pop([i])`: 指定された位置の要素を削除、あるいは末尾の要素を削除
# - `list.clear()`: リストのすべての要素を削除
# - `list.index(x, [start, [end]])`: 値xを持つ最初の要素の添字を返す
# - `list.count(x)`: リストのxの出現回数を返す
# - `list.sort(key=None, reverse=False)`: リストをインプレース演算でソート
# - `list.reverse()`: リストをインプレース演算で逆順にする
# - `list.copy()`: シャローコピーを返す。`a[:]`と等価

# %%
from math import pi
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')


# %%
fruits.index('banana')


# %%
fruits.count('tangerine')


# %%
fruits.index('banana', 4)


# %%
fruits.reverse()
fruits


# %%
fruits.append('grape')
fruits


# %%
fruits.sort()
fruits


# %%
fruits.pop()

# %% [markdown]
# リストを操作するメソッドは書き換えるメソッドで、これらは`None`を返すように設計されている。
# %% [markdown]
# numpyの配列を使ったりするだろうから、素のリストはあまり使わないんじゃないかな。
# そんなことはないかな。データを加工するのとかはリストを使うのかな。
# %% [markdown]
# ### 5.1.1. リストをスタックとして使う
# リストは`pop`メソッドを使ってスタックとして使える。
# %% [markdown]
# ### 5.1.2. リストをキュートして使う
# リストをキューに使うより`collections.deque`を使うと良い。
# %% [markdown]
# ### 5.1.3. リストの内包表記
# イテラブルに操作を行ったりフィルタリングしたりと言ったことの便利な表記。

# %%
squares = []
for x in range(10):
    squares.append(x ** 2)

squares


# %%
squares = list(map(lambda x: x**2, range(10)))
squares


# %%
squares = [x ** 2 for x in range(10)]
squares

# %% [markdown]
# 内包表記はカッコの中に式、`for`句、そして0個以上の`for`句、`if`句で構成される。

# %%
[(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

# %% [markdown]
# 以下に内包表記の例。

# %%
vec = [-4, -2, 0, 2, 4]
[x*2 for x in vec]


# %%
[x for x in vec if x >= 0]


# %%
[abs(x) for x in vec]


# %%
freshfruit = ['banana', 'loganberry', 'passion fruit ']
[weapon.strip() for weapon in freshfruit]


# %%
# [x, x**2 for x in range(6)]
[(x, x**2) for x in range(6)]


# %%
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[num for elem in vec for num in elem]


# %%
[str(round(pi, i)) for i in range(1, 6)]

# %% [markdown]
# 式の部分にメソッド呼び出しや複雑な関数などを書ける。
# %% [markdown]
# ### 5.1.4. ネストしたリストの内包表記
# 式の部分にさらにリストの内包表記を書ける。

# %%
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
[[row[i] for row in matrix] for i in range(4)]

# %% [markdown]
# 実際には組み込み関数を使うほうが良いだろう。
# %% [markdown]
# ## 5.2. `del`文
# %% [markdown]
# リストからの値の削除にはdel文が使える。

# %%
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
a


# %%
del a[2:4]
a


# %%
del a[:]
a

# %% [markdown]
# 変数そのものの削除にも使える。

# %%
del a

# %% [markdown]
# ## 5.3. タプルとシーケンス
# タプルはコンマで区切られた値。

# %%
t = 12345, 54321, 'hello'
t[0]

# %%
t
