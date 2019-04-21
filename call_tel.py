city=int(input('Введите код города:'))
length=int(input('Введите длительность разговора в минутах:'))
if city==343:
    print('Екатеринбург', length*15, 'руб')
elif city==381:
    print('Омск', length*18, 'руб')
elif city==473:
    print('Воронеж', length*13, 'руб')
elif city==485:
    print('Ярославль', length*11, 'руб')