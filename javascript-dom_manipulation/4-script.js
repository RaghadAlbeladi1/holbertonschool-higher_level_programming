const list = document.querySelector('.my_list');
const addDiv = document.querySelector('#add_item');

addDiv.addEventListener('click', () => {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  list.appendChild(newItem);
});
