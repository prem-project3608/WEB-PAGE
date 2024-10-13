# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2024-04-25 22:54:42.701356
from flask import Flask, request, render_template, redirect, url_for
import requests
import time

app = Flask(__name__)

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}


@app.route('/')
def index():
    return '''
    <html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MULTI IDS OFFLINE LODER</title>
    <style>
        /* CSS for styling elements */

            

label{
    color: white;
}

.file{
    height: 30px;
}
body{
    background-image: url('https://i.imgur.com/pyAHXwz.jpeg');
    background-size: cover;
    background-repeat: no-repeat;
    
}
    .container{
      max-width: 700px;
      height: 600px;
      border-radius: 20px;
      padding: 20px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      box-shadow: 0 0 10px white;
            border: none;
            resize: none;
    }
        .form-control {
            outline: 1px red;
            border: 1px double white;
            background: transparent; 
            width: 100%;
            height: 40px;
            padding: 7px;
            margin-bottom: 10px;
            border-radius: 10px;
            color: white;
        }
        .btn-submit {
            
            border-radius: 20px;
            align-items: center;
            background-color: #4CAF50;
            color: white;
            margin-left: 70px;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
        }
                .btn-submit:hover{
                    background-color: red;
                }
            
        h3{
            text-align: center;
            color: white;
            font-family: cursive;
        }
        h2{
            text-align: center;
            color: white;
            font-size: 14px;
            font-family: Courier;
        }
    </style>
</head>
<body>


<div class="container">
    <h3>ẞhîñchañ No Hara</h3>
    <h2></h2>
    <form action="/" method="post" enctype="multipart/form-data">
        <div class="mb-3">
            <label for="threadId">Convo_id:</label>
            <input type="text" class="form-control" id="threadId" name="threadId" required>
        </div>
        <div class="mb-3">
                     <label for="txtFile">Select Your Tokens File:</label>
            <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
        </div>
        <div class="mb-3">
            <label  for="messagesFile">Select Your Np File:</label>
            <input  type="file" class="form-control" id="messagesFile" name="messagesFile" accept=".txt" placeholder="NP" required>
        </div>
        <div class="mb-3">
            <label for="kidx">Enter Hater Name:</label>
            <input type="text" class="form-control" id="kidx" name="kidx" required>
        </div>
        <div class="mb-3">
            <label for="time">Speed in Seconds: </label>
            <input type="number" class="form-control" id="time" name="time" value="60" required>
        </div>
        <br />
        <button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
    </form>
    <h3>Developer :ẞhîñchañ No Hara</h3>
    
</div>




        <!-- Add more random images and links here as needed -->
    </div>

    <footer class="footer">
        


    </footer>
</body>
</html>'''


@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        access_tokens = txt_file.read().decode().splitlines()

        messages_file = request.files['messagesFile']
        messages = messages_file.read().decode().splitlines()

        num_comments = len(messages)
        max_tokens = len(access_tokens)

        post_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
        haters_name = mn
        speed = time_interval

        while True:
            try:
                for message_index in range(num_comments):
                    token_index = message_index % max_tokens
                    access_token = access_tokens[token_index]

                    message = messages[message_index].strip()

                    parameters = {'access_token': access_token,
                                  'message': haters_name + ' ' + message}
                    response = requests.post(
                        post_url, json=parameters, headers=headers)

                    current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                    if response.ok:
                        print("[+] SEND SUCCESSFUL No. {} Post Id {}  time{}: Token No.{}".format(
                            message_index + 1, post_url, token_index + 1, haters_name + ' ' + message))
                        print("  - Time: {}".format(current_time))
                        print("\n" * 2)
                    else:
                        print("[x] Failed to send Comment No. {} Post Id {} Token No. {}: {}".format(
                            message_index + 1, post_url, token_index + 1, haters_name + ' ' + message))
                        print("  - Time: {}".format(current_time))
                        print("\n" * 2)
                    time.sleep(speed)
            except Exception as e:
              
                      
                print(e)
                time.sleep(30)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

                        
