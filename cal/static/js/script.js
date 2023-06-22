// script.js

document.addEventListener('DOMContentLoaded', function () {
  // Get all the date elements
  const dates = document.getElementsByClassName('date');

  // Add click event listener to each date
  for (let i = 0; i < dates.length; i++) {
    dates[i].addEventListener('click', function () {
      // Get the next sibling element (event list)
      const eventList = this.nextElementSibling;

      // Toggle the visibility of the event list
      if (window.getComputedStyle(eventList).display === 'none') {
        eventList.style.display = 'block';
      } else {
        eventList.style.display = 'none';
      }
    });
  }
});
