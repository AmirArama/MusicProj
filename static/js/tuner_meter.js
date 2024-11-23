function updateGauge(offset) {
    // Clear previous fills
    document.querySelectorAll('.gauge-rectangle').forEach(rect => rect.classList.remove('filled'));
    document.getElementById('center-triangle').classList.remove('center-filled');
    document.getElementById('arrow-left').style.borderRightColor = 'lime';
    document.getElementById('arrow-right').style.borderLeftColor = 'lime';
    document.getElementById("arrow-left").style.visibility = "hidden";
    document.getElementById("arrow-right").style.visibility = "hidden";
    // Set new fills based on the offset
    if (offset === 0) {
        document.getElementById('center-triangle').classList.add('center-filled');
    } else if (offset < 0) {
        document.getElementById('arrow-right').style.borderRightColor = 'lime';
        document.getElementById("arrow-right").style.visibility = "visible";
        document.getElementById("arrow-left").style.visibility = "hidden";
        if (offset <= -50) document.getElementById('rect-50').classList.add('filled');
        if (offset <= -40) document.getElementById('rect-40').classList.add('filled');
        if (offset <= -30) document.getElementById('rect-30').classList.add('filled');
        if (offset <= -20) document.getElementById('rect-20').classList.add('filled');
        if (offset <= -10) document.getElementById('rect-10').classList.add('filled');
    } else {
        document.getElementById('arrow-left').style.borderRightColor = 'lime';
        document.getElementById("arrow-left").style.visibility = "visible";
        document.getElementById("arrow-right").style.visibility = "hidden";
        if (offset >= 10) document.getElementById('rect10').classList.add('filled');
        if (offset >= 20) document.getElementById('rect20').classList.add('filled');
        if (offset >= 30) document.getElementById('rect30').classList.add('filled');
        if (offset >= 40) document.getElementById('rect40').classList.add('filled');
        if (offset >= 50) document.getElementById('rect50').classList.add('filled');
    }
}

setInterval(() => {
    document.getElementById('rect-50').classList.remove('filled');
    document.getElementById('rect-40').classList.remove('filled');
    document.getElementById('rect-30').classList.remove('filled');
    document.getElementById('rect-20').classList.remove('filled');
    document.getElementById('rect-10').classList.remove('filled');
    document.getElementById('rect50').classList.remove('filled');
    document.getElementById('rect40').classList.remove('filled');
    document.getElementById('rect30').classList.remove('filled');
    document.getElementById('rect20').classList.remove('filled');
    document.getElementById('rect10').classList.remove('filled');

    document.getElementById("arrow-right").style.visibility = "hidden";
    document.getElementById("arrow-left").style.visibility = "hidden";

}, 3000);