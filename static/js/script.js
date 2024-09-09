// DIGITAL CLOCK

function updateClock(){

    const now = new Date();
    let hours = now.getHours();
    const meridiem = hours >= 12 ? "PM" : "AM"; //not a 24hr clock
    hours = hours % 12 || 12;
    hours = hours.toString().padStart(2, 0);
    const minutes = now.getMinutes().toString().padStart(2, 0);
    const seconds = now.getSeconds().toString().padStart(2, 0);
    const timeString = `${hours}:${minutes}${meridiem}`; //decided not to remove seconds
    document.getElementById("clock").textContent = timeString;
}

updateClock();
setInterval(updateClock, 1000);

// progress bar

document.addEventListener('DOMContentLoaded', (event) => {
    const progressBar = document.getElementById('progress-bar');
    const totalDuration = 3000; // Total duration in seconds (50mins)
    let currentDuration = 0; //have python set up to trigger on 0

    const interval = setInterval(() => {
        currentDuration++;
        const percentage = (currentDuration / totalDuration) * 100;
        progressBar.style.width = percentage + '%';

        if (currentDuration >= totalDuration) {
            clearInterval(interval);
        }
    }, 1000); // Update every second
});

// audio // 


document.addEventListener('DOMContentLoaded', function () {
    const audio = document.getElementById('audio');
    const playBtn = document.querySelector('.play-btn');
    const pauseBtn = document.querySelector('.pause-btn');
    const volumeBar = document.querySelector('.volume-bar');

    // Play Button
    playBtn.addEventListener('click', function () {
        audio.play();
    });

    // Pause Button
    pauseBtn.addEventListener('click', function () {
        audio.pause();
    });

    // Volume Bar Change
    volumeBar.addEventListener('input', function () {
        audio.volume = volumeBar.value / 100;
    });
});

// timer stuff here

document.addEventListener('DOMContentLoaded', function() {
    let countdown = 50 * 60; // 50 minutes in seconds
    const timerElement = document.getElementById('timer');

    function updateTimer() {
        const minutes = Math.floor(countdown / 60);
        const seconds = countdown % 60;
        timerElement.textContent = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
        countdown--;

        if (countdown < 0) {
            // Send request to the server when the timer ends
            fetch('/timer-end', { method: 'POST' })
                .then(response => response.json())
                .then(data => {
                    alert(data.message);
                })
                .catch(error => console.error('Error:', error));
        } else {
            setTimeout(updateTimer, 1000);
        }
    }

    updateTimer();
});



