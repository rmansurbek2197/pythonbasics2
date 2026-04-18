def juft_toq_sonlar(N):
    juft_sonlar = []
    toq_sonlar = []
    for i in range(1, N+1):
        if i % 2 == 0:
            juft_sonlar.append(i)
        else:
            toq_sonlar.append(i)
    print("Juft sonlar: ", juft_sonlar)
    print("Toq sonlar: ", toq_sonlar)

N = int(input("1 dan N gacha sonlarni kiriting: "))
juft_toq_sonlar(N)