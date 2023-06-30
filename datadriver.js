console.log("fetching data");

fetch("traveltime/traveltime.csv").then((response) => {

    if (!response.ok) {
        throw new Error(`HTTP error: ${response.status}`);
    }
    return
}).then((text) => {
    console.log(text);
});