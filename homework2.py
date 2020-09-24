publish_year = [2008,1991,1925]
books = ['The Great Gatsby','Empire of the Ants','Custom Paradise']
def bubble_sort(publish_year):
	last_item = len(publish_year) - 1

	for i in range(0,last_item):
		for j in range(0,last_item - i):
			if publish_year[j] > publish_year[j + 1]:
				publish_year[j], publish_year[j + 1] = publish_year[j + 1],publish_year[j]
	
	return publish_year
				
print('Old data', publish_year)
sorted_data = bubble_sort(publish_year).copy()
print('New data:', sorted_data)
for i in range(len(publish_year)):
	print(books[i],str(sorted_data[i]))
