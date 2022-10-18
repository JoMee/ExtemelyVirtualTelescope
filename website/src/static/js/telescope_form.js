telescope_positioning_button = document.querySelector('.telescope_positioning_button');

altitude_value = document.querySelector('[name="altitude"]')
azimuth_value = document.querySelector('[name="azimuth"]')

console.log("hello world");


telescope_positioning_button.addEventListener('click', function () {
    console.log(altitude_value.value);
    console.log(azimuth_value.value);

    console.log("hello world");

    fetch('/submit', {
        headers : {
            'Content-Type' : 'application/json'
        },
        method : 'POST',
        body : JSON.stringify( {
            'altitude' : altitude_value.value,
            'azimuth' : azimuth_value.value
        })
    });
});

console.log(telescope_positioning_button);
