for tc in range(int(input())):

    n,m = map(int,input().split())

    array = list(map(int,input().split()))

    dp = []

    for i in range(n):
        dp.append(array[i*m: i*m+m])
    #다이나믹 프로그래밍 진행
    for j in range(1,m): #열
        for i in range(n): #행
            #왼쪽위에서 오는경우
            if i == 0: left_up=0 #i == 0인경우 위에서 올 수 없어서 처리
            else:left_up = dp[i-1][j-1]
            #왼쪽아래에서 오는경우
            if i == n-1: left_down=0
            else:left_down = dp[i+1][j-1]
            #왼쪽에서 오는경우
            left =dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up,left_down,left)
    result = 0
    for i in range(n):
        result=max(result,dp[i][m-1])
    print(result)