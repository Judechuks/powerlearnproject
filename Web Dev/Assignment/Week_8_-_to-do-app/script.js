(() => {
  let toDoListArray = [];
  const form = document.querySelector(".form");
  const input = document.querySelector(".form_input");
  const ul = document.querySelector(".toDoList");

  // event listeners
  form.addEventListener("submit", (e) => {
    // prevent default behavior - Page reload
    e.preventDefault();
    // give item a unique ID
    let itemId = String(Date.now());
    // get/assign input value
    let toDoItem = input.value;
    // pass ID and item into functions
    addItemToDOM(itemId, toDoItem);
    addItemToArray(itemId, toDoItem);
    // clear the input box. (this is default behavior but we got rid of that)
    input.value = "";
  });

  ul.addEventListener("click", (e) => {
    let id = e.target.getAttribute("data-id");
    if (!id) return; // user clicked in something else
    // pass id through to functions
    removeItemFromDOM(id);
    removeItemFromArray(id);
  });

  function addItemToDOM(itemId, toDoItem) {
    // create li and trash icon to delete toDoItem
    const li = document.createElement("li");
    const i = document.createElement("i");
    li.setAttribute("data-id", itemId);
    i.setAttribute("class", "fa fa-trash");
    i.setAttribute("data-id", itemId);
    // add toDoItem text to li
    li.innerText = toDoItem;
    li.appendChild(i);

    // add li to the DOM
    ul.appendChild(li);
  }

  function addItemToArray(itemId, toDoItem) {
    // add item to array as an object with an ID so we can find and delete it later
    toDoListArray.push({ itemId, toDoItem });
  }

  function removeItemFromDOM(id) {
    var li = document.querySelector('[data-id="' + id + '"]');
    ul.removeChild(li);
  }

  function removeItemFromArray(id) {
    toDoListArray = toDoListArray.filter((item) => item.itemId !== id);
  }
})();
