import fileinput


lines = list(fileinput.input())
results = []
for line in lines:
    results.append(line)

def get_marker(signal, n):
    for i in range(n-1, len(signal)):
        markers = set() 
        for j in range(i-n+1,i+1):
            markers.add(signal[j])
        if len(markers) == n:
            print(markers, i+1)
            return


# Part 1
signal = results[0]
get_marker(signal, 4)

# Part 2
signal = results[0]
get_marker(signal, 14)
