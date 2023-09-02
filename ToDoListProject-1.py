#import tkinter for gui of the todo list project
import tkinter as tk
from tkinter import messagebox

class To_do_App:
    def __init__(self, root):
        self.root = root
        self.root.title("TODO_List Project")
        # Set background color
        self.root.configure(bg="#F2F2F2")  
        #tasks list
        self.tasks_list = []
        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(root, textvariable=self.task_var, width=40)
        self.task_entry.pack(pady=10)
#button for adding, updating, mark completed and delete items
        self.button_of_addition = tk.Button(root, text="Add Task", command=self.add_tasks_to_list, bg="#4CAF50", fg="white")
        self.button_of_addition.pack()
        self.list_box_of_tasks = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10, bg="#E0E0E0")
        self.list_box_of_tasks.pack(pady=10)

        self.Compuleted_mark_button = tk.Button(root, text="Mark as Completed", command=self.mark_completed_task, bg="#FFC107", fg="black")
        self.Compuleted_mark_button.pack()

        self.button_of_deleting_item = tk.Button(root, text="Delete Task", command=self.delete_task, bg="#F44336", fg="white")
        self.button_of_deleting_item.pack()

        self.button_of_updating_task = tk.Button(root, text="Update Task", command=self.task_update, bg="#2196F3", fg="white")
        self.button_of_updating_task.pack()
 #appending tasks to list       
    def add_tasks_to_list(self):
        task = self.task_var.get()
        if task:
            self.tasks_list.append({"task": task, "completed": False})
            self.task_list_updation()
            self.task_var.set("")
    
    def task_list_updation(self):
        self.list_box_of_tasks.delete(0, tk.END)
        for task_info in self.tasks_list:
            task_status = "✔" if task_info["completed"] else " "
            self.list_box_of_tasks.insert(tk.END, f"{task_status} {task_info['task']}")
    
    def mark_completed_task(self):
        selected_index = self.list_box_of_tasks.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks_list[index]["completed"] = True
            self.task_list_updation()
    
    def delete_task(self):
        selected_index = self.list_box_of_tasks.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks_list[index]
            self.task_list_updation()
    
    def task_update(self):
        selected_index = self.list_box_of_tasks.curselection()
        if selected_index:
            index = selected_index[0]
            new_task = self.task_var.get()
            if new_task:
                self.tasks_list[index]["task"] = new_task
                self.task_list_updation()

if __name__ == "__main__":
    root = tk.Tk()
    app = To_do_App(root)
    root.mainloop()
