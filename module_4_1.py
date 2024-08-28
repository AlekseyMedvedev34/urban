import fake_math as fa
import true_math as tr

print(fa)
print(tr)

fake_divide = fa.divide
true_divide = tr.divide

result1 = fa.divide(69, 3)
result2 = fa.divide(3, 0)
result3 = tr.divide(49, 7)
result4 = tr.divide(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)