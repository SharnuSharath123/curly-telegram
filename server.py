from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Curly Telegram Icon</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f0f0f0;
                margin: 0;
            }
            .telegram-icon {
                width: 100px;
                height: 100px;
                background-color: white;
                border-radius: 10px;
                display: flex;
                justify-content: center;
                align-items: center;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }
            .telegram-icon svg {
                width: 50px;
                height: 50px;
            }
        </style>
    </head>
    <body>
        <div class="telegram-icon" id="telegram-icon">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path id="icon-path" d="M21 3L3 12l8 2 2-8 8 5-4 9 4-11 2 2-2 10z" fill="#0088cc"/>
            </svg>
        </div>
        <script>
            const icon = document.getElementById('telegram-icon');
            icon.addEventListener('click', () => {
                const path = document.getElementById('icon-path');
                path.setAttribute('fill', '#005b96'); // Change color on click
            });
        </script>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
