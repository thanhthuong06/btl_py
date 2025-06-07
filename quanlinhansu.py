from file import doc_du_lieu, ghi_du_lieu, FIELDNAMES
import re
from datetime import datetime
# Nhập thông tin nhân sự
VN_PROVINCES = [
    "An Giang", "Ba Ria-Vung Tau", "Bac Giang", "Bac Kan", "Bac Lieu", "Bac Ninh",
    "Ben Tre", "Binh Dinh", "Binh Duong", "Binh Phuoc", "Binh Thuan", "Ca Mau",
    "Can Tho", "Cao Bang", "Da Nang", "Dak Lak", "Dak Nong", "Dien Bien", "Dong Nai",
    "Dong Thap", "Gia Lai", "Ha Giang", "Ha Nam", "Ha Noi", "Ha Tinh", "Hai Duong",
    "Hai Phong", "Hau Giang", "Hoa Binh", "Hung Yen", "Khanh Hoa", "Kien Giang",
    "Kon Tum", "Lai Chau", "Lam Dong", "Lang Son", "Lao Cai", "Long An", "Nam Dinh",
    "Nghe An", "Ninh Binh", "Ninh Thuan", "Phu Tho", "Phu Yen", "Quang Binh",
    "Quang Nam", "Quang Ngai", "Quang Ninh", "Quang Tri", "Soc Trang", "Son La",
    "Tay Ninh", "Thai Binh", "Thai Nguyen", "Thanh Hoa", "Thua Thien Hue", "Tien Giang",
    "Tra Vinh", "Tuyen Quang", "Vinh Long", "Vinh Phuc", "Yen Bai"
]
ds_phong_ban = ["Quan Ly", "Nhan Su", "Marketing", "Ke Toan", "Ky Thuat", "Phat Trien", "Nghien Cuu", "Thiet Ke"]
ds_chuc_vu = ["Nhan Vien", "Pho Phong", "Truong Phong", "Thu Ky", "Chu Tich", "Giam Doc"]
gia_tri_gt = ["Nam", "Nu", "Khac"]
def kiem_tra_ngay_hop_le(date_str):
    '''Kiểm tra định dạng ngày sinh và tuổi của nhân viên.
    date_str: Chuỗi ngày sinh theo định dạng DD/MM/YYYY.
    Trả về True nếu hợp lệ, False và thông báo lỗi nếu không hợp lệ.
    '''
    try:
        day, month, year = map(int, date_str.split('/'))
        input_date = datetime(year, month, day)
        current_date = datetime.now()
        if input_date >= current_date:
            return False, "Ngày sinh không được lớn hơn hoặc bằng ngày hiện tại."
        age = current_date.year - input_date.year - (
            (current_date.month, current_date.day) < (input_date.month, input_date.day)
        )
        if not (18 <= age <= 65):
            return False, "Tuổi nhân viên phải từ 18 đến 65."
        return True, ""
    except (ValueError, TypeError):
        return False, "Định dạng ngày sinh không hợp lệ (DD/MM/YYYY)."

def kiem_tra_ten_hop_le(name):
    '''Kiểm tra tính hợp lệ của họ tên.
    name: Chuỗi họ tên cần kiểm tra.
    Trả về True và tên đã chuẩn hóa nếu hợp lệ, False và thông báo lỗi nếu không hợp lệ.
    '''
    name = re.sub(r'\s+', ' ', name.strip())
    if not name or not re.match(r'^[A-Za-z\sÀ-ỹ]+$', name):
        return False, "Họ tên không được chứa ký tự đặc biệt hoặc để trống."
    words = name.split()
    if not all(word[0].isupper() for word in words):
        return False, "Họ tên phải viết hoa chữ cái đầu mỗi từ."
    return True, name
def nhap_thong_tin_nhan_su():
    '''Nhập thông tin nhân sự từ người dùng.
    Trả về một từ điển chứa thông tin nhân sự hợp lệ.
    '''
    data = doc_du_lieu()
    employee = {}
    print("Nhập thông tin nhân viên:")
    try:
        while True:
            ma_nv = input("Nhập mã nhân viên (5 số): ").strip()
            if len(ma_nv) == 5 and ma_nv.isdigit():
                if any(emp['MaNV'] == ma_nv for emp in data):
                    print("Mã nhân viên đã tồn tại. Vui lòng nhập lại.")
                else:
                    employee['MaNV'] = ma_nv
                    break
            else:
                print("Mã nhân viên phải là chuỗi 5 số. Vui lòng nhập lại.")
        while True:
            ho_ten = input("Nhập họ tên nhân viên: ").strip()
            is_valid, result = kiem_tra_ten_hop_le(ho_ten)
            if is_valid:
                employee['HoTen'] = result
                break
            else:
                print(result)
        while True:
            ngay_sinh = input("Nhập ngày sinh (DD/MM/YYYY): ").strip()
            is_valid, message = kiem_tra_ngay_hop_le(ngay_sinh)
            if is_valid:
                employee['NgaySinh'] = ngay_sinh
                break
            else:
                print(message)
        while True:
            gioi_tinh = input("Nhập giới tính (Nam/Nu/Khac): ").strip().capitalize()
            if gioi_tinh in gia_tri_gt:
                employee['GioiTinh'] = gioi_tinh
                break
            else:
                print(f"Giới tính phải là một trong {gia_tri_gt}. Vui lòng nhập lại.")
        while True:
            que_quan = input("Nhập quê quán: ").strip().title()
            if que_quan in VN_PROVINCES:
                employee['QueQuan'] = que_quan
                break
            else:
                print("Quê quán phải là một tỉnh/thành trong Việt Nam. Vui lòng nhập lại.")
        while True:
            phong_ban = input("Nhập phòng ban: ").strip().title()
            if phong_ban in ds_phong_ban:
                employee['PhongBan'] = phong_ban
                break
            else:
                print(f"Phòng ban phải là một trong {ds_phong_ban}. Vui lòng nhập lại.")
        while True:
            chuc_vu = input("Nhập chức vụ: ").strip().title()
            if chuc_vu in ds_chuc_vu:
                employee['ChucVu'] = chuc_vu
                break
            else:
                print(f"Chức vụ phải là một trong {ds_chuc_vu}. Vui lòng nhập lại.")
        while True:
            try:
                muc_luong = float(input("Nhập mức lương: ").strip())
                if muc_luong > 0:
                    employee['MucLuong'] = muc_luong
                    break
                else:
                    print("Mức lương phải lớn hơn 0. Vui lòng nhập lại.")
            except ValueError:
                print("Mức lương phải là một số. Vui lòng nhập lại.")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi nhập dữ liệu nhân viên: {e}")
        return None
    data.append(employee)
    ghi_du_lieu(data)
    print("Nhập thông tin nhân viên thành công.")
def cap_nhat_nhan_su():
   '''Cập nhật thông tin nhân viên theo mã nhân viên.
   '''
   ma_nv = input("Nhập mã nhân viên cần cập nhật: ")
   data = doc_du_lieu()
   for NV in data:
       if NV["MaNV"] == ma_nv:
           print("Thông tin nhân sự hiện tại:")
           for key, value in NV.items():
               print(f"{key}: {value}")
           while True:
               print("Chọn thông tin cần cập nhật:")
               print("1. Cập nhật họ tên nhân viên")
               print("2. Cập nhật ngày sinh")
               print("3. Cập nhật giới tính")
               print("4. Cập nhật quê quán")
               print("5. Cập nhật phòng ban")
               print("6. Cập nhật chức vụ")
               print("7. Cập nhật mức lương")
               choice = input("Nhập thông tin cần cập nhật (1-7): ")
               if choice == '1':
                     ho_ten = input("Nhập họ tên mới: ").strip()
                     is_valid, result = kiem_tra_ten_hop_le(ho_ten)
                     if is_valid:
                          NV['HoTen'] = result
                          print("Đã cập nhật họ tên.")
                     else:
                          print(result)
               elif choice == '2':
                     ngay_sinh = input("Nhập ngày sinh mới (DD/MM/YYYY): ").strip()
                     is_valid, message = kiem_tra_ngay_hop_le(ngay_sinh)
                     if is_valid:
                          NV['NgaySinh'] = ngay_sinh
                          print("Đã cập nhật ngày sinh.")
                     else:
                          print(message)
               elif choice == '3':
                     gioi_tinh = input("Nhập giới tính mới (Nam/Nu/Khac): ").strip().capitalize()
                     if gioi_tinh in gia_tri_gt:
                          NV['GioiTinh'] = gioi_tinh
                          print("Đã cập nhật giới tính.")
                     else:
                          print(f"Giới tính phải là một trong {gia_tri_gt}. Vui lòng nhập lại.")
               elif choice == '4':
                     que_quan = input("Nhập quê quán mới: ").strip().title()
                     if que_quan in VN_PROVINCES:
                          NV['QueQuan'] = que_quan
                          print("Đã cập nhật quê quán.")
                     else:
                          print("Quê quán phải là một tỉnh/thành trong Việt Nam. Vui lòng nhập lại.")
               elif choice == '5':
                     phong_ban = input("Nhập phòng ban mới: ").strip().title()
                     if phong_ban in ds_phong_ban:
                          NV['PhongBan'] = phong_ban
                          print("Đã cập nhật phòng ban.")
                     else:
                          print(f"Phòng ban phải là một trong {ds_phong_ban}. Vui lòng nhập lại.")
               elif choice == '6':
                     chuc_vu = input("Nhập chức vụ mới: ").strip().title()
                     if chuc_vu in ds_chuc_vu:
                          NV['ChucVu'] = chuc_vu
                          print("Đã cập nhật chức vụ.")
                     else:
                          print(f"Chức vụ phải là một trong {ds_chuc_vu}. Vui lòng nhập lại.")
               elif choice == '7':
                    try:
                        muc_luong = float(input("Nhập mức lương mới: ").strip())
                        if muc_luong > 0:
                            NV['MucLuong'] = muc_luong
                            print("Đã cập nhật mức lương.")
                        else:
                            print("Mức lương phải lớn hơn 0. Vui lòng nhập lại.")
                    except ValueError:
                        print("Mức lương phải là một số. Vui lòng nhập lại.")
               else:
                    print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")
               if choice in ['1', '2', '3', '4', '5', '6', '7']:
                    tiep_tuc = input("Bạn có muốn tiếp tục cập nhật thông tin khác không? (yes/no): ").strip().lower()
                    if tiep_tuc != "yes":
                        break
           ghi_du_lieu(data)
           print("Cập nhật thông tin nhân sự thành công.")
           return
   print("Không tìm thấy mã nhân viên.")
def tim_kiem_nhan_su():
    '''Tìm kiếm nhân viên theo mã nhân viên
    trả về danh sách nhân viên phù hợp với mã đã nhập.
    '''
    data = doc_du_lieu()
    ma_nv = input("Nhập mã nhân viên cần tìm kiếm: ").strip()
    found = False
    for NV in data:
       if NV["MaNV"] == ma_nv:
           print("Thông tin nhân sự tìm thấy:")
           for key, value in NV.items():
               print(f"{key}: {value}")
           found = True
           break 
    if not found:
        print("Không tìm thấy nhân viên với mã này.")
def xoa_nhan_su():
    '''Xóa nhân viên theo mã nhân viên sau khi xác nhận từ người dùng.'''
    data = doc_du_lieu()
    ma_nv = input("Nhập mã nhân viên cần xóa: ").strip()
    for NV in data:
        if NV["MaNV"] == ma_nv:
            # Hiển thị thông tin nhân viên trước khi xác nhận xóa
            print("Thông tin nhân viên tìm thấy:")
            for key, value in NV.items():
                print(f"{key}: {value}")
            
            # Hỏi xác nhận
            confirm = input("Bạn có chắc chắn muốn xóa nhân viên này? (Y/N): ").strip().upper()
            if confirm == "Y":
                data.remove(NV)
                ghi_du_lieu(data)
                print(f"Đã xóa nhân viên với mã {ma_nv}.")
            else:
                print("Đã hủy thao tác xóa.")
            return
            
    print("Không tìm thấy nhân viên với mã này.")


               
                
                
                
                
                
                
            
           







