document.addEventListener('DOMContentLoaded', function() {
    // Typing Effect
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
                setTimeout(type, 150); // Speed of typing
            }
        }
        setTimeout(type, 500);
    }

    // Smooth Scrolling for Navigation Links
    const navLinks = document.querySelectorAll('.nav-menu a');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Parallax effect for the hero section
    window.addEventListener('scroll', function() {
        const hero = document.querySelector('.hero');
        if (hero) {
            const scrollPosition = window.pageYOffset;
            hero.style.backgroundPosition = 'center ' + (scrollPosition * 0.5) + 'px';
        }
    });
});
