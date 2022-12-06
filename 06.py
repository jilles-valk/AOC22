def index_after_first_n_unique(data: list, n: int):
    buffer = list(data[:n])
    for i in range(n,len(data)):
        c = data[i]
        buffer.append(c)
        if len(buffer) >= n:
            buffer.pop(0)

        if (len(set(buffer)) == len(buffer)):
            return i + 1

f = open("06_input.txt")
data = f.read()

data_start = index_after_first_n_unique(data, 4)
message_start= index_after_first_n_unique(data, 14)

print("06_a: " + str(data_start))
print("06_b: " + str(message_start))