function sleepIn(weekday, vacation) {
    return !weekday || vacation;
}

function main() {
    // Test cases for sleepIn
    console.log(sleepIn(false, false)); 
    console.log(sleepIn(true, false)); 
    console.log(sleepIn(false, true)); 
    console.log(sleepIn(true, true));  
}

// Call the main function to execute
main();