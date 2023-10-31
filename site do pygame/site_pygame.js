const slider = document.querySelector('#slider');
const btnLeft = document.getElementById('moveLeft');
const btnRight = document.getElementById('moveRight');
const indicators = document.querySelectorAll('.indicator');

let baseSliderWidth = slider.offsetWidth;
let activeIndex = 0; // O índice atual na lista de slides

// Preencher o slider com todos os filmes no array de filmes
function populateSlider(movies) {
    movies.forEach(image => {
        // Clonar o filme inicial que está incluído no HTML, depois substituir a imagem por uma diferente
        const newMovie = document.getElementById('movie0');
        let clone = newMovie.cloneNode(true);
        let img = clone.querySelector('img');
        img.src = image.src;
        slider.insertBefore(clone, slider.childNodes[slider.childNodes.length - 1]);
    });
}

// Atualizar os indicadores que mostram em qual página estamos atualmente
function updateIndicators(index) {
    indicators.forEach(indicator => {
        indicator.classList.remove('active');
    });
    let newActiveIndicator = indicators[index];
    newActiveIndicator.classList.add('active');
}

// Botão para rolar para a esquerda
btnLeft.addEventListener('click', e => {
    let movieWidth = document.querySelector('.movie').getBoundingClientRect().width;
    let scrollDistance = movieWidth * 6; // Rolar o comprimento de 6 filmes
    slider.scrollBy({ top: 0, left: -scrollDistance, behavior: 'smooth' });
    activeIndex = (activeIndex - 1 + 3) % 3;
    updateIndicators(activeIndex);
});

// Botão para rolar para a direita
btnRight.addEventListener('click', e => {
    let movieWidth = document.querySelector('.movie').getBoundingClientRect().width;
    let scrollDistance = movieWidth * 6; // Rolar o comprimento de 6 filmes
    slider.scrollBy({ top: 0, left: scrollDistance, behavior: 'smooth' });
    activeIndex = (activeIndex + 1) % 3;
    updateIndicators(activeIndex);
});

// Inicializar o carrossel
populateSlider();
updateIndicators(activeIndex);