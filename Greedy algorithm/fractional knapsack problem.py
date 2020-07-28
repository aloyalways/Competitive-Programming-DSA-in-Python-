def fractional_knapsack(value, weight, capacity):
    index = list(range(len(value)))
    ratio = [v//w for v, w in zip(value, weight)]
    index.sort(key=lambda i: ratio[i], reverse=True)
    
    MaxValue=0
    for i in index:
        if weight[i]<capacity:
            MaxValue+=value[i]
            capacity-=weight[i]
        else:
            MaxValue+=(value[i]//weight[i])*(capacity)
            break
    print(MaxValue)

weight = [10, 40, 20, 30] 
value = [60, 40, 100, 120] 
capacity = 60
fractional_knapsack(value, weight, capacity)