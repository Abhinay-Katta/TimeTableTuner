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
            // handle the parsed_response here
            // For example:
            document.getElementById('day').innerHTML = response[0];
            document.getElementById('time').innerHTML = response[1];
            document.getElementById('class').innerHTML = response[2];
            document.getElementById('previous_class').innerHTML = response[3];
            document.getElementById('next_class').innerHTML = response[4];
        }
    });
}