let slideIndex = 0;
showSlides(slideIndex);

function moveSlide(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("carousel-item");
  let indicators = document.getElementsByClassName("indicator");
  if (n >= slides.length) {slideIndex = 0}
  if (n < 0) {slideIndex = slides.length - 1}
  for (i = 0; i < slides.length; i++) {
      slides[i].classList.remove("active");
      indicators[i].classList.remove("active");
  }
  slides[slideIndex].classList.add("active");
  indicators[slideIndex].classList.add("active");
}