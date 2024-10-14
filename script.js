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

function update() {
    // Clear canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw paddles and ball
    drawPaddle(paddleA.x, paddleA.y, paddleA.width, paddleA.height);
    drawPaddle(paddleB.x, paddleB.y, paddleB.width, paddleB.height);
    drawBall(ball.x, ball.y, ball.radius);
    drawScore();

    // Move ball
    ball.x += ball.dx;
    ball.y += ball.dy;

    // Ball collision with top and bottom
    if (ball.y + ball.radius > canvas.height || ball.y - ball.radius < 0) {
        ball.dy *= -1;
    }

    // Ball collision with paddles
    if (
        (ball.x - ball.radius < paddleA.x + paddleA.width && ball.y > paddleA.y && ball.y < paddleA.y + paddleA.height) ||
        (ball.x + ball.radius > paddleB.x && ball.y > paddleB.y && ball.y < paddleB.y + paddleB.height)
    ) {
        ball.dx *= -1;
    }

    // Score points
    if (ball.x + ball.radius > canvas.width) {
        scoreA++;
        resetBall();
    } else if (ball.x - ball.radius < 0) {
        scoreB++;
        resetBall();
    }

    requestAnimationFrame(update);
}

function resetBall() {
    ball.x = canvas.width / 2;
    ball.y = canvas.height / 2;
    ball.dx = -ball.dx;
    ball.dy = Math.random() > 0.5 ? 5 : -5;
}

// Keyboard controls
document.addEventListener('keydown', (e) => {
    if (e.key === 'w' && paddleA.y > 0) paddleA.y -= 20;
    if (e.key === 's' && paddleA.y < canvas.height - paddleA.height) paddleA.y += 20;
    if (e.key === 'ArrowUp' && paddleB.y > 0) paddleB.y -= 20;
    if (e.key === 'ArrowDown' && paddleB.y < canvas.height - paddleB.height) paddleB.y += 20;
});

update();