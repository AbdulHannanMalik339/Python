def OnTime(n) :
    iterations = 0
    for i in range(n) :
        iterations += 1
    print ("When n is: ", n, "Iterations: ", iterations)

OnTime(10)
OnTime(20)
OnTime(42)

print ("\n With 'n' iterations, the time complexity is O(n)")