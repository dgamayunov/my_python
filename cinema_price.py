film=input('Введите фильм:')
date=input('Дата сеанса:')
time=int(input('Время:'))
quant=int(input('Количество билетов:'))
if film=='Пятница':
    if date=='сегодня':
        if time==12:
            if quant>=20:
                print('Цена бронирования:', quant*250*0.8)
            elif quant<20:
                print('Цена бронирования:', quant*250)
        if time==16:
            if quant>=20:
                print('Цена бронирования:', quant*350*0.8)
            elif quant<20:
                print('Цена бронирования:',quant*350)
        if time==20:
            if quant>=20:
                print('Цена бронирования:', quant*450*0.8)
            elif quant<20:
                print('Цена бронирования:',quant*450)
    if date=='завтра':
        if time==12:
            if quant>=20:
                print('Цена бронирования:', quant*250*0.8*0.95)
            elif quant<20:
                print('Цена бронирования:', quant*250*0.95)
        if time==16:
            if quant>=20:
                print('Цена бронирования:', quant*350*0.8*0.95)
            elif quant<20:
                print('Цена бронирования:',quant*350*0.95)
        if time==20:
            if quant>=20:
                print('Цена бронирования:', quant*450*0.8*0.95)
            elif quant<20:
                print('Цена бронирования:',quant*450*0.95)
if film=='Чемпионы':
    if date=='сегодня':
        if time==10:
            if quant>=20:
                print('Цена бронирования:', quant*250*0.8)
            elif quant<20:
                print('Цена бронирования:', quant*250)
        if time==13:
            if quant>=20:
                print('Цена бронирования:', quant*350*0.8)
            elif quant<20:
                print('Цена бронирования:',quant*350)
        if time==16:
            if quant>=20:
                print('Цена бронирования:', quant*350*0.8)
            elif quant<20:
                print('Цена бронирования:',quant*350)
    if date=='завтра':
        if time==10:
            if quant>=20:
                print('Цена бронирования:', quant*250*0.8*0.95)
            elif quant<20:
                print('Цена бронирования:', quant*250*0.95)
        if time==13:
            if quant>=20:
                print('Цена бронирования:', quant*350*0.8*0.95)
            elif quant<20:
                print('Цена бронирования:',quant*350*0.95)
        if time==16:
            if quant>=20:
                print('Цена бронирования:', quant*350*0.8*0.95)
            elif quant<20:
                print('Цена бронирования:',quant*350*0.95)
if film=='Пернатая банда':
    if date=='сегодня':
        if time==10:
            if quant>=20:
                print('Цена бронирования:', quant*350*0.8)
            elif quant<20:
                print('Цена бронирования:', quant*350)
        if time==14:
            if quant>=20:
                print('Цена бронирования:', quant*450*0.8)
            elif quant<20:
                print('Цена бронирования:',quant*450)
        if time==18:
            if quant>=20:
                print('Цена бронирования:', quant*450*0.8)
            elif quant<20:
                print('Цена бронирования:',quant*450)
    if date=='завтра':
        if time==10:
            if quant>=20:
                print('Цена бронирования:', quant*350*0.8*0.95)
            elif quant<20:
                print('Цена бронирования:', quant*350*0.95)
        if time==14:
            if quant>=20:
                print('Цена бронирования:', quant*450*0.8*0.95)
            elif quant<20:
                print('Цена бронирования:',quant*450*0.95)
        if time==18:
            if quant>=20:
                print('Цена бронирования:', quant*450*0.8*0.95)
            elif quant<20:
                print('Цена бронирования:',quant*450*0.95)