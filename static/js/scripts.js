document.addEventListener('DOMContentLoaded', function () {
  const btn = document.getElementById('menu-btn');
  const menu = document.getElementById('menu');

  if (btn && menu) {
    btn.addEventListener('click', () => {
      menu.classList.toggle('hidden');
    });
  }
});