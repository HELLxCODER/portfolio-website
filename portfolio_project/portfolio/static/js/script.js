document.addEventListener('DOMContentLoaded', function() {
    const nameElement = document.querySelector('.typing-effect');
    if (nameElement) {
        const text = nameElement.textContent;
        nameElement.textContent = '';
        nameElement.style.display = 'inline-block';
        
        let index = 0;
        
        function type() {
            if (index < text.length) {
                nameElement.textContent += text.charAt(index);
                index++;
                setTimeout(type, 150); // Speed of typing (milliseconds)
            }
        }
        setTimeout(type, 500);
    }
});