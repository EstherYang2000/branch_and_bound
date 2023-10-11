# • Q1: Implement a full-enumeration tree to list all 6! schedules and their associated objective values.
# • Q2: Construct the schedule obtained from the Shortest Remaining Pro-cessing Time First (SRPT) rule. Deploy a min-heap to facilitate your implementation of the SRPT rule.
# • Q3: What is the difference between the optimal value of Q2 and the optimal value of Q1.
# • Q4: By the way, what is the run time of the SRPT algorithm?

# jobj 1 2 3 4 5 6
# rj   0 2 2 6 7 9
# pj   6 2 5 2 8 2

# 0 1 3 5 2 4
# 6 11 19 21

import itertools
import heapq


def completion_time(jobs: int, permutation: list):
    completion_times = []
    current_time = 0
    for idx in permutation:
        if current_time >= jobs[idx][0]:
            current_time = max(current_time, jobs[idx][0]) + jobs[idx][1]
            completion_times.append(current_time)
        else:
            return 0
    return completion_times[-1]


def full_enumeration_tree(jobs: list):
    all_permutations_list = list(itertools.permutations(range(len(jobs))))
    best_time_list = []
    for idx, permutation in enumerate(all_permutations_list):
        objective_value = completion_time(jobs, permutation)
        if objective_value != 0:
            best_time_list.append((idx, objective_value))
            print(
                f"Permutation: {permutation}, Total Completion Time: {objective_value}"
            )
    print(best_time_list)


if __name__ == "__main__":
    jobs = [(0, 6), (2, 2), (2, 5), (6, 2), (7, 8), (9, 2)]
    full_enumeration_tree(jobs)

    # jobj 1 2 3 4 5 6
    # rj   0 2 2 6 7 9
    # pj   6 2 5 2 8 2


# max_index = best_time_list.index(min(best_time_list[1:]))
# print("Best permuttation:"+str(all_permutations[max_index]))
# print("Min_processing_time:"+str(min(best_time_list)))
