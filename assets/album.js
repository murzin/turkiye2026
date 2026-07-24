(() => {
  const dialog = document.querySelector('.lightbox');
  if (!dialog) return;
  const image = dialog.querySelector('.lightbox-image');
  const counter = dialog.querySelector('[data-lightbox-counter]');
  const caption = dialog.querySelector('[data-lightbox-caption]');
  const cards = Array.from(document.querySelectorAll('.photo-card'));
  let active = 0;

  const show = (index) => {
    active = (index + cards.length) % cards.length;
    const card = cards[active];
    image.src = card.dataset.full;
    image.alt = card.querySelector('img').alt;
    caption.textContent = card.dataset.caption;
    counter.textContent = `${active + 1} / ${cards.length}`;
  };
  cards.forEach((card, index) => card.addEventListener('click', () => {
    show(index);
    dialog.showModal();
  }));
  dialog.querySelector('.lightbox-prev').addEventListener('click', () => show(active - 1));
  dialog.querySelector('.lightbox-next').addEventListener('click', () => show(active + 1));
  dialog.querySelector('.lightbox-close').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', (event) => { if (event.target === dialog) dialog.close(); });
  dialog.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowLeft') { event.preventDefault(); show(active - 1); }
    if (event.key === 'ArrowRight') { event.preventDefault(); show(active + 1); }
  });
})();
