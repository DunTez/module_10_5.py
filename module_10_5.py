import multiprocessing
import datetime

start = datetime.datetime.now()
def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


if __name__ == '__main__':

    filenames = [f'./file {number}.txt' for number in range(1, 5)]


    x = datetime.datetime.now()
    for file_name in filenames:
        read_info(file_name)
        y = datetime.datetime.now()
    print(y - x)

    x2 = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
        y2 = datetime.datetime.now()
    print(y2 - x2)