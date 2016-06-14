target = open('dictionary.txt', 'w')

rangeMin = 12000000
rangeMax = 40000000

while rangeMin <= rangeMax:
	
	for prefix in ['014', '015', '016']:
		target.write(prefix + str(rangeMin))
		target.write("\n")
		
	rangeMin += 1


target.close()