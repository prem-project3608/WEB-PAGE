from flask import Flask, request, render_template
import requests

app = Flask(__name__)

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
}

@app.route('/')
def index():
    return '''
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>FB Login and Get Cookies</title>
    </head>
    <body>
        <h2>Login with Facebook UID</h2>
        <form action="/login" method="post">
            <label for="uid">Facebook UID:</label>
            <input type="text" id="uid" name="uid" required><br><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required><br><br>
            <input type="submit" value="Login">
        </form>
    </body>
    </html>
    '''

@app.route('/login', methods=['POST'])
def login():
    uid = request.form['uid']
    password = request.form['password']

    # Facebook login URL
    login_url = 'https://m.facebook.com/login.php'

    # Facebook login payload
    payload = {
        'email': uid,  # UID as email input
        'pass': password
    }

    with requests.Session() as s:
        # Send post request to login
        response = s.post(login_url, data=payload, headers=headers)

        # Check if login was successful
        if 'c_user' in s.cookies:
            fb_cookies = s.cookies.get_dict()
            fbstate_cookie = fb_cookies.get('c_user')  # Example fbstate extraction
            return '''
            <html>
            <body>
                <h2>Login Successful!</h2>
                <label for="fbstate">Your fbstate Cookie (UID):</label><br>
                <textarea id="fbstate" rows="4" cols="50">{}</textarea><br>
                <button onclick="copyToClipboard()">Copy Cookie</button>
                <script>
                    function copyToClipboard() {
                        var copyText = document.getElementById("fbstate");
                        copyText.select();
                        document.execCommand("copy");
                    }
                </script>
            </body>
            </html>
            '''.format(fbstate_cookie)
        else:
            return "Login failed! Check your UID and password."

if __name__ == '__main__':
    app.run(debug=True)
