# 総当たり戦

team = ['A', 'B', 'C', 'D', 'E']
opps = ['A', 'B', 'C', 'D', 'E']

# for t1 in team:
#     for t2 in team:
#         if t1 != t2:
#             print(t1, 'vs', t2)
        # if t1 == t2:
        #     continue
        # print(t1, 'vs', t2)

for t1 in team:
    opps.remove(t1)
    for t2 in opps:
        print(t1, 'vs', t2)