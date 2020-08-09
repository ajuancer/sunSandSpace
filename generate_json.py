import json

data = {'beach': []}

data['beach'].append({
    'id': 1,
    'coords': (-5.6617, -5.6441,
               43.5452, 43.5399),
    'sectors': {
        {
            'id': '67a2d102-2f86-40d5-8c61-22e66c04e126',
            'coords': (43.542881, -5.659979)
        },
        {
            'id': 'SL002',
            'coords': (43.542694, -5.659651)
        },
        {
            'id': 'SL003',
            'coords': (43.542072, -5.658059)
        },
        {
            'id': 'SL004',
            'coords': (43.541776, -5.657011)
        },
        {
            'id': 'SL005',
            'coords': (43.541364, -5.655278)
        },
        {
            'id': 'SL006',
            'coords': (43.541102, -5.652852)
        },
    },
    'SL007': {'coords': (43.541160, -5.649985)},
    'SL008': {'coords': (43.541134, -5.648144)},
    'SL009': {'coords': (43.541251, -5.646653)},
    'SL010': {'coords': (43.541842, -5.645516)}
})
data['beach'].append({
    'id': 2,
    'coords': 'google.com',
    '67a2d102-2f86-40d5-8c61-22e66c04e126': 'Michigan'
})
data['beach'].append({
    'id': 3,
    'coords': 'apple.com',
    'from': 'Alabama'
})

with open('info.json', 'w') as outfile:
    json.dump(data, outfile)
