// Create new date object
const date = new Date();

// Create a timestamp for current year, month and day and create todays date
const dateToday = new Date(date.getFullYear(), date.getMonth(), date.getDate());

// Create Empty Storage "timeStamp" if not exist
if (localStorage.getItem("timeStamp") === null) {
  // Create localStorage with timestamp
  localStorage.setItem("timeStamp", dateToday);
}

// If root page, show up when last used app
if (window.location.pathname == '/') {
    // Save Content from Local Storage to variable
    const dateLocalStorage = new Date(localStorage.getItem("timeStamp"));

    // Return the absolute value between the different of the dates in milliseconds
    const timeDifference = Math.abs(dateToday.getTime() - dateLocalStorage.getTime());
    // Calculate milliseconds to days -> go to seconds (*1000) -> hours (*3600) -> days (*24)
    const differenceInDays = timeDifference / (1000 * 3600 * 24);

    // Get HTML-Element id "getDay" and write a last-used-fragment in it
    if (differenceInDays == 0) {
        document.getElementById("getDay").innerHTML = "today";
    } else if (differenceInDays == 1) {
        document.getElementById("getDay").innerHTML = "yesterday";
    } else {
        document.getElementById("getDay").innerHTML = differenceInDays + "  days ago";
    }

} else {
    // If not root page set timeStamp for today
    localStorage.setItem("timeStamp", dateToday);
}
