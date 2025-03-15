document.addEventListener('DOMContentLoaded', () => {
    const testButton = document.getElementById('testButton');
    const output = document.getElementById('output');
    
    testButton.addEventListener('click', () => {
        const currentTime = new Date().toLocaleTimeString();
        output.innerHTML = `Button clicked at: ${currentTime}`;
        output.classList.add('active');
        
        // Test console output
        console.log('Button clicked!', {
            time: currentTime,
            event: 'click'
        });
    });
}); 