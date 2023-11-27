import threading

def parallel_sums(ranges):

    # initialize results array
    results = [0] * len(ranges)
    # initialize threads array
    threads = []

    # define function to sum range and store in results array
    def sum_range(i, start, end):
        results[i] = sum(range(start, end+1))

    # create threads for each range and run them
    for i, (start, end) in enumerate(ranges):
        t = threading.Thread(target=sum_range, args=(i, start, end))
        threads.append(t)
        t.start()
    
    # wait for all threads to finish
    for t in threads:
        t.join()

    # print results
    print(f'range sums: ', results)
    return sum(results)


def main():

    # define ranges
    ranges = [
        [10,20],
        [1,5],
        [70,80],
        [27,92],
        [0,16]
    ]

    # print results of parallel sums function
    print(f'total sum: ', parallel_sums(ranges))

    return

if __name__ == '__main__':
    main()