# Write a method that joins the two lists by matching one girl with one boy into a new list
# If someone has no pair, he/she should be added to the list on his/her own
# Expected output: ["Eve-Joe", "Ashley-Fred", "Claire-Tom", "Kat-Todd", "Jane-Neef", "Jeff"]

girls = ["Eve", "Ashley", "Claire", "Kat", "Jane"]
boys = ["Joe", "Fred", "Tom", "Todd", "Neef", "Jeff"]


def join_lists(l1, l2):

    matched = []
    tup = list(zip(l1, l2))
    for k, v in tup:
        matched.append(k + '-' + v)

    if len(l1) == len(l2):
        pass

    elif len(l2) > len(l1):
        for i in l2[len(l1): len(l2)]:
            matched.append(i)

    elif len(l1) > len(l2):
        for i in l1[len(l2): len(l1)]:
            matched.append(i)

    return matched


print(join_lists(girls, boys))
