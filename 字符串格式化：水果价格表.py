total_width=int(input("please enter width: "))

price_width=10
item_width=total_width-price_width

print('='*total_width)

header_format='%-*s%*s'
content_format='%-*s%*.2f'

print(header_format%(item_width,'Item',price_width,'Price'))

print('-'*total_width)

print(content_format%(item_width,'A',price_width,8.999))

print('-'*total_width)