# hàm refine thực hiện xoá bỏ các kí tự mà người nhập đã ấn backspace
def refine(filename, file_result):
  with open(filename, "r") as file:
      content = file.read()
  while "Key.backspace" in content:
      index = content.find("Key.backspace")
      if index > 0:
          content = content[:index - 1] + content[index + len("Key.backspace"):]
      else:
          content = content[index + len("Key.backspace"):]

  #ghi lại nội dung đã refine vào file mới
  with open(file_result, "w") as refined_file:
      refined_file.write(content)

#tên file cần được refine
filename = "log/2023-12-19_01-26-10.txt"
#file chứa nội dung sau khi được refine
file_result = filename[:-4] + "[refine]" + filename[-4:]
#gọi hàm để thực hiện refine
refine(filename, file_result)