// The days of the week are: "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"

function getDayName(dateString) {
    // Write your code here
    const dayName = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    let day = new Date(dateString);
    const Index = day.getDay();
    return dayName[Index];
}
