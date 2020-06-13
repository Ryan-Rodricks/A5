from A5 import Process, read_processes, schedule


def test_process():
    print('{}'.format('-' * 20))
    print('Testing Process class:\n')

    p1 = Process(3504910000, 7, 5)
    p2 = Process(3240510001, 4, 6)

    print('p1 =  {}'.format(p1))
    print('p2 =  {}'.format(p2))
    print('p1.key() = {}'.format(p1.key()))
    print('p2.key() = {}'.format(p2.key()))
    print('p1 < p2? {}'.format(p1 < p2))
    print('p1 > p2? {}'.format(p1 > p2))
    print('p1 <= p2? {}'.format(p1 <= p2))
    print('p1 >= p2? {}'.format(p1 >= p2))
    print('p1 == p2? {}'.format(p1 == p2))
    print('p1 != p2? {}'.format(p1 != p2))
    print()

    print('p1 =  {}'.format(p1))
    p2.time = 7
    print('p2 =  {}'.format(p2))
    print('p1 < p2? {}'.format(p1 < p2))
    print('p1 > p2? {}'.format(p1 > p2))
    print('p1 <= p2? {}'.format(p1 <= p2))
    print('p1 >= p2? {}'.format(p1 >= p2))
    print('p1 == p2? {}'.format(p1 == p2))
    print('p1 != p2? {}'.format(p1 != p2))
    print()

    print('p1 =  {}'.format(p1))
    p2.arrival = 5
    print('p2 =  {}'.format(p2))
    print('p1 < p2? {}'.format(p1 < p2))
    print('p1 > p2? {}'.format(p1 > p2))
    print('p1 <= p2? {}'.format(p1 <= p2))
    print('p1 >= p2? {}'.format(p1 >= p2))
    print('p1 == p2? {}'.format(p1 == p2))
    print('p1 != p2? {}'.format(p1 != p2))
    print()

    print('p1 =  {}'.format(p1))
    p2.PID = p1.PID
    print('p2 =  {}'.format(p2))
    print('p1 < p2? {}'.format(p1 < p2))
    print('p1 > p2? {}'.format(p1 > p2))
    print('p1 <= p2? {}'.format(p1 <= p2))
    print('p1 >= p2? {}'.format(p1 >= p2))
    print('p1 == p2? {}'.format(p1 == p2))
    print('p1 != p2? {}'.format(p1 != p2))
    print()

    print('End of Process class testing')
    print('{}\n'.format('-' * 20))
    return


def test_read_processes():
    print('{}'.format('-' * 20))
    print('Testing read_processes:\n')

    processes = read_processes('processes1.txt')
    for p in processes:
        print(p)
    print()

    print('End of read_processes testing')
    print('{}\n'.format('-' * 20))
    return


def test_FIFO():
    print('{}'.format('-' * 20))
    print('Testing schedule_FIFO:\n')

    print('Scheduling processes1.txt')
    schedule('processes1.txt', 'FIFO')
    print()

    print('Scheduling processes2.txt')
    schedule('processes2.txt', 'FIFO')
    print()

    print('Scheduling processes3.txt')
    schedule('processes3.txt', 'FIFO')
    print()

    print('End of schedule_FIFO testing')
    print('{}\n'.format('-' * 20))
    return
    return


def test_SJF():
    print('{}'.format('-' * 20))
    print('Testing schedule_SJF:\n')

    print('Scheduling processes1.txt')
    schedule('processes1.txt', 'SJF')
    print()

    print('Scheduling processes2.txt')
    schedule('processes2.txt', 'SJF')
    print()

    print('Scheduling processes3.txt')
    schedule('processes3.txt', 'SJF')
    print()

    print('End of schedule_SJF testing')
    print('{}\n'.format('-' * 20))
    return


test_process()
test_read_processes()
# test_FIFO()
# test_SJF()
