const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

// Set canvas size
canvas.width = 800;
canvas.height = 600;

// Game variables
let paddleA = { x: 50, y: 300, width: 10, height: 100 };
let paddleB = { x: 740, y: 300, width: 10, height: 100 };
let ball = { x: 400, y: 300, radius: 10, dx: 5, dy: 5 };
let scoreA = 0;
let scoreB = 0;
let gameState = "splash"; // Initial game state
let isPaused = false;
let timeLimit = 30; // Time limit in seconds
let startTime;
let aiActive = false; // Track AI activation

// Load assets
const splashImage = new Image();
splashImage.src = 'assets/splash_pong.gif';
const gameBackgroundImage = new Image();
gameBackgroundImage.src = 'assets/game_background.gif';
const gameoverImage = new Image();
gameoverImage.src = 'assets/gameover.gif';

// Sound
const bounceSound = new Audio('assets/bounce.wav');

function drawPaddle(x, y, width, height) {
    ctx.fillStyle = 'white';
    ctx.fillRect(x, y, width, height);
}

function drawBall(x, y, radius) {
    ctx.beginPath();
    ctx.arc(x, y, radius, 0, Math.PI * 2);
    ctx.fillStyle = 'white';
    ctx.fill();
    ctx.closePath();
}

function drawScore() {
    ctx.font = '24px Arial';
    ctx.fillStyle = 'white';
    ctx.fillText(`Player A: ${scoreA}  Player B: ${scoreB}`, 300, 50);
}

function drawTime() {
    const elapsedTime = Math.floor((Date.now() - startTime) / 1000);
    const timeLeft = Math.max(timeLimit - elapsedTime, 0);
    ctx.font = '24px Arial';
    ctx.fillStyle = 'white';
    ctx.fillText(`Time: ${timeLeft}s`, 20, 50);

    if (timeLeft <= 0) {
        gameState = "gameover";
    }
}

function update() {
    if (isPaused) return;

    // Clear canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw background
    ctx.drawImage(gameBackgroundImage, 0, 0, canvas.width, canvas.height);

    // Draw paddles, ball, score, and time
    drawPaddle(paddleA.x, paddleA.y, paddleA.width, paddleA.height);
    drawPaddle(paddleB.x, paddleB.y, paddleB.width, paddleB.height);
    drawBall(ball.x, ball.y, ball.radius);
    drawScore();
    drawTime();

    // Move ball
    ball.x += ball.dx;
    ball.y += ball.dy;

    // Ball collision with top and bottom
    if (ball.y + ball.radius > canvas.height || ball.y - ball.radius < 0) {
        ball.dy *= -1;
        bounceSound.play();
    }

    // Ball collision with paddles
    if (
        (ball.x - ball.radius < paddleA.x + paddleA.width && ball.y > paddleA.y && ball.y < paddleA.y + paddleA.height) ||
        (ball.x + ball.radius > paddleB.x && ball.y > paddleB.y && ball.y < paddleB.y + paddleB.height)
    ) {
        ball.dx *= -1;
        bounceSound.play();
    }

    // Score points
    if (ball.x + ball.radius > canvas.width) {
        scoreA++;
        resetBall();
    } else if (ball.x - ball.radius < 0) {
        scoreB++;
        resetBall();
    }

    // AI Logic
    if (aiActive) {
        if (paddleB.y + paddleB.height / 2 < ball.y && paddleB.y + paddleB.height < canvas.height) {
            paddleB.y += 5; // Move paddle B down
        } else if (paddleB.y + paddleB.height / 2 > ball.y && paddleB.y > 0) {
            paddleB.y -= 5; // Move paddle B up
        }
    }
}

function resetBall() {
    ball.x = canvas.width / 2;
    ball.y = canvas.height / 2;
    ball.dx = -ball.dx;
    ball.dy = Math.random() > 0.5 ? 5 : -5;
}

function showSplashScreen() {
    ctx.drawImage(splashImage, 0, 0, canvas.width, canvas.height);
}

function showGameOver() {
    ctx.drawImage(gameoverImage, 0, 0, canvas.width, canvas.height);
    ctx.font = '24px Arial';
    ctx.fillStyle = 'white';
    ctx.fillText(`Player A: ${scoreA}  Player B: ${scoreB}`, 275, 340);
    ctx.fillText("Press R to restart", 300, 380);
}

function gameLoop() {
    if (gameState === "splash") {
        showSplashScreen();
    } else if (gameState === "game") {
        update();
    } else if (gameState === "gameover") {
        showGameOver();
    }
    requestAnimationFrame(gameLoop);
}

document.addEventListener('keydown', (e) => {
    if (gameState === "splash" && e.key === ' ') {
        gameState = "game";
        startTime = Date.now(); // Start the timer
        resetBall();
    } else if (gameState === "splash" && e.key === 'a') {
        gameState = "game";
        aiActive = true; // Activate AI
        startTime = Date.now(); // Start the timer
        resetBall();
    } else if (gameState === "gameover" && e.key === 'r') {
        gameState = "splash";
        scoreA = 0;
        scoreB = 0;
        aiActive = false; // Reset AI activation
    } else if (e.key === 'w' && paddleA.y > 0) {
        paddleA.y -= 20;
    } else if (e.key === 's' && paddleA.y < canvas.height - paddleA.height) {
        paddleA.y += 20;
    } else if (e.key === 'ArrowUp' && paddleB.y > 0 && !aiActive) {
        paddleB.y -= 20;
    } else if (e.key === 'ArrowDown' && paddleB.y < canvas.height - paddleB.height && !aiActive) {
        paddleB.y += 20;
    } else if (e.key === 'p') {
        isPaused = !isPaused;
    }
});

gameLoop();
