from django import template

# カスタムフィルターを作成する。
# templateをインポートして、Libraryを取り出す。
register = template.Library()

# カスタムフィルターを作る。ここでは、cutメソッドをつくる。
# argにある文字をvalueから消して返す。
@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """

    return value.replace(arg, '')

# registerに対して、フィルターをセットする。
# 通常はデコレータで処理をする。(のでコメントアウト。)
# register.filter('cut', cut)
