import sys

def foo():
    #timetable = list(tuple(map(int, input().split(' '))) for _ in range(int(input())))
    n = input()
    timetable = []
    for x in sys.stdin:
        timetable.append(tuple(map(int, x.strip().split())))
    timetable = sorted(timetable, key=lambda x: (x[1], x[0]))
    reports = 0
    prev = -1
    for report in timetable:
        if prev < report[0]:
            reports += 1
            prev = report[1]
    print(reports)

foo()


