#!/usr/bin/node
/* JavaScript script that updates the text color of the <header>
  using querySelector
 */
document.addEventListener('DOMContentLoaded', function () {
  const header = document.querySelector('header');
  header.style.color = '#FF0000';
});
