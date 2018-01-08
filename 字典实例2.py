people = {
    'XiaoXin': {
        'phone': '18351980702',
        'addr': 'Nanjing'
    },
    'Bob': {
        'phone': '13260908990',
        'addr': 'Beijing'
    }
}

labels = {
    'phone': 'phone number',
    'addr': 'address'
}
name = input('the name you want:')

request = input('phone_number (p) or address(a)?')

key = request
if request == 'p':
    key = 'phone'
if request == 'a':
    key = 'addr'


person = people.get(name, {})
result = person.get(key, 'not available')
label = labels.get(key, request)

print("%s's %s is %s" % (name, label, result))