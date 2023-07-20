import psutil
import tkinter as tk
from tkinter import ttk

def get_system_info():
    # Retrieve system information using psutil library
    cpu_percent = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    network = psutil.net_io_counters()
    processes = psutil.process_iter(attrs=['pid', 'name', 'username', 'cpu_percent', 'memory_percent'])

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
        process_info = process.info
        process_list.insert("", "end", values=(
            process_info['pid'],
            process_info['name'],
            process_info['username'],
            f'{process_info["cpu_percent"]:.2f}%',
            f'{process_info["memory_percent"]:.2f}%'
        ))

    # Schedule the next update in 1 second
    root.after(5000, update_system_info)

def end_task():
    # Get the selected item from the process list
    selected_item = process_list.selection()
    if selected_item:
        pid = int(process_list.item(selected_item, "values")[0])  # Convert PID to integer

        try:
            # Terminate the selected process
            process = psutil.Process(pid)
            process.terminate()
        except psutil.NoSuchProcess:
            pass


def search_process():
    query = search_entry.get().lower()
    process_list.delete(*process_list.get_children())

    for process in processes:
        process_info = process.info
        process_name = process_info['name'].lower()
        
        if query in process_name:
            process_list.insert("", "end", values=(
                process_info['pid'],
                process_info['name'],
                process_info['username'],
                f'{process_info["cpu_percent"]:.2f}%',
                f'{process_info["memory_percent"]:.2f}%'
            ))


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

# Create the "End Task" button
end_task_button = ttk.Button(root, text="End Task", command=end_task, style="White.TButton")
end_task_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Configure the style for the "End Task" button
style = ttk.Style()
style.configure("White.TButton", foreground="black", background="white", font=("Helvetica", 11, "bold"))

# Run the main event loop
root.mainloop()
