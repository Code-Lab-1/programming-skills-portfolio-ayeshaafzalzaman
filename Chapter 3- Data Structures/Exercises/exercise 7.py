places=['himalaya','paris','sharjah','kashmir','antarctica']
print('raw list:',places)
print('alphabetic order:', sorted(places))
print('original list:', places)
print('reverse order:',sorted(places,reverse=True))
places.reverse()
print('reverse list:', places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)