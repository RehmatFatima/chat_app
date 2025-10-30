var socket = io();

var username = prompt("Enter your name:");

function sendMessage() {
  var message = document.getElementById('message').value.trim();
  if (message) {
    socket.send({ username: username, message: message });
    document.getElementById('message').value = '';
  }
}

socket.on('message', function(data) {
  var chat = document.getElementById('messages');
  if (data.username && data.message) {
    chat.innerHTML += `<b>${data.username}:</b> ${data.message}<br>`;
  } else {
    chat.innerHTML += data + '<br>';
  }
  chat.scrollTop = chat.scrollHeight;
});
