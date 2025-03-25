// Selecting variables from html file
const content = document.getElementById("content");
const textToAdd = document.getElementById("textToAdd");
const butItemAdd = document.getElementById("butItemAdd");
const butItemRemoveLast = document.getElementById("butItemRemoveLast");
const butItemClearAll = document.getElementById("butItemClearAll");

// Create Empty Storage "itemList" if not exist
if (localStorage.getItem("itemList") === null) {
    localStorage.setItem("itemList", "");
}

// Initialize HTML List
createList();

////
// Heper Functions
////

// Get Local Storage "itemList" and create array
function getLocalStorageAndPrepare() {
    // Get Local Storage "itemList"
    const itemList = localStorage.getItem("itemList");
    // Create array from string
    const itemListArr = itemList.split(",");
    // Remove empty and null values from array and return
    return(itemListArr.filter(function(e){return e}));
}

// Create List with Storage Items
function createList() {
    // Get Local Storage as Array
    itemListArr = getLocalStorageAndPrepare();

    // Loop over array, while elements
    let i = 0;
    while (i < itemListArr.length) {
        // Create HTML paragraph
        const newParagraph = document.createElement("p");
        newParagraph.className = "styleParagraph";
        newParagraph.innerText = itemListArr[i];
        // Append paragraph to html content
        content.appendChild(newParagraph);
        i++;
    }
}

// List all Local Storage Elements
function listStorageElements() {
    // Clear Storage Items in HTML
    content.innerHTML = "";
    createList();
}

////
// Event Listener Functions
////

// Adding Paragraph to Local Storage
function addLocalStorage() {
    // Get value from textfield
    let text = textToAdd.value.trim();
    textToAdd.value = "";
    if (text != "" || text !== null) {
        // Get Local Storage as Array
        itemListArr = getLocalStorageAndPrepare();
        // Add new value to array at last position
        itemListArr.push(text);
        // Set Local Storage "itemList"
        localStorage.setItem("itemList", itemListArr);
        // Show new "itemList"
        listStorageElements();
    }
}

// Remove Last Storage Element
function removeLastStorage() {
    itemListArr = getLocalStorageAndPrepare();
    // Remove last element from array
    itemListArr.pop();
    // Set Local Storage "itemList"
    localStorage.setItem("itemList", itemListArr);
    // Show new "itemList"
    listStorageElements();
}

// Clar All Local Storage
function clearLocalStorage() {
    // Delete Local Storage
    localStorage.clear();
    // Create empty Local Storage "itemList"
    localStorage.setItem("itemList", "");
    // Clear HTML-items
    listStorageElements();
}

// Button functions from html file
butItemAdd.addEventListener("click", addLocalStorage);
butItemRemoveLast.addEventListener("click", removeLastStorage)
butItemClearAll.addEventListener("click", clearLocalStorage);
