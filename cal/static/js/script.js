document.addEventListener('DOMContentLoaded', function () {
  const dates = document.getElementsByClassName('date');

  for (let i = 0; i < dates.length; i++) {
    dates[i].addEventListener('click', function () {
      const eventList = this.nextElementSibling;

      if (window.getComputedStyle(eventList).display === 'none') {
        eventList.style.display = 'block';
      } else {
        eventList.style.display = 'none';
      }
    });
  }
});
