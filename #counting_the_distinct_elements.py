#counting_the_distinct_elements
import array
a=array.array('i',[1, 2, 2, 3, 4, 4, 4])
print(f'The distinct elements in {a.tolist()} is:{len(set(a))}')#here the set datatype by default delete all the dupicates 