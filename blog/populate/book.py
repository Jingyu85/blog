from populate import base

import datetime
import random

from article.models import Book



def populate():
    print('Populating Book...', end='')
    titles = ['網頁設計','資料結構','資訊管理','統計學','管理學','微積分','經濟學','管理數學','計算機概論','Java']
    authors = ['王小明','張小華','劉小美','張小志','陳小新','王小田','李小龍','江小瑜','林小泉','沈小琳']
    publishers = ['第一出版社','第二出版社','第三出版社','第四出版社','第五出版社','第六出版社','第七出版社','第八出版社','第九出版社','第十出版社']
    Book.objects.all().delete()

    for i in range(len(titles)):
        book = Book()
        book.title = titles[i]
        book.author=authors[i]
        book.publisher=publishers[i]
        book.publication = datetime.datetime.today()
        book.version = 1
        book.price = 680
        book.save()
    print('done')
    
if __name__ == '__main__':
    populate()