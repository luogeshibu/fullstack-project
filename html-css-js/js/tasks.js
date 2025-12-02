
// Function to fetch and display tasks
function fetchTasks() {
    fetch('http://192.168.88.88:8000/tasks/')
        .then(response => response.json())
        .then(data => {
            const taskList = document.getElementById("taskList");
            taskList.innerHTML = ""; // Clear existing tasks

            data.forEach(task => {
                addTaskToList(task);
                //console.log(task)
            });
        })
        .catch(error => console.error('Error fetching tasks:', error));
}

// Function to add a task to the task list
function addTaskToList(task) {
    let listItem = document.createElement("li");
    listItem.className = "task-item";
    
    let taskDetails = `
        <strong>${task.taskName}</strong><br>
        Description: ${task.taskDescription}<br>
        Due Date: ${task.taskDueDate}<br>
        Status: ${task.taskStatus}<br>
        <button class="delete-btn" onclick="deleteTask('${task._id}', this)">Delete</button>
        <button class="hide-btn" onclick="hideTask(this)">Hide</button>
    `;
    
    listItem.innerHTML = taskDetails;
    
    document.getElementById("taskList").appendChild(listItem);
}

// Function to add a new task
document.getElementById("taskForm").addEventListener("submit", function(event) {
    event.preventDefault();

    let taskName = document.getElementById("taskName").value;
    let taskDescription = document.getElementById("taskDescription").value;
    let taskStatus = document.getElementById("taskStatus").value;
    let taskDueDate = document.getElementById("taskDueDate").value;

    let task = {
        taskName: taskName,
        taskDescription: taskDescription,
        taskStatus: taskStatus,
        taskDueDate: taskDueDate
    };

    fetch('http://192.168.88.88:8000/tasks/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(task)
    })
    .then(response => response.json())
    .then(data => {
        addTaskToList(data);
        document.getElementById("taskForm").reset(); // Clear form fields
    })
    .catch(error => console.error('Error adding task:', error));
});

// Fetch tasks on page load
// fetchTasks();

// Function to update machines periodically
function updateMachinesPeriodically(interval) {
    // Fetch and display machines immediately
    fetchTasks();

    // Set interval to fetch and display machines every 'interval' milliseconds
    setInterval(fetchTasks, interval);
}

// Call the function to update machines every 5 seconds (5000 milliseconds)
updateMachinesPeriodically(5000); // Adjust the interval as needed



// Function to delete a task
function deleteTask(taskId, buttonElement) {
    fetch(`http://192.168.88.88:8000/tasks/${taskId}`, {
        method: 'DELETE'
    })
    .then(response => {
        if (response.ok) {
            let listItem = buttonElement.closest(".task-item");
            listItem.remove();
        } else {
            console.error('Error deleting task:', response.statusText);
        }
    })
    .catch(error => console.error('Error deleting task:', error));
}

// Function to hide a task
function hideTask(buttonElement) {
    let listItem = buttonElement.closest(".task-item");
    listItem.classList.add("completed");
    buttonElement.disabled = true;
}



// 

// Function to add a new task
// document.getElementById("taskForm").addEventListener("submit", function(event) {
//     event.preventDefault();

//     let taskName = document.getElementById("taskName").value;
//     let taskDescription = document.getElementById("taskDescription").value;
//     let taskStatus = document.getElementById("taskStatus").value;
//     let taskDueDate = document.getElementById("taskDueDate").value;

//     let task = {
//         taskName: taskName,
//         taskDescription: taskDescription,
//         taskStatus: taskStatus,
//         taskDueDate: taskDueDate
//     };

//     fetch('http://192.168.56.88:8000/tasks/', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify(task)
//     })
//     .then(response => response.json())
//     .then(data => {
//         alert('Task added successfully');
//         document.getElementById("taskForm").reset();
//     })
//     .catch(error => console.error('Error adding task:', error));
// });




