def getScript():
    return"""
let stopTyping = false;

document.addEventListener('DOMContentLoaded', async function () {

    let screen = document.querySelector('.mobile_screen');
    let text = document.querySelector('.text_area');
    let send = document.querySelector('.send');
    let stop = document.querySelector('.stop');

    send.addEventListener('click', async function () {
        if (text.value) {
            console.log("Text found");
            let userInput = text.value;
            let user_box = document.createElement('div');
            user_box.className = 'user text_box';
            user_box.innerHTML = "<span class='emoji' style='font-size: 30px;'>👩🏻‍🦰 </span> " + userInput;
            screen.append(user_box);
            scrollToBottom()
            text.value = '';

            let botResponse = await SendToAI(userInput);

            let bot_box = document.createElement('div');
            bot_box.className = 'AI text_box';
            screen.append(bot_box);
            
            bot_box.innerHTML = "<span class='emoji' style='font-size: 30px;'>🐼 </span> ";
            scrollToBottom()
            stop.addEventListener('click', function () {
                stopTyping = true;
            });

            stopTyping = false;
            await typeEffect(bot_box, botResponse);
        } else {
            alert("Type in a message to send");
        }
    });

})

async function SendToAI(input) {
    try {
        let response = await fetch('/api/aiResponse', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 'Userinput': input })
        });
        if (response.ok) {
            let data = await response.json();
            return data.botResponse;
        } else {
            return "Error: Unable to get response from AI.";
        }
    } catch (error) {
        console.error("Error in SendToAI:", error);
        return "Oops, something went wrong!";
    }
}

async function typeEffect(element, text) {
    const typingSpeed = 50;
    let i = 0;
    while (i < text.length && !stopTyping) {
        element.innerHTML += text.charAt(i);
        i++;
        await new Promise((resolve) => setTimeout(resolve, typingSpeed));
    }
}

async function scrollToBottom() {
    screen.scrollTop = screen.scrollHeight;
}
"""
