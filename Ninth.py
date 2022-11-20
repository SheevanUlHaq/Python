def maxPercentage(dict):
    l = []
    for item in dict:
        ds = dict[item]["DS"]
        cn = dict[item]["CN"]
        python = dict[item]["Python"]
        os = dict[item]["OS"]
        total = ds+cn+python+os
        perc = (total/400)*100
        l.append(perc)
    max = l[0]
    print("Percentages are", l, "respectively: ")
    for i in l:
        if (i > max):
            max = i
    print("Maximum percentage is : ", max)


myDict = {
    "Rahul": {
        "DS": 75,
        "CN": 68,
        "Python": 83,
        "OS": 67
    },
    "Sameer": {
        "DS": 92,
        "CN": 73,
        "Python": 55,
        "OS": 53
    },
    "Saim": {
        "DS": 70,
        "CN": 72,
        "Python": 65,
        "OS": 83
    },
    "Harsh": {
        "DS": 59,
        "CN": 66,
        "Python": 79,
        "OS": 72
    }

}
print("Data of the students:- ")
print(myDict)
maxPercentage(myDict)
