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
function linke() {
    const sub = printClass();
    if (sub == 'Cyber Security') {

        window.location.href = 'https://bytexl-in.zoom.us/meeting/register/tZcod-GtqjgpE9GAb-ABO-3K7oTlyt2DVudD';
    }

    else if (sub == 'Recess' || sub == 'Lunch Break') {
        document.getElementById("link").innerHTML = "Break";
    }
    else {
        Document.getElementById("link").innerHTML = "Offline Class";
    }
}
function printClass() {
    const day = findDay();
    const hr = d.getHours();
    const min = d.getMinutes();
    var sub = '';
    var time = hr * 60 + min;
    if (time > 585 && time < 645) {
        sub += tt[day][0];
    }
    else if (time > 645 && time < 705) {
        sub += tt[day][1];
    }
    else if (time > 705 && time < 765) {
        sub += 'Lunch Break';
    }
    else if (time > 765 && time < 815) {
        sub += tt[day][2];
    }
    else if (time > 815 && time < 865) {
        sub += tt[day][3];
    }
    else if (time > 865 && time < 885) {
        sub += 'Recess';
    }
    else if (time > 885 && time < 945) {
        sub += tt[day][4];
    }
    else if (time > 945 && time < 1005) {
        sub += tt[day][5];
    }
    else if (time < 585) {
        sub += "Classes have not started yet";
    }
    else if (time > 1005) {
        sub += "Classes have ended";
    }
    document.getElementById("day").innerHTML = sub;
    return sub, day;
}
function nextClass() {
    const current_sub = printClass()[0];
    const current_day = printClass()[1];
    document.getElementById("next").innerHTML += tt[current_day].values(current_sub);
    // document.getElementById("next").innerHTML = tt[current_day[current_sub]];
}