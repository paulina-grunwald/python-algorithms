
'''
Create dict combing two tuples.
'''
names = ('Alex','Paulina','Mike','John','Alexandra')
ages = (15,22,33,54,15)
combined_data = dict(zip(names,ages))

combined_data_values = [combined_data[value] for value in combined_data]
combined_data_keys = list(combined_data.keys())
print('Combined names and ages placed into dict: {}'.format(combined_data))
print('Combined data values: {}'.format(combined_data_values))
print'Combined data keys{}:'.format((combined_data_keys))

'''Unpack disct using *iterable'''
unpacked_data = [*combined_data]
print('Unpacked data using *iterable: {}'.format(unpacked_data))
