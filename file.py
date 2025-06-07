import os

FILE_NAME = "Nhansu.txt"
FIELDNAMES = [
    "MaNV", "HoTen", "NgaySinh", "GioiTinh",
    "QueQuan", "PhongBan", "ChucVu", "MucLuong"
]

def khoitaofile():
    '''Khởi tạo file TXT với tiêu đề nếu chưa tồn tại.'''
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', encoding='utf-8') as f:
            f.write('|'.join(FIELDNAMES) + '\n')
        print(f"Đã khởi tạo file {FILE_NAME} thành công.")

def doc_du_lieu():
    """Đọc tất cả dữ liệu từ file TXT.
    Nếu file không tồn tại, trả về danh sách rỗng.
    Nếu file tồn tại, trả về danh sách các dòng dữ liệu dưới dạng dict.
    """
    if not os.path.exists(FILE_NAME):
        print(f"File {FILE_NAME} không tồn tại.")
        return []
    data = []
    with open(FILE_NAME, mode='r', encoding='utf-8') as f:
        lines = f.readlines()
    if not lines:
        return []
    header = lines[0].strip().split('|')
    for line in lines[1:]:
        values = line.strip().split('|')
        if len(values) == len(header):
            record = {}  # Tạo từ điển trống
            for i in range(len(header)):
                record[header[i]] = values[i]
            data.append(record)
    return data

def ghi_du_lieu(data):
    """Ghi dữ liệu vào file TXT.
    data: Danh sách các dict chứa dữ liệu cần ghi.
    """
    try:
        with open(FILE_NAME, mode='w', encoding='utf-8') as f:
            f.write('|'.join(FIELDNAMES) + '\n')
            for row in data:
                line = '|'.join([str(row.get(field, '')) for field in FIELDNAMES])
                f.write(line + '\n')
    except Exception as e:
        print(f"Có lỗi xảy ra khi ghi dữ liệu vào file {FILE_NAME}: {e}")