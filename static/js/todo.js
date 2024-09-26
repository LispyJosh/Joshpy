document.addEventListener('DOMContentLoaded', () => {
    const todoForm = document.getElementById('todo-form');
    const todoList = document.getElementById('todo-list');

    // Fetch existing tasks
    fetch('/get-todos')
        .then(response => response.json())
        .then(tasks => {
            tasks.forEach(task => {
                addTaskToList(task);
            });
        });

    // Handle form submission
    todoForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const taskInput = document.getElementById('todo-input');
        const etaInput = document.getElementById('eta-input');
        const priorityInput = document.getElementById('priority-select');
        const dueDateInput = document.getElementById('due-date-input');

        const newTask = { 
            task: taskInput.value,
            eta: etaInput.value,
            priority: priorityInput.value,
            due_date: dueDateInput.value
        };

        fetch('/add-todo', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(newTask)
        })
        .then(response => response.json())
        .then(data => {
            addTaskToList({
                id: data.id, 
                task: data.task, 
                eta: data.eta, 
                priority: data.priority, 
                due_date: data.due_date
            });
            taskInput.value = '';  // Clear the input fields
            etaInput.value = '';
            priorityInput.value = '';
            dueDateInput.value = '';
        });
    });

    // Function to add task to list
    function addTaskToList(task) {
        const li = document.createElement('li');
        li.textContent = `Task: ${task.task}, ETA: ${task.eta}, Priority: ${task.priority}, Due Date: ${task.due_date}`;
        
        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = 'Delete';
        deleteBtn.addEventListener('click', () => {
            fetch(`/delete-todo/${task.id}`, { method: 'DELETE' })
                .then(() => {
                    li.remove();
                });
        });
        li.appendChild(deleteBtn);
        todoList.appendChild(li);
    }
});
