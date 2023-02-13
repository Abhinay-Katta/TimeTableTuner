// with the grace of the great GPT:
// I know the following is the most unoptimized worst code you've ever seen and also that it hurts your eyes just by looking at it. Please excuse me, ahem.
document.addEventListener("DOMContentLoaded", function () {
    // DOMContentLoaded event listener ensures that the JavaScript code does not run
    // until the DOM has finished loading.This is to make sure that the elements you're
    // trying to select with querySelector and querySelectorAll are actually present in the DOM and can be selected.
    let h1 = document.querySelector("nav h1");
    let button = document.querySelectorAll("nav button");
    let clicked = false
    h1.addEventListener("click", function () {
        if (clicked == false) {
            for (let i = 0; i < button.length; i++) {
                button[i].style.display = "inline-block";
            }
            clicked = true;
        }
        else {
            for (let i = 0; i < button.length; i++) {
                button[i].style.display = "none";
            }
            clicked = false;
        }
    });
});

function return_div_num(num) {
    $.ajax({
        type: 'POST',
        url: '/return_json_data',
        data: { value: num },
        success: function (response) {
            document.getElementById('json').innerHTML = response;
            // handle the response from Flask here
            // TODO: print the datetime, current class, next classes and other shit using this.
        }
    });
}
// yoinked from chatGPT
// function getData() {
//     var xhr = new XMLHttpRequest();
//     xhr.open("GET", "/your_function", true);
//     xhr.onreadystatechange = function () {
//         if (xhr.readyState === 4 && xhr.status === 200) {
//             var data = JSON.parse(xhr.responseText);
//             document.getElementById("data").innerHTML = data;
//         }
//     };
//     xhr.send();
// }