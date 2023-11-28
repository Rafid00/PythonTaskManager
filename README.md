# PythonTaskManager

![Screenshot 2023-11-27 235130](https://github.com/Rafid00/PythonTaskManager/assets/48888237/a9109aed-869c-4cff-a82a-e3530f736222)

Developing a GUI application to track and log system activity in real-time is the main goal of the "Development of Monitoring and Activity Logging Application" project. The program makes use of the psutil package to get important system data like CPU and memory utilization, network activity, and active processes. Users may efficiently monitor system performance, spot resource-guzzling activities, and assess overall system activity by viewing this data on the GUI. The project's elements and results are thoroughly analyzed in the review that follows.

# Explaination

The ‘psutil’ library is imported to retrieve system information, `tkinter` library is imported for creating the GUI.
The ‘get_system_info()’ function updates the system information by using ‘psutil’ to retrieve information about CPU usage, network usage, and running processes.
The ‘update_system_info()’ function updates the system information in the GUI by calling ‘get_system_info()’. It updates the CPU label, memory label, and process list.
A Treeview widget is created to display the list of running processes. Columns are defined for the process attributes.
The main event loop (root.mainloop()) is executed to run the GUI.
