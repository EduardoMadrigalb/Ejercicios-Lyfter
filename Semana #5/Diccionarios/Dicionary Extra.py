sales = [
	{
		'date': '25/03/25',
		'customer_email': 'auri.jin@gmail.com',
		'items': [
			{
				'name': 'Cat food',
				'upc': 'ITEM-001',
				'unit_price': 15.07,
			},
			{
				'name': 'Tuna',
				'upc': 'ITEM-002',
				'unit_price': 7.92,
			},
			{
				'name': 'Bowl',
				'upc': 'ITEM-003',
				'unit_price': 10.60,
			},
		],
	},
	{
		'date': '26/03/25',
		'customer_email': 'dinosaur@gmail.com',
		'items': [
			{
				'name': 'Cat food',
				'upc': 'ITEM-001',
				'unit_price': 30.40,
			},
			{
				'name': 'Bowl',
				'upc': 'ITEM-003',
				'unit_price': 10.60,
			},
		],
	},
	{
		'date': '27/03/25',
		'customer_email': 'catlover@gmail.com',
		'items': [
			{
				'name': 'Cat food',
				'upc': 'ITEM-001',
				'unit_price': 60.45,
			},
			{
				'name': 'Tuna',
				'upc': 'ITEM-002',
				'unit_price': 14.54,
			}
		],
	},
]

result= {}

for i in sales:
    for item in i ['items']:
        upc = item['upc']
        unit_price = item['unit_price']

        if upc in result:
            result[upc] += unit_price
        else:
            result[upc] = unit_price

print(result)