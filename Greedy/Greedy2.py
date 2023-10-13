def greedy(N, times = 0, number = 0):
    if number == N:
        print(times)
    else:
        if number == 0 and N % 2 == 0:
            return greedy(N, times+1, number+1)
        if number == 0 and N % 2 != 0:
            return greedy(N, times, number+1)
        else:
            if number * 2 <= N :

                return greedy(N, times+1, number * 2)
            else:
                return greedy(N, times+1, number+1)

greedy(7)
