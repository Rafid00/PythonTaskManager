import psutil
import tkinter as tk
from tkinter import ttk

def get_system_info():
    # Retrieve system information using psutil library
    cpu_percent = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    network = psutil.net_io_counters()
    processes = psutil.process_iter()

    return cpu_percent, memory, network, processes

def update_system_info():
    # Update system information in the GUI
    cpu_percent, memory, network, processes = get_system_info()

    # Update CPU label
    cpu_label.config(text=f'CPU Usage: {cpu_percent}%')

    # Update memory label
    memory_label.config(text=f'Memory Usage: {memory.percent}%')

    # Update network label
    network_label.config(text=f'Network Usage: Sent: {network.packets_sent} packets, Received: {network.packets_recv} packets')

    # Clear the process list
    process_list.delete(*process_list.get_children())

    # Populate the process list with the current running processes
    for process in processes:
        process_info = process.as_dict(attrs=['pid', 'name', 'username', 'cpu_percent', 'memory_percent'])
        process_list.insert("", "end", values=(
            process_info['pid'],
            process_info['name'],
            process_info['username'],
            f'{process_info["cpu_percent"]:.2f}%',
            f'{process_info["memory_percent"]:.2f}%'
        ))

    # Schedule the next update in 1 second
    root.after(1000, update_system_info)

# Create the root window
root = tk.Tk()
root.title("Task Manager")
root.geometry("1000x600") 

# Create labels to display system information
cpu_label = ttk.Label(root, text="CPU Usage: ")
cpu_label.pack()

memory_label = ttk.Label(root, text="Memory Usage: ")
memory_label.pack()

network_label = ttk.Label(root, text="Network Usage: ")
network_label.pack()

# Create a table to display the list of processes
process_columns = ("PID", "Name", "Username", "CPU", "Memory")
process_list = ttk.Treeview(root, columns=process_columns, show="headings")

for col in process_columns:
    process_list.heading(col, text=col)

# Create a vertical scrollbar
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=process_list.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the Treeview widget to use the scrollbar
process_list.configure(yscrollcommand=scrollbar.set)
process_list.pack(expand=True, fill=tk.BOTH)  # Make the task window expand to fill available space

# Start updating system information
update_system_info()

# Run the main event loop
root.mainloop()