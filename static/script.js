$(document).ready(function() {
    // When the send button is clicked or enter key is pressed
    $('.send').click(function() {
        sendMessage();
    });

    $('#userInput').keypress(function(e) {
        if (e.which == 13) {  // Enter key pressed
            sendMessage();
            return false;    // Prevent form submission
        }
    });

    // Function to send a message to the Flask server
    function sendMessage() {
        var userText = $('#userInput').val().trim(); // Get the user input
    
        if (userText !== '') { // Check if the user input is not empty
            appendMessage(userText, 'send'); // Append the message to the chat
            $('#userInput').val(''); // Clear the input field
    
            // Post the user message to the Flask server
            $.post('/get', {msg: userText}, function(data) {
                // Append the bot response to the chat
                appendMessage(data, 'receive');
            }).fail(function() {
                // Handle errors or unsuccessful operations here
                appendMessage('Failed to get a response from the server.', 'receive');
            });
        }
    }

    // Function to append messages to the chat box
    function appendMessage(message, type) {
        var messageType = (type === 'send') ? 'chat-box-body-send' : 'chat-box-body-receive';
        var messageHtml = `<div class="${messageType}"><p>${message}</p><span>${getCurrentTime()}</span></div>`;

        $('.chat-box-body').append(messageHtml); // Append the message
        $('.chat-box-body').scrollTop($('.chat-box-body')[0].scrollHeight); // Auto scroll to the latest message
    }

    // Function to get the current time in HH:MM format
    function getCurrentTime() {
        var now = new Date();
        return now.getHours() + ':' + (now.getMinutes() < 10 ? '0' : '') + now.getMinutes();
    }
});
