# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime as dt


def check_gas_testing_time_compliance() -> bool:
    with open("entrant_gas_reading.csv", "r") as entrant_reading:
        e = entrant_reading.readlines()

    # Extracting read,entry & exit time for the first entrant
    t = e[0].split('\t')
    read_time = dt.datetime.strptime(t[0].strip(), '%Y-%m-%dT%H:%M:%S.%f%z')
    entry_time = dt.datetime.strptime(t[1].strip(), '%Y-%m-%dT%H:%M:%S.%f%z')
    exit_time = dt.datetime.strptime(t[2].strip(), '%Y-%m-%dT%H:%M:%S.%f%z')

    # Extracting all the gas readings in entrant file
    e1 = []
    for i in e:
        temp = i.split('\t')
        e1.append(temp[0])
        temp = []

    # Reading periodic file as lines and storing it as list
    with open("periodical_gas_reading.csv", "r") as periodical_reading:
        next(periodical_reading)
        p = periodical_reading.readlines()

    compliant = 0
    loop_v = 0
    k_time = entry_time - dt.timedelta(minutes=-30)

    if exit_time <= k_time:
        print('Compliant')

    else:
        while k_time < exit_time:
            loop_v += 1

            for i in p:
                t1 = dt.datetime.strptime(i.strip(), '%Y-%m-%dT%H:%M:%S.%f%z')
                if t1 >= read_time and t1 <= k_time:
                    compliant += 1
            for i in e1:
                if i != e1[0]:
                    t1 = dt.datetime.strptime(i.strip(), '%Y-%m-%dT%H:%M:%S.%f%z')
                    if t1 >= read_time and t1 <= k_time:
                        compliant += 1

            read_time = k_time
            k_time = k_time - dt.timedelta(minutes=-30)

    if loop_v <= compliant:
        res = True
    else:
        res = False
    return res


if __name__ == "__main__":
    if check_gas_testing_time_compliance():
        print("Compliant")
    else:
        print("Not Compliant")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
