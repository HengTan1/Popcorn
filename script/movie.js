const track = document.querySelector('.carousel_track');
const slides = Array.from(track.children);
const nextBtn = document.querySelector('.carousel_btn--right');
const prevBtn = document.querySelector('.carousel_btn--left');
const navDots = document.querySelector('.carousel_nav');
const dots = Array.from(navDots.children);

//getting width of screen
const slideSize = slides[0].getBoundingClientRect();
const slideWidth = slideSize.width;

//arrange slide from the others slide
//for each slide move next slide to the left with amount = screenWidth
const setSlidePosition = (slide, index) => {
  slide.style.left = slideWidth * index + 'px';
}

slides.forEach(setSlidePosition);

//reveal left-right button
const revealArrowBtn = (slides, prevBtn, nextBtn, targetIndex) => {
if (targetIndex === 0) {
    prevBtn.classList.add('is-hidden');
    nextBtn.classList.remove('is-hidden');
  } 
  else if (targetIndex === slides.length - 1) {
    prevBtn.classList.remove('is hidden');
    nextBtn.classList.add('is-hidden');
  }
  else {
    prevBtn.classList.remove('is-hidden');
    nextBtn.classList.remove('is-hidden');  
  }
}
 
//btn controlling
const moveToSlide = (track, currentSlide, targetSlide) => {
  track.style.transform = 'translateX(-' + targetSlide.style.left + ')';
  
  currentSlide.classList.remove('current-slide');
  targetSlide.classList.add('current-slide');
}

//on click left move to the left slide
prevBtn.addEventListener('click', e => {
  //move to the slide on the right
  const currentSlide = track.querySelector('.current-slide');
  const prevSlide = currentSlide.previousElementSibling;
  const currentDot = navDots.querySelector('.current-slide');
  const prevDot = currentDot.previousElementSibling;
  const prevIndex = slides.findIndex(slide => slide === prevSlide);
  
  
  moveToSlide(track, currentSlide, prevSlide);
  updateDots(currentDot, prevDot);
  
  revealArrowBtn(slides, prevBtn, nextBtn, prevSlide);
})

//on click right move to the right slide
nextBtn.addEventListener('click', e => {
  //move to the slide on the right
  const currentSlide = track.querySelector('.current-slide');
  const nextSlide = currentSlide.nextElementSibling;
  const currentDot = navDots.querySelector('.current-slide');
  const nextDot = currentDot.nextElementSibling;
  const nextIndex = slides.findIndex(slide => slide === nextSlide);
  
  moveToSlide(track, currentSlide, nextSlide);
  updateDots(currentDot, nextDot);
  
  revealArrowBtn(slides, prevBtn, nextBtn, nextIndex);
})

//on click dot move to the exact slide
//dot update
const updateDots = (currentDot, targetDot) => {
  
  currentDot.classList.remove('current-slide');
  targetDot.classList.add('current-slide');
}

//on click dot
navDots.addEventListener('click', e =>{
  //Which dot is clicked on?
  const targetDot = e.target.closest('button');
  if (!targetDot) return;
  
  const currentSlide = track.querySelector('.current-slide');
  const currentDot = navDots.querySelector('.current-slide');
  
  //which slide to show?
  const targetIndex = dots.findIndex(dot => dot === targetDot);
  const targetSlide = slides[targetIndex];
  
  moveToSlide(track, currentSlide, targetSlide);
  updateDots(currentDot, targetDot);
  
  revealArrowBtn(slides, prevBtn, nextBtn, targetIndex);
})

//on click poster popup screen blur background
function toggle(element) {
  // get data of specific item
  /*
  var parent = $(element).parent();
  var movie_name = parent.find('.movie-name').html();
  var movie_description = parent.find('.movie-description').html();
  var movie_trailer_url = parent.find('.movie-trailer-url').html();
  var movie_director = parent.find('.movie-trailer-url').html();
  var movie_cast = parent.find('.movie-trailer-url').html();

  // set data to popup
  var popup = $('#popup');
  popup.find('.movie_name').html(movie_description);
  popup.find('.movie_description').html('Movie description: ' + movie_description);
  popup.find('.trailer source').prop('src', movie_trailer_url);
  popup.find('.movie_director').html('Director: ' + movie_director);
  popup.find('.movie_cast').html('Actor/Actress: ' + movie_cast);
  */
  // toggle show popup
  $('#blur').toggle('active');
  $('#popup').toggle('active');
}

// call ajax onload to get data 

window.document.onload = function () {
  $.ajax({
    url: '127.0.0.1/get-data',
    data: {data_id: id},
    success: function(data) {
      //data la 1 object JSON 
      var data = JSON.parse(data);

      // data has 5 items
      $.each(data, function (index, value) {
        // create element (for each movies create 1 template and 1 dot)
        $('.carousel_track').append(li_template);
        $('.carousel_nav').append('<button class="carousel_dot"></button>');

        // set data to element (the item.x x is the json attributes)
        $('.carousel_img').prop('src', item.img_url);
        $('.text-info').html(item.movie_name);
        $('.text-info-r').html(item.movie_rating_point);
        $('.movie-name').html(item.movie_name);
        $('.movie-description').html(item.movie_description);
        $('.movie-trailer-url').html(item.movie_trailer_url);
        $('.movie-director').html(item.movie_director);
        $('.movie-cast').html(item.movie_cast); 
      });
     
      // set default
      $('.carousel_nav').find('button:first-child').addClass('current-slide');
      $('.carousel_track').find('carousel_slide:first-child').addClass('current-slide');
    }
  })
}