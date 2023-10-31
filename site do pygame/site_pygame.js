let currentSlide = 0;

function showSlide(index) {
    const slides = document.querySelectorAll('.slide');
    for (let i = 0; i < slides.length; i++) {
        let offset = i - index;
        if (offset < 0) offset = slides.length + offset;
        let opacity = (offset === 0) ? 1 : 0.6;
        slides[i].style.transform = `rotateY(${offset * 60}deg) translateZ(500px)`;
        slides[i].style.opacity = opacity;
    }
}

function nextSlide() {
    currentSlide = (currentSlide + 1) % document.querySelectorAll('.slide').length;
    showSlide(currentSlide);
}

function prevSlide() {
    currentSlide = (currentSlide - 1 + document.querySelectorAll('.slide').length) % document.querySelectorAll('.slide').length;
    showSlide(currentSlide);
}

// Inicializa o carrossel
showSlide(currentSlide);