# 1. 飲料與點心名稱、價格分開存
d_name = ["珍奶", "紅茶", "冬瓜茶"]
d_price = [60, 30, 25]
s_name = ["雞排", "地瓜球", "烤玉米"]
s_price = [80, 40, 50]
ans = []
for i in range(len(d_name)):
    for j in range(len(s_name)):
        total = d_price[i] + s_price[j]
        if total <= 100:
            ans.append(f"{d_name[i]}+{s_name[j]}")
print(ans)

