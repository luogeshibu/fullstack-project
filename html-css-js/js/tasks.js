const API_BASE = "http://192.168.88.88:8000/tasks/";
let editingTaskId = null;

// Fetch tasks
function fetchTasks() {
    fetch(API_BASE)
        .then(response => response.json())
        .then(data => {
            const taskList = document.getElementById("taskList");
            taskList.innerHTML = "";

            data.forEach(task => addTaskToList(task));
        })
        .catch(error => console.error("Error fetching tasks:", error));
}

// Add task to list
function addTaskToList(task) {
    let listItem = document.createElement("li");
    listItem.className = "task-item";

    listItem.innerHTML = `
        <strong>${task.taskName}</strong><br>
        Description: ${task.taskDescription}<br>
        Due Date: ${task.taskDueDate}<br>
        Status: ${task.taskStatus}<br>

        <button onclick="openEditModal('${task._id}', '${task.taskName}', '${task.taskDescription}', 
                '${task.taskStatus}', '${task.taskDueDate}')">
            Edit
        </button>

        <button onclick="deleteTask('${task._id}', this)">Delete</button>
        <button onclick="hideTask(this)">Hide</button>
    `;

    document.getElementById("taskList").appendChild(listItem);
}

// Add new task
document.getElementById("taskForm").addEventListener("submit", function(event) {
    event.preventDefault();

    let task = {
        taskName: document.getElementById("taskName").value,
        taskDescription: document.getElementById("taskDescription").value,
        taskStatus: document.getElementById("taskStatus").value,
        taskDueDate: document.getElementById("taskDueDate").value
    };

    fetch(API_BASE, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(task)
    })
    .then(() => {
        document.getElementById("taskForm").reset();
        fetchTasks();
    })
    .catch(error => console.error("Error adding task:", error));
});

// Delete task
function deleteTask(taskId, buttonElement) {
    fetch(API_BASE + taskId, { method: "DELETE" })
        .then(response => {
            if (response.ok) {
                buttonElement.closest(".task-item").remove();
            }
        })
        .catch(error => console.error("Error deleting task:", error));
}

// Hide task
function hideTask(buttonElement) {
    let listItem = buttonElement.closest(".task-item");

    // 获取标题
    const title = listItem.querySelector("strong").innerText;

    // 只显示标题
    listItem.innerHTML = `
        <strong>${title}</strong><br>
        <span style="color: gray; font-size: 12px;">(Hidden)</span>
    `;
}


// ====== Edit Task ======

function openEditModal(id, name, desc, status, dueDate) {
    editingTaskId = id;

    document.getElementById("editTaskName").value = name;
    document.getElementById("editTaskDescription").value = desc;
    document.getElementById("editTaskStatus").value = status;
    document.getElementById("editTaskDueDate").value = dueDate;

    document.getElementById("editModal").style.display = "flex";
}

function closeEditModal() {
    document.getElementById("editModal").style.display = "none";
}

// Save edited task (PUT)
function saveEditedTask() {
    const updatedTask = {
        taskName: document.getElementById("editTaskName").value,
        taskDescription: document.getElementById("editTaskDescription").value,
        taskStatus: document.getElementById("editTaskStatus").value,
        taskDueDate: document.getElementById("editTaskDueDate").value
    };

    fetch(API_BASE + editingTaskId, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(updatedTask)
    })
    .then(() => {
        closeEditModal();
        fetchTasks();
    })
    .catch(error => console.error("Error updating task:", error));
}

// Auto fetch tasks every 5 seconds
setInterval(fetchTasks, 5000);
fetchTasks();
