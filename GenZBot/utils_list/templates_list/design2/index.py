def getHtml(BotName):
    return f"""
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Lobster+Two:ital,wght@0,400;0,700;1,400;1,700&display=swap"
        rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
        href="https://fonts.googleapis.com/css2?family=Lobster+Two:ital,wght@0,400;0,700;1,400;1,700&family=Rubik:ital,wght@0,300..900;1,300..900&display=swap"
        rel="stylesheet">
    <link rel="stylesheet" href="{{{{ url_for('static', filename='style.css') }}}}">
    <title>Chatbot</title>
</head>

<body>
    <div class="mobile">
        <div class="mobile_heading"><p>{BotName}</p></div>
        <div class="mobile_screen">
           
        </div>
        <div class="mobile_buttons">
            <input type="text" class="text_area" placeholder="Type your text">
            <button class="send exchange">👉</button>
            <button class="stop exchange">😵‍💫</button>
        </div>
    </div>

    <script src="{{{{ url_for('static', filename='script.js') }}}}"></script>
</body>

</html>
"""
