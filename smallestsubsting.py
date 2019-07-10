totalchar = 256
def maxdistinct(str, n): 
	count = [0] * totalchar
	for i in range(n): 
		count[ord(str[i])] += 1
	max_distinct = 0
	for i in range(totalchar): 
		if (count[i] != 0): 
			max_distinct += 1	
	return max_distinct 
def smallesteSubstr_maxDistictChar(str): 

	n = len(str)	
	max_distinct = maxdistinct(str, n) 
	minl = n	
	for i in range(n): 
		for j in range(n): 
			subs = str[i:j] 
			subs_lenght = len(subs) 
			sub_distinct_char = maxdistinct(subs,subs_lenght)
			if (subs_lenght < minl and max_distinct == sub_distinct_char): 
				minl = subs_lenght 

	return minl 
str =input()
l = smallesteSubstr_maxDistictChar(str); 
print(l) 