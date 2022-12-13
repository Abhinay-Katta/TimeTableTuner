tt = {
    '1':
        ['Cyber Security', 'Cyber Security', 'Mobile Application Development', 'Library', 'Cyber Security-lab', 'Cyber Security'],
    '2':
        ['GPU', 'GPU', 'Employablity Skills', 'Compiler Design', 'Machine Learning', 'Machine Learning'],
    '3':
        ['Machine Learning', 'Compiler Design', 'Library', 'Library', 'Compiler Design', 'GPU'],
    '4':
        ['Mobile Application Development', 'Mobile Application Development', 'Cyber Security', 'Library', 'Mobile Application Development-LAB', 'Mobile Application Development-LAB'],
    '5':
        ['Machine Learning-LAB', 'Machine Learning-LAB', 'Compiler Design-LAB', 'Compiler Design-LAB', 'GPU-LAB', 'GPU-LAB'],
}
const d = new Date();
function findDay() {
    const day = d.getDay();
    return day;
}
function printDay() {
    const day = findDay();
    const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',]
    document.getElementById("pd").innerHTML = days[day];
}
function printClass() {
    const day = findDay();
    const hr = d.getHours();
    const min = d.getMinutes();
    var time = hr * 60 + min;
    /*test:
    if (time > 490 && time < 500) {
        document.getElementById("day").innerHTML = 'this is ass';
    }*/
    if (time > 585 && time < 645) {
        document.getElementById("day").innerHTML = tt[day][0];
    }
    else if (time > 645 && time < 705) {
        document.getElementById("day").innerHTML = tt[day][1];
    }
    else if (time > 705 && time < 765) {
        document.getElementById("day").innerHTML = 'Lunch Break';
    }
    else if (time > 765 && time < 815) {
        document.getElementById("day").innerHTML = tt[day][2];
    }
    else if (time > 815 && time < 865) {
        document.getElementById("day").innerHTML = tt[day][3];
    }
    else if (time > 865 && time < 885) {
        document.getElementById("day").innerHTML = 'Recess';
    }
    else if (time > 885 && time < 945) {
        document.getElementById("day").innerHTML = tt[day][4];
    }
    else if (time > 945 && time < 1005) {
        document.getElementById("day").innerHTML = tt[day][5];
    }
    else if (time < 585) {
        document.getElementById("day").innerHTML = "Classes have not started yet";
    }
    else if (time > 1005) {
        document.getElementById("day").innerHTML = "Classes have ended";
    }
}