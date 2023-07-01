import requests
import base64

token = input('Masukkan token akses GitHub: ')
username = input('Masukkan username GitHub: ')
repo_name = input('Masukkan nama repositori: ')
file_path = input('Masukkan path file yang akan diunggah: ')

headers = {
    'Authorization': f'Token {token}'
}
upload_url = f'https://api.github.com/repos/{username}/{repo_name}/contents/{file_path}'

with open(file_path, 'rb') as file:
    content = file.read()
    encoded_content = base64.b64encode(content).decode('utf-8')

    data = {
        'message': 'Upload file',
        'content': encoded_content
    }

    response = requests.put(upload_url, headers=headers, json=data)

    if response.status_code == 201:
        print('File berhasil diunggah ke GitHub.')
    else:
        print('Gagal mengunggah file ke GitHub.')
