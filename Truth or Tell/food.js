function dare1() {
    var preferedTrail = document.getElementById("htmlTrail").value;
    if (preferedTrail == 'hiking')
        document.getElementById("dare1").innerHTML = 'Your Dare Number 1 is: <br><form action="/action_page.php"><input type="file" id="myFile" name="filename" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"><input type="submit" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"></form><br><button onclick="dare2()" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;">Next</button>';
    else if (preferedTrail == 'footpath')
        document.getElementById("dare1").innerHTML = 'Your Dare Number 1 is: <br><form action="/action_page.php"><input type="file" id="myFile" name="filename" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"><input type="submit" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"></form><br><button onclick="dare2()" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;">Next</button>';
    else if (preferedTrail == 'naturalTrail')
        document.getElementById("dare1").innerHTML = 'Your Dare Number 1 is: <br><form action="/action_page.php"><input type="file" id="myFile" name="filename" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"><input type="submit" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"></form><br><button onclick="dare2()" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;">Next</button>';
    else if (preferedTrail == 'bicycle')
        alert
        document.getElementById("dare1").innerHTML = 'Your Dare Number 1 is: <br><form action="/action_page.php"><input type="file" id="myFile" name="filename" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"><a class="btn-red"> </a> </form><br><a onclick="dare2()" class="btn-red">Next</a>';
    else
        document.getElementById("dare1").innerHTML = 'Your Dare Number 1 is: <br><form action="/action_page.php"><input type="file" id="myFile" name="filename" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"><input type="submit" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"></form><br><button onclick="dare2()" olor:#ccf2ff;color:#0008ff; font-family: courier new;">Next</button>';
}

function dare2() {
    var tryout2 = document.getElementById("comfortLevel").value;
    if (tryout2 == 'yes')
        dare2random();
    else
        dare2specific();
}

function dare2random() {
    var dare2random = ["A", "B", "C", "D"]
    var randomFoodDare = Math.floor(Math.random()*(dare2random.length));
    document.getElementById("dare2").innerHTML = 'Your Dare Number 2 is: ' + dare2random[randomFoodDare] + '<br><form action="/action_page.php"><input type="file" id="myFile" name="filename" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"><input type="submit" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"></form><br><button onclick="dare3()" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;">Next</button>';
}

function dare2specific() {
    var preferedTrail = document.getElementById("htmlFood").value;
    if (preferedTrail == 'hiking')
        document.getElementById("dare2").innerHTML = 'Your Dare Number 2 is: <br><form action="/action_page.php"><input type="file" id="myFile" name="filename" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"><input type="submit" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"></form><br><button onclick="dare3()" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;">Next</button>';
    else if (preferedTrail == 'footpath')
        document.getElementById("dare2").innerHTML = 'Your Dare Number 2 is: <br><form action="/action_page.php"><input type="file" id="myFile" name="filename" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"><input type="submit" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"></form><br><button onclick="dare3()" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;">Next</button>';
    else if (preferedTrail == 'naturalTrail')
        document.getElementById("dare2").innerHTML = 'Your Dare Number 2 is: <br><form action="/action_page.php"><input type="file" id="myFile" name="filename" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"><input type="submit" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"></form><br><button onclick="dare3()" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;">Next</button>';
    else if (preferedTrail == 'forestExploration')
        document.getElementById("dare2").innerHTML = 'Your Dare Number 2 is: <br><form action="/action_page.php"><input type="file" id="myFile" name="filename" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"><input type="submit" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"></form><br><button onclick="dare3()" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;">Next</button>';
}




function dare3() {
    var preferedFood = document.getElementById("htmlFood").value;
    if (preferedFood == 'southAsian')
        document.getElementById("dare3").innerHTML = 'Your Dare Number 3 is: <br><form action="/action_page.php"><input type="file" id="myFile" name="filename" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"><input type="submit" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"></form><br><button onclick="dare4()" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;">Next</button>';
    else if (preferedFood == 'asian')
        document.getElementById("dare3").innerHTML = 'Your Dare Number 3 is: <br><form action="/action_page.php"><input type="file" id="myFile" name="filename" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"><input type="submit" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"></form><br><button onclick="dare4()" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;">Next</button>';
    else if (preferedFood == 'mediterranean')
        document.getElementById("dare3").innerHTML = 'Your Dare Number 3 is: <br><form action="/action_page.php"><input type="file" id="myFile" name="filename" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"><input type="submit" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"></form><br><button onclick="dare4()" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;">Next</button>';
    else if (preferedFood == 'european')
        document.getElementById("dare3").innerHTML = 'Your Dare Number 3 is: <br><form action="/action_page.php"><input type="file" id="myFile" name="filename" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"><input type="submit" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"></form><br><button onclick="dare4()" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;">Next</button>';
    else if (preferedFood == 'northAmerican')
        document.getElementById("dare3").innerHTML = 'Your Dare Number 3 is: <br><form action="/action_page.php"><input type="file" id="myFile" name="filename" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"><input type="submit" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"></form><br><button onclick="dare4()" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;">Next</button>';
    else if (preferedFood == 'caribbean')
        document.getElementById("dare3").innerHTML = 'Your Dare Number 3 is: <br><form action="/action_page.php"><input type="file" id="myFile" name="filename" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"><input type="submit" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"></form><br><button onclick="dare4()" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;">Next</button>';
    else if (preferedFood == 'vietnamese')
        document.getElementById("dare3").innerHTML = 'Your Dare Number 3 is: <br><form action="/action_page.php"><input type="file" id="myFile" name="filename" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"><input type="submit" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"></form><br><button onclick="dare4()" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;">Next</button>';
    else if (preferedFood == 'italian')
        document.getElementById("dare3").innerHTML = 'Your Dare Number 3 is: <br><form action="/action_page.php"><input type="file" id="myFile" name="filename" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"><input type="submit" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"></form><br><button onclick="dare4()" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;">Next</button>';
    else
        document.getElementById("dare3").innerHTML = 'Your Dare Number 3 is: <br><form action="/action_page.php"><input type="file" id="myFile" name="filename" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"><input type="submit" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"></form><br><button onclick="dare4()" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;">Next</button>';
}

function dare4() {
    var tryout4 = document.getElementById("comfortLevel").value;
    if (tryout4 == 'yes')
        dare4random();
    else
        dare4specific();
}

function dare4random() {
    var dare4random = ["A", "B", "C"]
    var randomFoodDare = Math.floor(Math.random()*(dare4random.length));
    document.getElementById("dare4").innerHTML = 'Your Dare Number 4 is: ' + dare4random[randomFoodDare] + '<br><form action="/action_page.php"><input type="file" id="myFile" name="filename" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"><input type="submit" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"></form><br><button style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;">Next</button>';
}

function dare4specific() {
    var preferedFood = document.getElementById("htmlFood").value;
    if (preferedFood == 'southAsian')
        document.getElementById("dare4").innerHTML = 'Your Dare Number 4 is: <br><form action="/action_page.php"><input type="file" id="myFile" name="filename" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"><input type="submit" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"></form><br><button style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;">Next</button>';
    else if (preferedFood == 'asian')
        document.getElementById("dare4").innerHTML = 'Your Dare Number 4 is: <br><form action="/action_page.php"><input type="file" id="myFile" name="filename" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"><input type="submit" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"></form><br><button style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;">Next</button>';
    else if (preferedFood == 'mediterranean')
        document.getElementById("dare4").innerHTML = 'Your Dare Number 4 is: <br><form action="/action_page.php"><input type="file" id="myFile" name="filename" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"><input type="submit" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"></form><br><button style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;">Next</button>';
    else if (preferedFood == 'european')
        document.getElementById("dare4").innerHTML = 'Your Dare Number 4 is: <br><form action="/action_page.php"><input type="file" id="myFile" name="filename" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"><input type="submit" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"></form><br><button style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;">Next</button>';
    else if (preferedFood == 'northAmerican')
        document.getElementById("dare4").innerHTML = 'Your Dare Number 4 is: <br><form action="/action_page.php"><input type="file" id="myFile" name="filename" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"><input type="submit" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"></form><br><button style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;">Next</button>';
    else if (preferedFood == 'caribbean')
        document.getElementById("dare4").innerHTML = 'Your Dare Number 4 is: <br><form action="/action_page.php"><input type="file" id="myFile" name="filename" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"><input type="submit" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"></form><br><button style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;">Next</button>';
    else if (preferedFood == 'vietnamese')
        document.getElementById("dare4").innerHTML = 'Your Dare Number 4 is: <br><form action="/action_page.php"><input type="file" id="myFile" name="filename" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"><input type="submit" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"></form><br><button style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;">Next</button>';
    else if (preferedFood == 'italian')
        document.getElementById("dare4").innerHTML = 'Your Dare Number 4 is: <br><form action="/action_page.php"><input type="file" id="myFile" name="filename" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"><input type="submit" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"></form><br><button style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;">Next</button>';
    else
        document.getElementById("dare4").innerHTML = 'Your Dare Number 4 is: <br><form action="/action_page.php"><input type="file" id="myFile" name="filename" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"><input type="submit" style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;"></form><br><button style="background-color:#ccf2ff;color:#0008ff; font-family: courier new;">Next</button>';
}
