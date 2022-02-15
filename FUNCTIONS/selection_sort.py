def index_of_min(l, start_index):
	l_diff = len(l) - len(l[start_index: ])
	min_int = l[start_index]
	for i in range(start_index, len(l)):
		if l[i] < min_int:
			min_int = l[i]
	l = l[start_index:]
	return l.index(min_int) + l_diff







def selection_sort(l):
	x = 0
	while x < len(l):
		y = index_of_min(l, x)
		l[x], l[y] = l[y], l[x]
		x += 1
	return l





