f = open("data.txt", "r")

is_avail = True

avail_map = {}

successes = 0


for line in f:
    if line == "\n":
        is_avail = False
    else:
        line = line.rstrip("\n")
        if is_avail:
            for avail in line.split(", "):
                avail_map[avail] = 1
        else:
            dp = [0] * (len(line)+1)
            dp[0] = 1
            index = 0
            while index < len(line):
                initial = line[index:]
                for i in range(1, len(initial) + 1):
                    if initial[:i] in avail_map:
                        dp[index + i] = dp[index + i] + dp[index]
                index = index + 1
            successes = successes + dp[len(dp) - 1]
print(successes)
