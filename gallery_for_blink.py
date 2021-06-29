from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)
# 파일 업로드 용량 제한(Byte 단위) : 16MB
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return render_template('page_not_found.html'), 404

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/list')
def list():
    files = os.listdir('./uploads')
    return render_template('list.html', files=files)

@app.route('/upload')
def uploade():
    return render_template('upload.html')

@app.route('/fileUpload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        # 저장할 경로 + 파일명
        # f.save('./uploads/' + secure_filename(f.filename))
        f.save('./uploads/' + f.filename)
        return render_template('success.html')

@app.route('/download')
def download():
    files = os.listdir('./uploads')
    return render_template('download.html', files=files)

@app.route('/filedownload', methods=['GET', 'POST'])
def download_file():
    if request.method == 'POST':
        check = False
        files = os.listdir('./uploads')
        for x in files:
            if(x == request.form['file']):
                check = True
        if(check):
            path = "./uploads/"
            return send_file(path + request.form['file'], attachment_filename=request.form['file'], as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)