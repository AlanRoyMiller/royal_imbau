// vanilla JS
// init with element
var grid = document.querySelector('.grid');
var msnry = new Masonry( grid, {
  // options...
  itemSelector: '.grid-item',
  columnWidth: 300
});

// Only one Masonry initialization is needed; remove duplicate or unused code.
// If not used in your HTML, this file has no effect.