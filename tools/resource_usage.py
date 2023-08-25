import psutil
import matplotlib.pyplot as plt
import time
import argparse

def plot_resource_usage_using_pid(pid, duration):
    process = psutil.Process(pid)
    plot_resource_usage(process, duration)

def plot_resource_usage(process, duration):
    cpu_percentages = []
    memory_percentages = []
    timestamps = []

    start_time = time.time()

    while time.time() - start_time < duration:
        cpu_percent = process.cpu_percent(interval=1)
        memory_percent = process.memory_percent()

        timestamp = time.time() - start_time
        cpu_percentages.append(cpu_percent)
        memory_percentages.append(memory_percent)
        timestamps.append(timestamp)
    
    # print(cpu_percentages)
    # print(memory_percentages)

    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(timestamps, cpu_percentages, marker='o')
    plt.title('CPU Usage Over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('CPU Usage (%)')

    plt.subplot(2, 1, 2)
    plt.plot(timestamps, memory_percentages, marker='o', color='orange')
    plt.title('Memory Usage Over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Memory Usage (%)')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="plot resource usage.")
    parser.add_argument("--pid", type=int, default=0)
    parser.add_argument("--dur", type=int, default=10)
    args = parser.parse_args()
    
    assert args.pid != 0 and args.dur > 0
    
    process_pid = args.pid  # Replace this with the PID of the process you want to monitor
    # process = psutil.Process(process_pid)
    monitoring_duration = args.dur  # Monitor for 60 seconds, you can adjust this

    plot_resource_usage_using_pid(process_pid, monitoring_duration)
    # plot_resource_usage(process, monitoring_duration)
