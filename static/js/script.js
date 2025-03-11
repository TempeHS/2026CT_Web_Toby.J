player_guess = prompt("Enter rock, paper or scissors");

if (
  player_guess == "Rock" ||
  player_guess == "Scissors" ||
  player_guess == "Paper"
) {
  document.getElementById("user_feedback").innerHTML = "Error, No capitals";

  exit();
}

comp_guess = randomIntFromInterval(1, 3);

if (comp_guess == 1) {
  comp_guess = "rock";
}

if (comp_guess == 2) {
  comp_guess = "paper";
}

if (comp_guess == 3) {
  comp_guess = "scissors";
}

alert("Computer chose " + comp_guess);

if (player_guess == comp_guess) {
  document.getElementById("user_feedback").innerHTML =
    "Tie!  You both chose " + player_guess;
}

if (player_guess == "rock" && comp_guess == "scissors") {
  document.getElementById("user_feedback").innerHTML =
    "You Win! " + player_guess + " beats " + comp_guess;
}

if (player_guess == "rock" && comp_guess == "paper") {
  document.getElementById("user_feedback").innerHTML =
    "You lose! " + comp_guess + " beats " + player_guess;
}

if (player_guess == "scissors" && comp_guess == "paper") {
  document.getElementById("user_feedback").innerHTML =
    "You win! " + player_guess + " beats " + comp_guess;
}

if (player_guess == "scissors" && comp_guess == "rock") {
  document.getElementById("user_feedback").innerHTML =
    "You lose! " + comp_guess + " beats " + player_guess;
}

if (player_guess == "paper" && comp_guess == "scissors") {
  document.getElementById("user_feedback").innerHTML =
    "You lose! " + comp_guess + " beats " + player_guess;
}

if (player_guess == "paper" && comp_guess == "rock") {
  document.getElementById("user_feedback").innerHTML =
    "You win! " + player_guess + " beats " + comp_guess;
}

function randomIntFromInterval(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}
