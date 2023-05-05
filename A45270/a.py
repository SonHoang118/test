# # Viết chương trình in ra 10 số nguyên tố đầu tiên

# def so_nguyen_to(n):
#     for i in range(2,n):
#         if n%i == 0:
#             return False
#     return False
# # so_nguyen_to(int(input()))

# def tong_cac_so(n):
#     s=0
#     while n!=0:
#         s += (n%10)
#         n = n//10
#     return s
# # tong_cac_so(int(input()))

# cnt = 0
# number = 2
# while (cnt<2):
#     if (so_nguyen_to(number)) and (tong_cac_so(number) % 4 == 0):
#         print(number)
#         cnt += 1
#     number += 1







# viet chuong trinh in ra 10 số đối xứng đầu tiên mà tổng các chữ số đó chia hết cho 3
# def so_doi_xung(n):
#     lst = list(str(n))
#     if (lst == lst[::-1]):
#         return True
#     return False

# def tong_cac_so(n):
#     s=0
#     while n!=0:
#         s += (n%10)
#         n = n//10
#     return s

# cnt = 0
# number = 10
# while (cnt < 10):
#     if (so_doi_xung(number)) and (tong_cac_so(number)%3==0):
#         print(number)
#         cnt += 1
#     number += 1


# print(32//10)

# def so_doi_xung(n):
#     so_ban_dau = n
#     so_khi_lat = 0
#     while n:
#         so_khi_lat += n%10*10 + n//10
#         n = n//10
#     return so_khi_lat
# print(so_doi_xung(int(input())))

def dem_so_luong_ki_tu(S):
    lst = list(S)
    while True:
        count = 1
        for i in range (0,len(lst)):
            for j in range (1,len(lst)):
                if lst[i] == lst[j]:
                    count += 1
                    
