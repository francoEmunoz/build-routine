document.addEventListener('DOMContentLoaded', () => {
    const openRoutineButtons = document.querySelectorAll('[id^="openRoutine"]');
    openRoutineButtons.forEach(button => {
        button.addEventListener('click', () => {
            const routineId = button.getAttribute('data-routine-id');
            const routine = document.getElementById('routine' + routineId);
            
            if (routine) {
                if (routine.style.display === 'none') {
                    routine.style.display = 'block';
                } else {
                    routine.style.display = 'none';
                }
            }
        });
    });
});
