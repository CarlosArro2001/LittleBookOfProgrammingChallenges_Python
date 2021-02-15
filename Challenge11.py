#program that will give the students the answer to logic gate questions

print("Enter Logic Gate ")
gate = input()
print("Enter first input : ")
f_input = int(input())
print("Enter second input : ")
s_input = int(input() )
if((gate == "AND" and f_input==0 and s_input == 0)or(gate == "AND" and f_input==0 and s_input == 1)or(gate == "AND" and f_input==1 and s_input == 0)or(gate == "OR" and f_input==0 and s_input == 0)or(gate == "XOR" and f_input == s_input)):
    print(0)
else:
    print(1)

