# Danh sách để lưu các công việc
tasks = []
def add_task(task_name):
 """Thêm một công việc mới vào danh sách."""
 tasks.append(task_name)
 print(f"Đã thêm công việc: '{task_name}'")
# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
 print("Chào mừng đến với ứng dụng To-Do List!")
 add_task("Học bài Git và GitHub")
 add_task("Làm bài tập thực hành ở nhà")

tasks = []
def add_task(task_name):
    tasks.append(task_name)
def list_tasks():
    print("Danh sách công việc:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
if __name__ == "__main__":
    add_task("Học bài Git")
    add_task("Làm bài tập ToDo")
    list_tasks()

tasks = []
def add_task(task_name):
    tasks.append({'name': task_name, 'completed': False})
def list_tasks():
    print("Danh sách công việc:")
    for i, task in enumerate(tasks, start=1):
        status = "[x]" if task['completed'] else "[ ]"
        print(f"{i}. {status} {task['name']}")
def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
    else:
        print("Chỉ số không hợp lệ.")
if __name__ == "__main__":
    add_task("Học Git")
    add_task("Làm bài tập ToDo")
    complete_task(0)
    list_tasks()

def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        removed = tasks.pop(task_index)
        print(f" Đã xóa: {removed['name']}")
    else:
        print(" Chỉ số không hợp lệ.")
if __name__ == "__main__":
    add_task("Học Git")
    add_task("Làm bài tập ToDo")
    list_tasks()
    delete_task(0)
    list_tasks()

