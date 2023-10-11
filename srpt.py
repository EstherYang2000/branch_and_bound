import heapq
from min_heap import MinHeap


class Job:
    def __init__(self, name, arrival_time, burst_time) -> None:
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time

    def __lt__(self, other):
        return self.burst_time < other.burst_time


def srpt_preemptive_scheduler(jobs):
    current_time = 0
    min_heap = MinHeap()  # Create an instance of your MinHeap
    # queue = []
    result = []
    while jobs or min_heap.heap:
        while jobs and jobs[0].arrival_time <= current_time:
            job = jobs.pop(0)
            # heapq.heappush(queue,job)
            min_heap.insert(job)

        if not min_heap.heap:
            current_time += 1
        else:
            current_job = min_heap.get_min()
            min_heap.delete()
            # current_job = heapq.heappop(queue)
            result.append(current_job.name)
            current_job.burst_time -= 1
            current_time += 1

            if current_job.burst_time > 0:
                # heapq.heappush(queue,current_job)
                min_heap.insert(current_job)
    return result, current_time


if __name__ == "__main__":
    processes = [
        Job("J1", 0, 6),
        Job("J2", 2, 2),
        Job("J3", 2, 5),
        Job("J4", 6, 2),
        Job("J5", 7, 8),
        Job("J6", 9, 2),
    ]

    result, current_time = srpt_preemptive_scheduler(processes)
    print("SRPT Order:", result)
    print("Total_Job_Time:", current_time)

    """ Q2
    SRPT Order: ['J1', 'J1', 'J2', 'J2', 'J1', 'J1', 'J1', 'J1', 'J4', 'J4', 'J6', 'J6', 'J3', 'J3', 'J3', 'J3', 'J3', 'J5', 'J5', 'J5', 'J5', 'J5', 'J5', 'J5', 'J5']
    Total_Job_Time: 25
    """

    """Q3
        The optimal value for Q1 is the minimum of all these total times.As for the Q2 using the SRPT rule to schedule the job 
        This will represent the difference between the optimal value of Q2 (SRPT) and Q1 (all possible schedules).
        Q4
        it depends on the prority queue.
        we anaylze "n" jobs and they arrive in a way that creates a skewed priority queue, 
        you could have up to O(n log n) complexity for each job's insertion and deletion. 
    """
