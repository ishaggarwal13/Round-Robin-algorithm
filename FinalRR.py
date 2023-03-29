import random

class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.finish_time = None
        self.waiting_time = 0

    def execute(self, time_quantum):
        if self.remaining_time <= time_quantum:
            current_time = self.finish_time = self.arrival_time + self.burst_time
            self.remaining_time = 0
        else:
            current_time = self.arrival_time + time_quantum
            self.remaining_time -= time_quantum
        return current_time

def generate_processes(num_processes, max_burst_time):
    processes = []
    for i in range(num_processes):
        arrival_time = random.randint(0, 10)
        burst_time = random.randint(1, max_burst_time)
        processes.append(Process(i+1, arrival_time, burst_time))
    return processes

def simulate_round_robin(processes, time_quantum, total_time):
    current_time = 0
    while current_time < total_time:
        all_finished = True
        for process in processes:
            if process.remaining_time > 0:
                all_finished = False
                finish_time = process.execute(time_quantum)
                for other_process in processes:
                    if other_process != process and other_process.remaining_time > 0 and other_process.arrival_time <= finish_time:
                        other_process.waiting_time += finish_time - other_process.arrival_time
        if all_finished:
            break
        current_time += time_quantum

def print_results(processes):
    total_waiting_time = 0
    total_turnaround_time = 0
    print("PID\tArrival Time\tBurst Time\tFinish Time\tWaiting Time")
    for process in processes:
        total_waiting_time += process.waiting_time
        total_turnaround_time += process.waiting_time + process.burst_time
        print(f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.finish_time}\t\t{process.waiting_time}")
    print(f"Average waiting time: {total_waiting_time/len(processes):.2f}")
    print(f"Average turnaround time: {total_turnaround_time/len(processes):.2f}")

# Example usage
processes = generate_processes(5, 10)
simulate_round_robin(processes, 2, 20)
print_results(processes)