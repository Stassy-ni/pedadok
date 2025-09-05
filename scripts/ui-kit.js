// UI kit interactions

document.querySelectorAll('.case').forEach(card => {
  const url = card.dataset.url;
  if (!url) return;
  const open = () => {
    window.location.href = url;
  };
  card.addEventListener('click', open);
  card.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      open();
    }
  });
});
