$(function() {
    $(this).find('input').keypress(function(e) {
        if(e.which == 10 || e.which == 13) {
            makeGuess();
        }
    });
});


async function makeGuess() {
    const guess = document.getElementById('weight').value;
    const answer = document.getElementById('answer').innerHTML;

    points = 100 - (2 * Math.abs(guess - answer))
    var positive;
    if (points >= 0) {
        $('#results').css("color", "green");
        $('#results').text("+" + points);
        positive = true
    }
    else {
        $('#results').css("color", "red");
        $('#results').text(points);
        positive = false
    }
    if (points == 0) {
        $('#results').css("color", "gray");
    }

    document.getElementById("weightdiv").hidden = false;
    if (points != 0) {
        animateScoreboard(points, positive)
    }

    document.getElementById("button-container").hidden = false;
}

function animateScoreboard(points, positive) {
    if (points > 0) {
        $('#score').css("color", "green");
    }
    else {
        $('#score').css("color", "red");
    }
    const finalScore = parseInt($("#score").text().split(" ")[1]) + points
    animation = setInterval(function() {
        const displayedScore = parseInt($("#score").text().split(" ")[1])
        if (displayedScore != finalScore) {
            if (positive) {
                $("#score").text("Score: " + String(displayedScore + 1))
            }
            else {
                $("#score").text("Score: " + String(displayedScore - 1))
            }
        }
        else {
            $('#score').css("color", "darkblue");
            clearInterval(animation);
        }
    }, 10)
}

function next() {
    var form = document.createElement("form");
    var score = document.createElement("input"); 
    var round = document.createElement("input");  

    form.method = "POST";
    form.action = "game";   

    score.name = "score";
    score.value = $("#score").text().split(" ")[1]
    form.appendChild(score);  

    round.name = "round";
    round.value = $("#round").text().split(" ")[1]
    form.appendChild(round);  
    form.hidden = true;
    document.body.appendChild(form);

    form.submit();
}